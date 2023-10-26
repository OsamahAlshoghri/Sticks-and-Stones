from functions import *
from classes import *
from objects import *
from misc_var import *
import os

# https://www.geeksforgeeks.org/getting-started-with-pygame/
# https://www.101computing.net/getting-started-with-pygame/
# these websites were used to gain an understanding of pygame and its functions

# flags were obtained through chatGPT as a way of reducing screen tearing.
flags = pg.SCALED | pg.FULLSCREEN
canvas = pg.display.set_mode((WIDTH, HEIGHT), flags)
clock = pg.time.Clock()

'''
COLLABORATIVE: START -->
'''
# stores rect values of all boxes on level select menu. used to draw the boxes to level select menu
boxes: list[pg.Rect or pg.Surface] = []
counter = 0  # keeps track of the number of boxes
for j in range(1): # loop initializes the boxes on the level select menu that will represent the levels that the user can select
    for i in range(5):
        counter += 1

        rect = pg.Rect(i * 100 + 125, j * 100 + 75, 50, 50)  # intialize box

        text = STDRD_FONT.render(str(counter), True, WHITE)  # text on the box
        # centering text onto the box
        text_rect = text.get_rect(center=rect.center)
        # position for the score text
        score_rect = text.get_rect(center=(rect.x, rect.y + 65))
        locked_rect = text.get_rect(center=(rect.x + 10, rect.y))

        # add box, text, and text_rect values to boxes array
        boxes.append([rect, text, text_rect, score_rect, counter, locked_rect])

level_completion = [False for i in range(5)] # represents the levels that have been completed
level_scores = [0 for i in range(5)] # represents the highscores for each level
'''
COLLABORATIVE: END -->
'''

'''
COLLABORATIVE: START -->
'''
if os.path.isfile('highscores.csv') and os.path.isfile('level-completion.csv'): # checks to see if highscores.csv exists as a file in this directory. if so, loads data from highscores.csv into the level_scores array
    load_data(level_scores, level_completion)
else: # if highscores.csv does not exist, creates that file with all the highscores set to 0
    with open('highscores.csv', 'w', newline="") as f: # creates highscores file
        writer = csv.writer(f)
        writer.writerow(["Level", "Highscore"])
        for i in range(10):
            writer.writerow([i + 1, 0])

    with open('level-completion.csv', 'w', newline="") as ff: # creates highscores file
        writer = csv.writer(ff)
        writer.writerow(["Level", "Completion"])
        for i in range(10):
            writer.writerow([i + 1, False])
'''
COLLABORATIVE: END -->
'''

'''
ABDULLAH: START -->
'''
# function for when the player pauses during a level
def pause():
    while True:
        canvas.fill(BLACK)  # sets background to black
        # displays all text on the pause screen
        display_text(canvas, pause_txt, pause_txt_rect, WHITE)
        display_text(canvas, pause_quit, pause_quit_rect, BLACK)
        display_text(canvas, pause_resume, pause_resume_rect, BLACK)

        for ev in pg.event.get():
            if if_quit(ev):
                ex_quit(level_scores, level_completion)

            mouse_pos = pg.mouse.get_pos()
            if mouse_in_rect(mouse_pos, pause_resume_rect): # checks to see if the cursor is in the "resume" text
                hand_cursor()
                if if_clicked(ev):
                    return # exits the function in order to resume the level
            else:
                def_cursor()

            if mouse_in_rect(mouse_pos, pause_quit_rect): # checks to see if the cursor is in the "quit" text
                hand_cursor()
                if if_clicked(ev):
                    player.quit = True # sets player.quit to true, which sets the level_num variable in ex_level() to 0, which sends the user back to the level select menu
                    return

        pg.display.update()
        clock.tick(60)
'''
ABDULLAH: END -->
'''

'''
ABDULLAH: START -->
'''
def game_over():
    while True:
        canvas.fill(BLACK)
        # draws all text for the game over screen
        display_text(canvas, game_over_txt, game_over_txt_rect, BLACK)
        display_text(canvas, game_over_restart, game_over_restart_rect, BLACK)
        display_text(canvas, game_over_quit, game_over_quit_rect, BLACK)

        for ev in pg.event.get():
            if if_quit(ev):
                ex_quit(level_scores, level_completion)

            mouse_pos = pg.mouse.get_pos()
            if mouse_in_rect(mouse_pos, game_over_restart_rect): # checks to see if the cursor is in the "restart" text
                hand_cursor()
                if if_clicked(ev):
                    player.restarted = True # sets player.restarted to true, letting them restart the level after all the sprites have been defaulted
                    return 
            else:
                def_cursor()

            if mouse_in_rect(mouse_pos, game_over_quit_rect): # checks to see if the cursor in in the "quit" text
                hand_cursor()
                if if_clicked(ev):
                    player.quit = True # sets player.quit to true, which sets the level_num variable in ex_level() to 0, which sends the user back to the level select menu
                    return

        pg.display.update()
        clock.tick(60)
'''
ABDULLAH: END -->
'''

'''
ABDULLAH: START -->
'''
def level_complete(level_num):
    while True:
        canvas.fill(BLACK)
        # draws all text for the level complete screen
        display_text(canvas, lvl_comp_text, lvl_comp_text_rect, WHITE)
        display_text(canvas, lvl_comp_next, lvl_comp_next_rect, BLACK)
        display_text(canvas, lvl_comp_quit, lvl_comp_quit_rect, BLACK)

        for ev in pg.event.get():
            if if_quit(ev):
                ex_quit(level_scores, level_completion)

            mouse_pos = pg.mouse.get_pos()
            if mouse_in_rect(mouse_pos, lvl_comp_next_rect): # checks to see if the cursor is in the "next" text
                hand_cursor()
                if if_clicked(ev):
                    return level_num # returns level_number if user clicked the next button, sending the player to the next level
            else:
                def_cursor()

            if mouse_in_rect(mouse_pos, lvl_comp_quit_rect): # checks to see if the cursor is in the "quit" text
                hand_cursor()
                if if_clicked(ev):
                    return 0 # returns 0, which sets the level_num variable in ex_level() to 0, effectively sending the player back to the level select screen (by taking them out of the cycle in the ex_ex_level() func.) instead of actually calling the level_select() function
        
        pg.display.update()
        clock.tick(60)
'''
ABDULLAH: END -->
'''


def main_game(def_group, enemy_group, platform_group, projectile_group, web_grp, artillery_grp, artillery_shell_grp, idle_weapons_grp, active_weapon_grp, checkpoints_grp, finish_grp, coins_grp, consumables_grp):
    def_cursor()
    canvas.fill(BLACK)

    '''
    COLLABORATIVE: START -->
    '''
    player_platform_collision = pg.sprite.spritecollide(player, platform_group, False)  # detects player platform collision
    player_enemy_collision = pg.sprite.spritecollide(player, enemy_group, False)  # detects player enemy collision
    player_projectile_collision = pg.sprite.spritecollide(player, projectile_group, True)  # detects player projectile collision
    player_idle_weapons_collision = pg.sprite.spritecollide(player, idle_weapons_grp, True) # detects player collision with idle weapons on the ground
    player_shell_collision = pg.sprite.spritecollide(player, artillery_shell_grp, True)  # detects player projectile collision
    player_checkpoint_collision = pg.sprite.spritecollide(player, checkpoints_grp, False) # detects player and checkpoint collision
    player_finish_collision = pg.sprite.spritecollide(player, finish_grp, False)  # detects player finish collision
    player_coins_collision = pg.sprite.spritecollide(player, coins_grp, True)  # detects player coins collision
    player_consumables_collision = pg.sprite.spritecollide(player, consumables_grp, player.destroy_health)  # detects player consumable collision

    enemy_platform_collision = pg.sprite.groupcollide(enemy_group, platform_group, False, False)  # detects enemy platform collision
    enemy_active_weapon_collision = pg.sprite.groupcollide(enemy_group, active_weapon_grp, False, True) # detects enemy and active weapon collisions
    shell_platform_collision = pg.sprite.groupcollide(artillery_shell_grp, platform_group, True, False) # detects artillery shell and platform collision
    projectile_platform_collision = pg.sprite.groupcollide(projectile_group, platform_group, True, False) # detects projectiles and platform collisions
    active_weapon_platform_collision = pg.sprite.groupcollide(active_weapon_grp, platform_group, True, False) # detects active weapons and enemy collisions

    player.collision_check(player_enemy_collision, player_projectile_collision, player_shell_collision, player_platform_collision, player_idle_weapons_collision, player_checkpoint_collision, player_finish_collision, player_coins_collision, player_consumables_collision)  # check to see for any player collisions
    
    for enemy in enemy_group: # loops through all enemies to check for collisions
        try:
            if isinstance(enemy, Artillery):
                enemy.collision_check(enemy_platform_collision, enemy_active_weapon_collision, artillery_shell_grp)
            else:
                enemy.collision_check(enemy_platform_collision, enemy_active_weapon_collision)
        except:
            pass
    # loops through all projectiles and artillery shells to check if they collide with any platforms. If so, delete that object from the system's memory. This is done to save on performance.
    for projectile in projectile_group: 
        try:
            projectile.collision_check(projectile_platform_collision)
        except:
            pass
    for shell in artillery_shell_grp:
        try:
            shell.collision_check(shell_platform_collision)
        except:
            pass

    if player.health <= 0: # checks to see if the player has lost all their health points
        game_over() # if so, then the game over screen appears
        return

    for event in pg.event.get():  # checks if the game is being closed
        if event.type == QUIT:
            ex_quit(level_scores, level_completion)
        if event.type == pg.KEYDOWN:
            # checks if up key is pressed
            if event.key == pg.K_UP or event.key == pg.K_w:
                # checks if player is on the wall and if they have a wall jump available
                if (player.collide_right or player.collide_left) and player.wall_jump:
                    player.wall_jump = False
                    player.velocity.y = -7
                # checks if player is on the floor
                elif player_platform_collision and not player.collide_right and not player.collide_left:
                    player.velocity.y = -7
                # checks if player is not on the floor but has a double jump
                elif not player_platform_collision and player.double_jump:
                    player.double_jump = False
                    player.velocity.y = -7
                player.collide_top = False

            # if the player presses the "e" key while they have a weapon, then they will throw that weapon
            if event.key == pg.K_e and player.have_weapon:  
                player.throw_weapon(active_weapon_grp)

            if event.key == pg.K_ESCAPE:
                pause()  # pauses game if the player picks the escape key
                return
            
            if if_quit(event):
                ex_quit(level_scores, level_completion)

    # checks to see if an enemy shot a projectile
    for enemy in enemy_group:
        if isinstance(enemy, Projectile_Enemy):
            enemy.shoot(projectile_group, player)

    # all artilleries sets the position of the player as their target so that can shoot it
    for s in artillery_grp:
        s.target(player, artillery_shell_grp)
    '''
    COLLABORATIVE: END -->
    '''

    '''
    ABDULLAH: START -->
    '''
    # this if statement allows the program to return the player to the last checkpoint they had crossed if they have falled off the edge of the game
    if player.position.y > 800:
        health = player.health - 1

        if player.last_checkpoint[0] != player.def_x: # this returns the player to their last acheived checkpoint
            player.position.y = player.last_checkpoint[1]

            # loops through all sprites and sets their position to be relative to the checkpoint the player returns to
            for group in [enemy_group, platform_group, projectile_group, artillery_shell_grp, idle_weapons_grp, checkpoints_grp, finish_grp, coins_grp, consumables_grp]:
                for s in group:
                    # resets position of all sprites
                    if group != platform_group:
                        s.position.x += player.pos_from_start - (player.last_checkpoint[0] - 190)
                    else:
                        s.rect.x += player.pos_from_start - (player.last_checkpoint[0] - 190)    
        
            player.pos_from_start = player.last_checkpoint[0] - 190 # resets position of player
        else: # this returns the player to the starting position if they had never acheived a checkpoint
            default_all_groups(player, player.def_x, player.def_y, player.checkpoint_start_pos_x, def_group, projectile_group, artillery_shell_grp, None, None, all_weapons, None, None, Idle_Weapon)
        
        player.health = health
    '''
    ABDULLAH: END -->
    '''

    '''
    COLLABORATIVE: START -->
    '''
    # this section allows the level to scroll with the player. It scrolls at the same speed as the player, making the player look stationary
    if not (player.collide_right and player.right) and not (player.collide_left and player.left):
        for group in [enemy_group, platform_group, projectile_group, artillery_shell_grp, idle_weapons_grp, checkpoints_grp, finish_grp, coins_grp, consumables_grp]:
            for s in group:
                if player.right: # if player is moving right, scrolls all other sprites to the left
                    s.scroll(-player.speed)
                elif player.left: # if player is moving left, scrolls all other sprites to the right
                    s.scroll(player.speed)

        # This player.pos_from_start variable represents how far the player has moved from the beginning
        # This is used to reset the position of all sprites when the player falls off an edge
        if player.right:
            player.pos_from_start += player.speed
        elif player.left:
            player.pos_from_start -= player.speed
    '''
    COLLABORATIVE: END -->
    '''

    '''
    OSAMAH: START -->
    '''                    
    # draws all sprites to the screen
    for group in [checkpoints_grp, finish_grp, coins_grp, consumables_grp, platform_group, idle_weapons_grp, active_weapon_grp, projectile_group, enemy_group, artillery_grp, web_grp, artillery_shell_grp]:
        for s in group:
            if group == artillery_grp:
                # shoots all active artillery shells
                if s.shell.target_x is not None and not s.frozen:
                    s.shoot()
            elif group == web_grp:
                canvas.blit(s.web_surface, s.web_rect)
            else:
                s.update() # calls the update function for all enemies and projectiles in order to update their positions and status
                canvas.blit(s.surface, s.rect)
    '''
    OSAMAH: END -->
    '''

    player.update()  # updates player position and status
    canvas.blit(player.curr_img, player.rect) # draws player to the screen
    draw_health(canvas, player) # draws the health bar

    pg.display.update()  # updates screen
    clock.tick(60)  # sets frame rate

'''
COLLABORATIVE: START -->
'''
# performs the all the steps necessary for executing a level
def ex_level(level_num, def_group, enemy_group=pg.sprite.Group(), platform_group=pg.sprite.Group(), projectile_group=pg.sprite.Group(), web_grp=pg.sprite.Group(), artillery_grp=pg.sprite.Group(), artillery_shell_grp=pg.sprite.Group(), idle_weapons_grp=pg.sprite.Group(), active_weapons_grp=pg.sprite.Group(), checkpoints_grp=pg.sprite.Group(), finish_grp=pg.sprite.Group(), coins_grp=pg.sprite.Group(), consumables_grp=pg.sprite.Group()):
    # sets all sprites to their default state
    default_all_groups(player, player.def_x, player.def_y, 0, def_group, projectile_group, artillery_shell_grp, all_coins, all_consumables, all_weapons, Coins, Consumables, Idle_Weapon)
    counter = 0
    
    # loops through level until the player reaches the end goal or until the player dies and chooses to restart the level
    while (not player.finish and not player.restarted and not player.quit) or (coins_grp and not player.restarted and not player.quit):
        main_game(def_group, enemy_group, platform_group, projectile_group, web_grp, artillery_grp, artillery_shell_grp, idle_weapons_grp, active_weapons_grp, checkpoints_grp, finish_grp, coins_grp, consumables_grp)  # executes the level
        counter += 1

        if player.finish and not coins_grp:
            # sets that level to be complete
            level_completion[level_num - 1] = True
            level_num += 1  # increases the level_num variable so that the program automatically moves the player to the next level after they have completed it

            # if the score is higher than last time, it changes it
            if score_calc(counter) > level_scores[level_num - 2]:
                level_scores[level_num - 2] = score_calc(counter)
            
            level_num = level_complete(level_num)

        elif player.restarted:
            # sets all sprites to their default state
            default_all_groups(player, player.def_x, player.def_y, 0, def_group, projectile_group, artillery_shell_grp, all_coins, all_consumables, all_weapons, Coins, Consumables, Idle_Weapon)
            counter = 0
        
        elif player.quit:
            level_num = 0

    return level_num
'''
COLLABORATIVE: END -->
'''


'''
OSAMAH: START -->
'''
def ex_ex_level(level_num):  # executes the ex_level function for each level. Makes it so that when the player finishes a level, it automatically moves onto the next one
    if level_num == 1:  # executes level 1
        level_num = ex_level(level_num, def_groups_1, enemies_grp_1, platform_grp_1, idle_weapons_grp=idle_weapon_grp_1, finish_grp=exits_grp_1, coins_grp = coins_grp_1, consumables_grp = consumables_grp_1)

    if level_num == 2:  # executes level 2
        level_num = ex_level(level_num, def_groups_2, enemies_grp_2, platform_grp_2, web_grp=web_grp, artillery_grp=artilleries, finish_grp=exits_grp_2, coins_grp = coins_grp_2, consumables_grp = consumables_grp_2, idle_weapons_grp=idle_weapon_grp_2, checkpoints_grp=checkpoints_grp_2)

    if level_num == 3: # executes level 3
        level_num = ex_level(level_num, def_groups_3, enemies_grp_3, platform_grp_3, idle_weapons_grp=idle_weapon_grp_3, checkpoints_grp=checkpoints_grp_3,finish_grp=exits_grp_3, coins_grp = coins_grp_3, consumables_grp = consumables_grp_3, web_grp = web_grp_2, artillery_grp=artilleries_2)
    
    if level_num == 4: # executes level 4
        level_num = ex_level(level_num, def_groups_4, enemies_grp_4, platform_grp_4, idle_weapons_grp=idle_weapon_grp_4, artillery_grp=artilleries_3, checkpoints_grp=checkpoints_grp_4, coins_grp=coins_grp_4, finish_grp=exits_grp_4, consumables_grp=consumables_grp_4, web_grp=web_grp_3)

    if level_num == 5: # executes level 5
        level_num = ex_level(level_num, def_groups_5, enemies_grp_5, platform_grp_5, web_grp=web_grp_4, artillery_grp=artilleries_4, idle_weapons_grp=idle_weapon_grp_5, checkpoints_grp=checkpoints_grp_5, finish_grp=exits_grp_5, coins_grp=coins_grp_5, consumables_grp=consumables_grp_5)
'''
OSAMAH: END -->
'''

def level_select():
    def_cursor()

    while True:
        canvas.fill(WHITE)
        canvas.blit(exit, exitRect)  # draw exit text to screen
        display_text(canvas, reset_txt, reset_rect, WHITE)

        '''
        COLLABORATIVE: START -->
        '''
        for box in boxes:
            # draws all boxes that represent different levels
            pg.draw.rect(canvas, RED, box[0])
            canvas.blit(box[1], box[2])  # draws numbers on top of those boxes
            # blits the score under the box
            canvas.blit(SMALL_FONT.render("High Score: " + str(level_scores[box[4] - 1]), True, BLACK), box[3])

            if not level_completion[box[4] - 2] and box[4] > 1: # if the level is locked, the "LOCKED" text is displayed by the box
                canvas.blit (SMALL_FONT.render("LOCKED", True, BLACK), box[5])
        '''
        COLLABORATIVE: END -->
        '''
              
        for ev in pg.event.get():
            '''
            ABDULLAH: START -->
            '''
            mouse_pos = pg.mouse.get_pos()

            if mouse_in_rect(mouse_pos, exitRect): # checks if mouse is in the Exit text rect
                hand_cursor()
                if if_clicked(ev): # returns to the main menu
                    return
            else:
                def_cursor()

            if mouse_in_rect(mouse_pos, reset_rect): # checks if mouse is in the reset scores text rect
                hand_cursor()
                if if_clicked(ev):
                    for i in range(len(boxes)): # if the user clicks on the text, it resets all scores
                        level_scores[i] = 0

            if if_quit(ev):
                ex_quit(level_scores, level_completion)
            '''
            ABDULLAH: END -->
            '''

            '''
            OSAMAH: START --> 
            '''
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_u:
                    for i in range(len(boxes)):
                        level_completion[i] = True
                if ev.key == pg.K_i:
                    for i in range(len(boxes)):
                        level_completion[i] = False
            '''
            OSAMAH: END -->
            '''

            for i in range(len(boxes)):  # loops through all boxes
                # checks to see if mouse is in any of those boxes
                if mouse_in_rect(mouse_pos, boxes[i][0]):
                    hand_cursor()
                    if if_clicked(ev):  # checks if mouse clicked a certain box
                        print(i + 1)
                        # This match case will load a different level depending on number of the box chosen. For now, there is nothing in the match cases.
                        match i + 1:
                            case 1: # executes level 1
                                ex_ex_level(1)

                            case 2: # executes level 2
                                if level_completion[0]:
                                    ex_ex_level(2)

                            case 3: # executes level 3
                                if level_completion[1]:
                                    ex_ex_level(3)

                            case 4: # executes level 4
                                if level_completion[2]:
                                    ex_ex_level(4)
                                    
                            case 5: # executes level 5
                                if level_completion[3]:
                                    ex_ex_level(5)

        pg.display.update()
        clock.tick(60)

'''
ABDULLAH: START -->
'''
def main():
    def_cursor()  # resets cursor to default look (arrow)

    while True:
        canvas.fill(WHITE)
        # displays the play, quit, and title text to window
        display_text(canvas, play, playRect, RED)
        display_text(canvas, quit, quitRect, RED)
        display_text(canvas, title1, title1Rect, WHITE)
        display_text(canvas, title2, title2Rect, WHITE)

        # loops through events (user inputs)
        for ev in pg.event.get():
            mouse_pos = pg.mouse.get_pos()  # gets current position of the cursor

            if if_quit(ev):  # checks if window was closed via the "X" in the top right corner of the window
                ex_quit(level_scores, level_completion)  # exits window

            if mouse_in_rect(mouse_pos, playRect):  # checks if "play" text was clicked
                hand_cursor()  # makes cursor look like a hand (prompts user to click)
                if if_clicked(ev):  # if user clicked the left mouse button
                    level_select()  # goes to level select menu
            else:
                def_cursor()  # resets cursor to default look (arrow)

            if mouse_in_rect(mouse_pos, quitRect):  # checks if "quit" text was clicked
                hand_cursor()
                if if_clicked(ev):
                    ex_quit(level_scores, level_completion)  # exits program

        pg.display.update()
        clock.tick(60)
main()
'''
ABDULLAH: END -->
'''