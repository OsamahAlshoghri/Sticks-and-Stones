from typing import Any
import pygame as pg
from pygame.locals import *
from functions import *
from misc_var import *
vector = pg.math.Vector2

'''
ABDULLAH: START -->
'''
class Sprite_Template(pg.sprite.Sprite):
    def __init__(self, width, height, x, y, imgs):
        super().__init__()
        self.width = width # width of sprite
        self.height = height # height of sprite

        self.position = vector((x, y)) # position of sprite
        self.velocity = vector(0, 0) # velocity of sprite
        
        self.def_x = x # default x position of sprite
        self.def_y = y # default y position of sprite

        self.imgs = imgs # all images for the sprite
    
    def scroll(self, speed): # scrolls the sprite when the player moves
        self.position.x += speed
'''
ABDULLAH: END -->
'''

#COLLAB
class Character(Sprite_Template):
    def __init__(self):
        super().__init__(30, 65, 190, 430, [["images/player/player0.png"], ["images/player/player-running-0.png", "images/player/player-running-1.png", "images/player/player-running-2.png"], ["images/player/player0-inv.png"], ["images/player/player-running-0-inv.png", "images/player/player-running-1-inv.png", "images/player/player-running-2-inv.png"]])

        self.idle_img = set_img(self.imgs[0][0], self.width, self.height) # image when player is idle
        self.invincible_idle_img = set_img(self.imgs[2][0], self.width, self.height) # images when the player idle and invincible
        self.running_imgs = [set_img(self.imgs[1][0], self.width, self.height), set_img(self.imgs[1][1], self.width, self.height), set_img(self.imgs[1][2], self.width, self.height)] # images when the player is running
        self.invincible_running_imgs = [set_img(self.imgs[3][0], self.width, self.height), set_img(self.imgs[3][1], self.width, self.height), set_img(self.imgs[3][2], self.width, self.height)] # images when the player is running and invincible
        self.curr_img = self.idle_img # the current image of the player. This will be the variable used to draw the player on the screem

        self.running_frames = 0 # frames used during running animation

        self.health = 10 # health of player
        self.double_jump = True # whether the player has a double jump available
        self.wall_jump = True # whether the player has a wall jump available
        self.last_side_platform_right = self.last_side_platform_left = None # represents the last platforms the player has side collided with

        self.pos_from_start = 0 # player's position from the start of the level
        self.speed = 3 # speed of the player

        self.right = False; self.left = False # represents whether the player is going right or left
        self.last_right = True; self.last_left = False # represents whether the player was last going right or left

        self.collide_right = self.collide_left = self.collide_top = self.collide_bottom = False # represents if the player is colliding with what side of a platform

        # checks if user is invincible (will turn true when colliding with enemy)
        self.invincible = False
        self.inv_frames = 0 # counter that will start when the player turns invincible. Will allow for invincibility to wear off after some time.

        self.finish = False # represents if the player has finished the current level
        self.restarted = False # represents if the player has restarted the current level
        self.quit = False # represents if the player has quit the current level

        self.coin_count = 0 # represents the number of coins the player has collected in the current level

        self.last_checkpoint = (self.def_x, self.def_y) # represents the position of the last checkpoin earned
        self.last_checkpoint_number = 0 # represents the number of the last checkpoint
        self.checkpoint_start_pos_x = 0 

        self.have_weapon = False # represents whether the player currently has a weapon
        self.weapon_width = None # represents width of player's weapon
        self.weapon_height = None # represents height of player's weapon

        self.locked = False # will lock player controls when it is True

        self.destroy_health = False
        self.heal = True

        self.jump_timer = 0 
        self.GRAVITY = 0.25 # gravity of player
    
    def update(self):
        # this if statement is used to animate the player's sprite
        if (not self.right and not self.left) or (True not in [self.collide_bottom, self.collide_top, self.collide_left, self.collide_right]): # is true if the player is idle or they are in the air
            if self.invincible:
                self.curr_img = self.invincible_idle_img
            else:
                self.curr_img = self.idle_img
            self.running_frames = 0
        else:
            if self.running_frames // 7 in [0, 1, 2] and self.collide_top:
                if self.right: # sets sprite when they are facing right
                    if self.invincible:
                        self.curr_img = self.invincible_running_imgs[self.running_frames // 7]
                    else:
                        self.curr_img = self.running_imgs[self.running_frames // 7]
                else: # sets sprite when they are facing left. it is the same as the right facing sprites but they are just flipped
                    if self.invincible:
                        self.curr_img = pg.transform.flip(self.invincible_running_imgs[self.running_frames // 7], True, False)
                    else:
                        self.curr_img = pg.transform.flip(self.running_imgs[self.running_frames // 7], True, False)
                
                self.running_frames += 1 # frames that have passed since the player started running
                if self.running_frames // 7 > len(self.running_imgs) - 1:
                    self.running_frames = 0

        self.rect = self.curr_img.get_rect() # gets rect of sprite

        if self.invincible:
            self.inv_frames += 1 # adds to invicibility frames

            if self.inv_frames == 200: # max number of inv frames
                self.invincible = False
                self.inv_frames = 0
        
        self.locked = self.position.y > HEIGHT

        # checks if key is left, which moves the player to the left
        if ((pg.key.get_pressed())[K_LEFT] or pg.key.get_pressed()[K_a]) and not self.locked:
            self.left = self.last_left = True
            self.right = self.last_right = False
        # checks if key is right, which moves the player to the right
        elif ((pg.key.get_pressed())[K_RIGHT] or pg.key.get_pressed()[K_d]) and not self.locked:
            self.left = self.last_left = False
            self.right = self.last_right = True
        # otherwise, the player is not moving
        else:
            self.left = self.right = False
        
        # adds y velocity to position of player
        self.position.y += self.velocity.y

        # sets the center bottom of the sprite to the position variable that is affected by the velocity
        self.rect.midbottom = self.position
    
    def collision_check(self, enemies, projectiles, artillery_shells, platforms, weapons, checkpoints, finish, coins, consumables):
        '''
        COLLABORATIVE: START -->
        '''
        if platforms:  # checks to see if the player is colliding with any platform

            # an ai tool (ChatGPT) was used as a TOOL to assist in establishing the platform collisions
            for platform in platforms:  # loops through all platforms the player is currently colliding with
                # checks to see if player is colliding with the left of the platform
                if self.rect.right >= platform.rect.left and not (self.rect.left > platform.rect.left) and not self.rect.bottom - 10 <= platform.rect.top and not self.rect.top + 10 >= platform.rect.bottom:
                    self.collide_right = True
                    self.collide_left = False

                    if not self.last_side_platform_right == platform: # checks if the player has collided with the same platform as they had the last time
                        self.last_side_platform_right = platform # this self.last_side_platform variable is used to ensure that the player cannot use wall jumps on the same wall consecutively
                        self.wall_jump = True # enables player wall jump
                    self.last_side_platform_left = None
                    
                    if self.velocity.y < 1:
                        self.velocity.y += self.GRAVITY
                    else:
                        self.velocity.y = 1
                else:
                    self.collide_right = False

                # checks to see if player is colliding with the right of the platform.
                if self.rect.left <= platform.rect.right and not (self.rect.right < platform.rect.right) and not self.rect.bottom - 10 <= platform.rect.top and not self.rect.top + 10 >= platform.rect.bottom:
                    self.collide_left = True
                    self.collide_right = False

                    # checks to see if this wall is different than the one the player has last been on.
                    # if so, it reset the player's wall jump. This is to prevent players from wall jumping from the same wall consecutively.
                    if not self.last_side_platform_left == platform: 
                        self.last_side_platform_left = platform 
                        self.wall_jump = True 
                    self.last_side_platform_right = None
                    
                    if self.velocity.y < 1: 
                        self.velocity.y += self.GRAVITY
                    else:
                        self.velocity.y = 1
                else:
                    self.collide_left = False
                
                # checks to see if the player fell on top of the platform
                if self.rect.bottom >= platform.rect.top and self.velocity.y >= 0 and not (self.rect.top > platform.rect.top) and not self.collide_left and not self.collide_right:
                    self.collide_top = True

                    if self.velocity.y > 0:
                    # sets player position to top of platform
                        self.position.y = platform.rect.top + 1
                        self.velocity.y = 0  # resets y velocity
                        self.double_jump = self.wall_jump = True  # refreshes player's double jump
                else:
                    self.collide_top = False

                # same as above if statement but checks for if player hits bottom of platform
                if self.rect.top <= platform.rect.bottom and self.velocity.y < 0 and not (self.rect.bottom < platform.rect.bottom) and not self.collide_left and not self.collide_right:
                    self.collide_bottom = True
                    self.position.y = platform.rect.bottom + self.rect.height
                    self.velocity.y = 0
                else:
                    self.collide_bottom = False
                  
        else:
            # if there is no collision, continue to increase player's velocity downwards
            self.velocity.y += self.GRAVITY
            self.collide_right = self.collide_left = self.collide_top = self.collide_bottom = False
        '''
        COLLABORATIVE: END -->
        '''

        '''
        ABDULLAH: START -->
        '''
        # checks to see if the player is colliding with any enemies or projectiles
        if enemies or projectiles or artillery_shells:

            if enemies and not isinstance(enemies[0], Spikes) and not isinstance(enemies[0], Spider):
                if not enemies[0].frozen and not self.invincible:
                    self.health -= 1
                    self.invincible = True
            elif (enemies and (isinstance(enemies[0], Spikes) or isinstance(enemies[0], Spider)) and not self.invincible):
                self.health -= 1
                self.invincible = True
            elif (projectiles or artillery_shells) and not self.invincible:
                self.health -= 1
                for projectile in projectiles:
                    del projectile
                for shell in artillery_shells:
                    del shell

            if self.health == 0:  # if health is 0, quits program
                self.dead = True
                return

        # if the player collides with a weapon lying on the ground, they will pick it up
        if weapons:
            if not self.have_weapon:
                self.have_weapon = True
                for weapon in weapons:
                    self.weapon_width = weapon.width
                    self.weapon_height = weapon.height
                    del weapon

        if checkpoints: # checks to see if player has collided with checkpoint
            for checkpoint in checkpoints:
                if checkpoint.number > self.last_checkpoint_number: # if the checkpoint they collided with is later in the level than the last checkpoint they had, it sets the latest checkpoint to this one
                    self.last_checkpoint_number = checkpoint.number # sets checkpoint number as the last checkpoint number
                    self.last_checkpoint = (checkpoint.def_x, checkpoint.def_y - (checkpoint.height / 2)) # sets the reset location of the player to the checkpoint's location
                    self.checkpoint_start_pos_x = self.start_pos_x # saves the start_pos_x variable so that the scrolling can remain uninterrupted when the player returns to the checkpoint
                    checkpoint.earned = True
        '''
        ABDULLAH: END -->
        '''

        '''
        OSAMAH: START -->
        '''
        if finish:  # makes self.finish true if the player touches the yellow square
            self.finish = True
        else:
            self.finish = False

        if coins:
            self.coin_count += 1

        if consumables: # checks to see if player has used any consumables
            for cons in consumables:
                if cons.type == "health" and self.health < 10 and self.heal:
                    self.health += 1
                    self.destroy_health = True
                    self.heal = False
                else:
                    self.destroy_health = False
                    self.heal = True

                if cons.type == "jump":
                    self.GRAVITY = 0.125
                    self.jump_timer = 1
            
        if (self.jump_timer == 100) or (self.velocity.y == 0 and not self.jump_timer == 1) or not self.double_jump:
            self.GRAVITY = 0.25
            self.jump_timer = 0
        elif self.jump_timer > 0:
            self.jump_timer += 1
        '''
        OSAMAH: END -->
        '''

    '''
    ABDULLAH: START -->
    '''
    def throw_weapon(self, weapon_grp):
        if self.have_weapon:
            if self.last_left: # if the player is facing left, then shoot the weapon left
                weapon = Projectile(self.weapon_width, self.weapon_height, self.rect.midleft)
                weapon.velocity.x = -5
            else: # if the player is facing right, then shoot the weapon right
                weapon = Projectile(self.weapon_width, self.weapon_height, self.rect.midright)
                weapon.velocity.x = 5
            
        try:
            weapon_grp.add(weapon) # adds the now moving weapon to a sprite group to check for collision with enemies and platforms
        except:
            pass
        
        # resets all weaopn related values on the Character sprite
        self.have_weapon = False
        self.weapon_width = self.weapon_height = self.weapon_color = None

    def default(self, x, y, start_pos_x): # defaults all variable values
        self.position.x = x
        self.position.y = y
        self.velocity = vector(0, 0)

        self.curr_img = self.idle_img
        self.rect = self.curr_img.get_rect()

        self.rect.midbottom = self.position

        self.health = 10
        self.double_jump = self.wall_jump = True

        self.pos_from_start = 0
        self.start_pos_x = start_pos_x
        self.start_scroll = 60
        self.speed = 3

        self.right = False; self.last_right = True
        self.left = False; self.last_left = False
        
        self.collide_top = self.collide_bottom = self.collide_right = self.collide_left = False

        self.invincible = False
        self.inv_frames = 0

        self.finish = False
        self.restarted = False
        self.quit = False

        self.coin_count = 0

        self.have_weapon = False
        self.weapon_width = self.weapon_height = None

        self.last_checkpoint = (self.def_x, self.def_y)
        self.last_checkpoint_number = 0
        self.checkpoint_start_pos_x = 0

        self.destroy_health = False
        self.heal = True

        self.jump_timer = 0
        self.GRAVITY = 0.25

        self.locked = False
    '''
    ABDULLAH: END -->
    '''

'''
ABDULLAH: START -->
'''
class Inanimate_Sprite(Sprite_Template):
    def __init__(self, width, height, x, y, imgs):
        super().__init__(width, height, x, y, imgs)
        self.surface = set_img(imgs[0], width, height) # image of the sprite
        self.surface.set_colorkey(TRANSPARENT)
        self.rect = self.surface.get_rect(midbottom=(x,y))

    def update(self): # updates position of sprite
        self.rect.midbottom = self.position

    def default(self): # defaults all values
        self.position = vector((self.def_x, self.def_y))
        self.rect.midbottom = self.position
'''
ABDULLAH: END -->
'''

'''
ABDULLAH: START -->
'''
class Animate_Sprite(Sprite_Template):
    def __init__(self, width, height, x, y, imgs):
        super().__init__(width, height, x, y, imgs)
        self.surface = set_img(imgs[0][0], width, height) # image of the sprite
        self.rect = self.surface.get_rect()

        self.surface.set_colorkey(TRANSPARENT)

        self.rect.midbottom = self.position

    def update(self): # updates position of the sprite
        self.rect.midbottom = self.position

    def default(self): # defaults all values
        self.position = vector((self.def_x, self.def_y))
        self.velocity = vector(0, 0)
        self.rect.midbottom = self.position
'''
ABDULLAH: END -->
'''

'''
COLLABORATIVE: START -->
'''
class Enemy(Animate_Sprite): # standard enemies that move back and forth
    def __init__(self, width, height, x, y, speed, max_frames, imgs=[['images/enemy/enemy0.png', 'images/enemy/enemy1.png'], ["images/enemy/enemy0-frozen.png", "images/enemy/enemy1-frozen.png"]]):
        super().__init__(width, height, x, y, imgs)

        self.stdrd_imgs = self.imgs[0] # all normals images
        self.frozen_imgs = self.imgs[1] # all images for when the sprite is frozen
        self.ani_position = 0 # what image should be used within the animation of the sprite at a given point in time

        self.speed = speed # speed of sprite
        self.default_speed = int(speed)

        self.move_frames = 0 # frames when the sprite moves
        self.max_frames = max_frames # the max frames it can move

        self.ani_frames = 0 # frames used to animate sprite
        self.max_ani_frames = 60 # used to determine speed of animation

        self.frozen = False # whether the enemy frozen
        self.frozen_frames = 0 # frames since the enemy was frozen
        self.max_frozen_frames = 200 # maximum number of frames since the enemy was frozen

    def update(self): # updates position
        if self.speed > 0: #
            # depending on the ani frames variable, the image for the sprite is chosen through the ani position variable 
            if self.ani_frames == self.max_ani_frames / 2:
                self.ani_position = 0
            elif self.ani_frames == self.max_ani_frames:
                self.ani_position = 1
                self.ani_frames = 0

            if not self.frozen:
                self.ani_frames += 1
        
        # depending on the ani position variable, sets image of sprite
        if self.frozen:
            self.surface = set_img(self.frozen_imgs[self.ani_position], self.width, self.height)
        else:
            self.surface = set_img(self.stdrd_imgs[self.ani_position], self.width, self.height)

        self.rect = self.surface.get_rect()

        # updates frozen frames of sprite
        if self.frozen_frames < self.max_frozen_frames and self.frozen:
            self.frozen_frames += 1
        else:
            self.frozen_frames = 0
            self.frozen = False

        # modifies position of sprite
        if not self.frozen:
            if self.move_frames <= self.max_frames // 2:
                self.position.x += self.speed
                self.move_frames += 1
            else:
                self.position.x -= self.speed
                self.move_frames += 1
                if self.move_frames == self.max_frames:
                    self.move_frames = 0
                self.position.y += self.velocity.y

        super().update()

    def collision_check(self, platforms, active_weapons): # checks collisions between platforms and player weapons
        if self in platforms:
            for platform in platforms[self]:
                # stops enemy movement when they are moving against a wall
                if (self.rect.right > platform.rect.left and not (self.rect.left > platform.rect.left) and not self.rect.bottom - 1 <= platform.rect.top and self.move_frames <= self.max_frames // 2) or (self.rect.left < platform.rect.right and not (self.rect.right < platform.rect.right) and not self.rect.bottom - 1 <= platform.rect.top and self.move_frames < self.max_frames):
                    self.speed = 0
                else:
                    self.speed = int(self.default_speed)
                
                # ensures enemies stay on top of platforms
                if self.rect.bottom > platform.rect.top and self.velocity.y >= 0:
                    self.position.y = platforms[self][0].rect.top + 1
                    self.velocity.y = 0
        else:
            self.velocity.y += GRAVITY
        
        if self in active_weapons: # freezes enemy when hit by a player weapon
            self.frozen = True

    def default(self): # defaults all values
        super().default()
        self.speed = self.default_speed
        self.move_frames = 0
        
        self.frozen = False
        self.frozen_frames = 0
'''
COLLABORATIVE: START -->
'''

'''
ABDULLAH: START -->
'''
class Projectile_Enemy(Enemy): # enemies that move back and forth and shoot projectiles
    def __init__(self, width, height, x, y, speed, max_frames, shoot_counter):
        super().__init__(width, height, x, y, speed, max_frames, [["images/projectile-enemy/projectile-enemy0.png", "images/projectile-enemy/projectile-enemy1.png"], ["images/projectile-enemy/projectile-enemy0-frozen.png", "images/projectile-enemy/projectile-enemy1-frozen.png"]])

        self.max_distance = 600 # maximum distance from which the sprite can shoot the player from
        self.shoot_counter = shoot_counter # number of frames between each projectile shot
        self.shoot_timer = self.shoot_counter + 50 # tracks the number of frames since the last projectile shot
    
    # this function lets this sprite shoot projectiles that can harm the player
    def shoot(self, sprites: pg.sprite.Group(), player: Character):
        if not self.frozen and abs(self.position.x - player.position.x) <= self.max_distance:
            if self.shoot_timer == self.shoot_counter:
                if self.move_frames <= self.max_frames // 2: # if the enemy is moving right, set the release point of the projectlie to be at the right of the sprite and set the velocity to go right
                    projectile = Projectile(10, 10, self.rect.midright)
                    projectile.velocity.x = 5
                else: # if the enemy is moving left, set the release point of the projectlie to be at the left of the sprite and set the velocity to go left
                    projectile = Projectile(10, 10, self.rect.midleft)
                    projectile.velocity.x = -5

                try: # adds projectile to a projectile sprite group that can be used in collision checks
                    sprites.add(projectile)
                except:
                    pass

        if self.shoot_timer > 0:
            self.shoot_timer -= 1

        # sets shoot timer to shoot counter when timer is up, allowing the nemy to shoot a projectile
        if self.shoot_timer == 0 and abs(self.position.x - player.position.x) <= self.max_distance:
            self.shoot_timer = self.shoot_counter

    def default(self):
        super().default()
        self.shoot_timer = self.shoot_counter + 50
'''
ABDULLAH: END -->
'''

'''
ABDULLAH: START -->
'''
class Projectile(Inanimate_Sprite): # projectiles that is shot by projectile enemy
    def __init__(self, width, height, xy):
        super().__init__(width, height, xy[0], xy[1], ["images/projectile/projectile.png"])

    def collision_check(self, platforms): # deletes projectile when it collides with something
        if self in platforms:
            del self

    def update(self): # updates position of sprite
        self.position.x += self.velocity.x
        self.rect.midbottom = self.position
'''
ABDULLAH: END -->
'''

'''
OSAMAH: START -->
'''
class Spikes(Inanimate_Sprite): # stationary enemies that looks like spikes
    def __init__(self, width, height, x, y):
        super().__init__(width, height, x, y, ["images/spikes/spikes.png"])
'''
OSAMAH: END -->
'''

'''
OSAMAH: START -->
'''
class Spider(pg.sprite.Sprite): # spider enemy that crawls from the top of the screen
    def __init__(self, width, height, x, y, speed):
        super().__init__()
        self.surface = pg.Surface((width, height))
        self.surface.fill(PURPLE)

        self.color = PURPLE

        self.position = vector((x, y))
        self.surface.set_colorkey(TRANSPARENT)

        self.def_x = x
        self.def_y = y

        self.rect = self.surface.get_rect()
        self.rect.midbottom = self.position

        self.speed = speed
        self.frame = 0 # frame is used to check when spider moves up or down

        self.web_surface = pg.Surface((width/4, 2000))
        self.web_surface.fill(WHITE)
        self.web_position = vector((x, 0))
        self.web_rect = self.web_surface.get_rect()
        self.web_rect.midbottom = self.position

        self.def_web_x = x

    def update(self):
        if self.frame <= 200: # moves spider down
            self.position.y += self.speed
        elif self.frame > 300 and self.frame <= 500: # moves spider up
            self.position.y -= self.speed
        else: # resets frames for the spider
            if self.frame == 600:
                self.frame = 0
        self.frame += 1

        # updates spider and web position
        self.rect.midbottom = self.position
        self.web_rect.midbottom = self.position

    def scroll(self, speed):
        self.position.x += speed
    
    def default(self):
        self.position = vector((self.def_x, self.def_y))
        self.rect.midbottom = self.position

        self.web_position = vector((self.def_web_x, 0))
        self.frame = 0
'''
OSAMAH: START -->
'''

'''
OSAMAH: START -->
'''
class Artillery(Enemy): # stationary enemy that shoots projectiles in an arc
    def __init__(self, width, height, x, y, max_distance=400):
        super().__init__(width, height, x, y, 0, 400, [["images/artillery/artillery.png"], ["images/artillery/artillery-frozen.png"]])

        # creates artillery projectile
        self.shell = Artillery_Shell(10, 10, self.position.x, self.position.y)

        self.artillery_counter = 150 # number of frames between each projectile shot
        self.artillery_timer = self.artillery_counter + 100 # timer that tracks the frames since the last artillery shot
        self.max_distance = max_distance # the maximum distance (in pixels) that the artillery can shoot the player from

    def target(self, player: Character, shell_grp: pg.sprite.Group()):
        if self.artillery_timer == self.artillery_counter and abs(self.position.x - player.position.x) < self.max_distance and not self.frozen:
            shell_grp.add(self.shell)

            # sets the target of the artillery to the player's position
            self.shell.target_x = player.position.x
            self.shell.target_y = player.position.y
            
            self.shell.progress = 90 # this number goes down while the projectile is in motion an deletes the projectile once it hits 0
            self.shell.velocity = vector(0, -9.25)
            self.shell.position = vector(self.position.x, self.position.y)
        
        self.artillery_timer -= 1 # ticks down the counter for the artillery shot

        if self.artillery_timer == 0:
            self.artillery_timer = self.artillery_counter
    
    def shoot(self):
        if self.shell.progress > -40:
            # moves the artillery shell
            distance = self.shell.target_x - self.position.x
            # speed must be divided by the amount of progress frames to reach the player at the correct time
            self.shell.velocity.x = distance / 90
            self.shell.velocity.y += 0.2
            self.shell.progress -= 1

            self.shell.position += self.shell.velocity
            self.shell.rect.midbottom = self.shell.position
        else:
            self.shell.position = vector(self.position.x, self.position.y)
            self.shell.rect.midbottom = self.shell.position

    def collision_check(self, platforms, active_weapons, shell_grp):
        super().collision_check(platforms, active_weapons)

        if self in active_weapons:
            shell_grp.remove(self.shell)
'''
OSAMAH: END -->
'''

'''
OSAMAH: START -->
'''
class Artillery_Shell(Inanimate_Sprite): # artillery shell that is used by artillery enemy
    def __init__(self, width, height, x, y):
        super().__init__(width, height, x, y, ["images/artillery-shell/artillery-shell.png"])
        self.progress = 0
        self.target_x = None
        self.target_y = None

    def collision_check(self, platforms):
        if self in platforms:
            del self

    def scroll(self, speed):
        super().scroll(speed)
        self.target_x += speed
'''
OSAMAH: END -->
'''

'''
OSAMAH: START -->
'''
class Platform(pg.sprite.Sprite):  # class for platforms the player moves on
    def __init__(self, sizeX, sizeY, posX, posY):
        super().__init__()
        self.surface = pg.Surface((sizeX, sizeY))  # size of the platform
        self.surface.fill((162, 162, 162))  # color of the platform

        self.rect = self.surface.get_rect(center=(posX, posY))  # position of the platform

        self.def_x = posX
        self.def_y = posY

    def scroll(self, speed):
        self.rect.x += speed
    
    def default(self):
        self.rect.center = (self.def_x, self.def_y)
'''
OSAMAH: END -->
'''

'''
OSAMAH: START -->
'''
class Finish(Inanimate_Sprite): # the finish line for the player for each level
    def __init__(self, width, height, x, y):
        super().__init__(width, height, x, y, ["images/finish/finish.png"])

    def scroll(self, speed):
        self.position.x += speed

    def update(self):
        self.rect.midbottom = self.position
    
    def default(self):
        self.position = vector((self.def_x, self.def_y))
        self.rect.midbottom = self.position
'''
OSAMAH: END -->
'''

'''
OSAMAH: START -->
'''
class Consumables(pg.sprite.Sprite): # items that provide special effects
    def __init__(self, width, height, x, y, color, type):
        super().__init__()
        self.surface = pg.Surface((width, height))
        self.surface.fill(color)

        self.color = color

        self.position = vector((x, y))
        self.velocity = vector(0, 0)
        self.surface.set_colorkey(TRANSPARENT)

        self.def_x = x; self.def_y = y

        self.rect = self.surface.get_rect()
        self.rect.midbottom = self.position

        self.type = type

    def scroll(self, speed):
        self.position.x += speed

    def update(self):
        self.rect.midbottom = self.position
    
    def default(self):
        self.position = vector((self.def_x, self.def_y))
        self.rect.midbottom = self.position
'''
OSAMAH: END -->
'''

'''
OSAMAH: START -->
'''
class Coins(Inanimate_Sprite): # collectibles that must be collected to finish a level
    def __init__(self, width, height, x, y):
        super().__init__(width, height, x, y, ["images/coin/coin.png"])
'''
OSAMAH: END -->
'''

'''
ABDULLAH: START -->
'''
class Idle_Weapon(Inanimate_Sprite): # weapons lying on the ground that the player can pick up
    def __init__(self, x, y, width=15, height=15):
        super().__init__(width, height, x, y, ["images/idle-weapon/idle-weapon.png"])
'''
ABDULLAH: END -->
'''

'''
COLLABORATIVE: START -->
'''
class Checkpoint(Inanimate_Sprite): # checkpoints the player can earn and be returned to when they fall off the edge
    def __init__(self, width, height, x, y, number):
        super().__init__(width, height, x, y, ["images/checkpoint/checkpoint-not-earned.png", "images/checkpoint/checkpoint-earned.png"])

        self.number = number
        self.earned = False

    def update(self):
        super().update()
        if self.earned:
            self.surface = set_img(self.imgs[1], self.width, self.height)

    def default(self):
        super().default()
        self.surface = set_img(self.imgs[0], self.width, self.height)
        self.earned = False
'''
COLLABORATIVE: END -->
'''