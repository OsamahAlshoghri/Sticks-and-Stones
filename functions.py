import pygame as pg, sys, csv
from misc_var import *

'''
COLLABORATIVE: START -->
'''
# saves all of the player's highscores
def save_data(level_scores, level_completion):
    with open('highscores.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Level", "Highscore"])
        for i in range(5):
            writer.writerow([i + 1, level_scores[i]])

    with open('level-completion.csv', 'w', newline="") as ff:
        writer = csv.writer(ff)
        writer.writerow(["Level", "Completion"])
        for i in range(5):
            writer.writerow([i + 1, level_completion[i]])
'''
COLLABORATIVE: END -->
'''

'''
COLLABORATIVE: START -->
'''
# loads all of the player's highscores to the level_scores variable
def load_data(level_scores, level_completion):
    with open('highscores.csv', 'r', newline="") as f:
        rows = []
        for row in csv.reader(f):
            rows.append(row)

        for i in range(1, len(rows) - 1):
            print(i)
            level_scores[i - 1] = int(rows[i][1])
    
    with open('level-completion.csv', 'r', newline="") as ff:
        rows = []
        for row in csv.reader(ff):
            rows.append(row)
        
        for i in range(1, len(rows) - 1):
            level_completion[i - 1] = rows[i][1] == "True"
'''
COLLABORATIVE: END -->
'''

'''
ABDULLAH: START -->
'''
def mouse_in_rect(mouse_pos, rect: pg.Rect) -> bool:
    # returns whether the cursor is overlapping a box by getting checking if the cursor is in the box's x and y bounds
    return mouse_pos[0] in range(rect.left, rect.width + rect.left + 1) and mouse_pos[1] in range(rect.top, rect.height + rect.top + 1)
'''
ABDULLAH: END -->
'''

'''
ABDULLAH: START -->
'''
def if_quit(event) -> bool:
    # checks if user clicked red "X" at the top right of the window
    return event.type == pg.QUIT
'''
ABDULLAH: END -->
'''

'''
ABDULLAH: START -->
'''
def if_clicked(event) -> bool:
    # checks if user clicked the left mouse button
    return event.type == pg.MOUSEBUTTONDOWN and event.button == 1
'''
ABDULLAH: END -->
'''

'''
ABDULLAH: START -->
'''
def ex_quit(level_scores, level_completion):
    # executes process for exiting window
    save_data(level_scores, level_completion)
    pg.quit()
    sys.exit()
'''
ABDULLAH: END -->
'''

'''
ABDULLAH: START -->
'''
def def_cursor():
    # sets cursor to default look (arrow)
    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
'''
ABDULLAH: END -->
'''

'''
ABDULLAH: START -->
'''
def hand_cursor():
    # sets cursor to look like a hand, prompting the user to click
    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
'''
ABDULLAH: END -->
'''

'''
ABDULLAH: START -->
'''
def display_text(canvas: pg.Surface, text: pg.Surface, rect: pg.Rect, color: tuple):
    # draws text onto the window alongside the rectangle that text resides upon
    pg.draw.rect(canvas, color, rect)
    canvas.blit(text, rect)
'''
ABDULLAH: END -->
'''

'''
OSAMAH: START -->
'''
def create_platform(platform_class, platform_group, sizeX, sizeY, posX, posY): # creates a platform and adds it to a group
    platform_name = platform_class(sizeX, sizeY, posX, posY)
    platform_group.add(platform_name)
    return platform_name
def create_enemy(enemy_class, enemy_group, x, y, speed, max_frames = 400): # creates a standard enemy object
    enemy = enemy_class(50, 50, x, y, speed, max_frames)
    enemy_group.add(enemy)
    return enemy
def create_projectile_enemy(enemy_class, enemy_group, x, y, speed, max_frames=100): # creates a projectile enemy object
    enemy = enemy_class(30, 30, x, y, speed, 400, max_frames)
    enemy_group.add(enemy)
    return enemy
def create_spikes(enemy_class, enemy_group, x, y): # creates a spikes enemy object
    enemy = enemy_class(60, 30, x, y)
    enemy_group.add(enemy)
    return enemy
def create_spider(enemy_class, enemy_group, spider_group, width, height, x, y, speed): # creates a spider enemy object
    enemy = enemy_class(width, height, x, y, speed)
    enemy_group.add(enemy); spider_group.add(enemy)
    return enemy
def create_artillery(enemy_class, enemy_group, artillery_group, x, y): # creates artillery enemy object
    enemy = enemy_class(60, 40, x, y)
    enemy_group.add(enemy); artillery_group.add(enemy)
'''
OSAMAH: END -->
'''

'''
COLLABORAIVE: START -->
'''
# defaults player state as well as state of all enemies
def default_all_groups(player, x, y, start_pos_x, def_group, projectiles, shells, all_coins, all_cons, all_weapons, coin_class, con_class, weapon_class):
    player.default(x, y, start_pos_x)

    for group in def_group:
        for s in group:
            s.default()

    for projectile in projectiles:
        projectiles.remove(projectile)
        del projectile
    for shell in shells:
        shells.remove(shell)
        del shell

    # deletes all coins
    if all_coins is not None:
        for coin_grp in all_coins:
            for coin in coin_grp:
                coin_grp.remove(coin)
                del coin
        # establishes all coins in all levels
        # level 1
        all_coins[0].add(coin_class(25, 25, 30, 300))
        all_coins[0].add(coin_class(25, 25, 730, 100))
        all_coins[0].add(coin_class(25, 25, 730, 400))
        all_coins[0].add(coin_class(25, 25, 2100, 300))
        # level 2
        all_coins[1].add(coin_class(25, 25, 475, 300))
        all_coins[1].add(coin_class(25, 25, 1600, 50))
        all_coins[1].add(coin_class(25, 25, 3000, 100))
        # level 3
        all_coins[2].add(coin_class(25, 25, 400, 100))
        all_coins[2].add(coin_class(25, 25, 2325, 50))
        all_coins[2].add(coin_class(25, 25, 4000, 350))
        # level 4
        all_coins[3].add(coin_class(25, 25, 615, 170))
        all_coins[3].add(coin_class(25, 25, 1700, 250))
        all_coins[3].add(coin_class(25, 25, 2120, 410))
        # level 5
        all_coins[4].add(coin_class(25, 25, 2100, 450))
        all_coins[4].add(coin_class(25, 25, 2150, 265))
        all_coins[4].add(coin_class(25, 25, 3900, 120))

    # deletes all consumables
    if all_cons is not None:
        for con_grp in all_cons:
            for con in con_grp:
                con_grp.remove(con)
                del con

        # establishes all consumables in all levels
        # level 3
        all_cons[2].add(con_class(25,25, 3200, 50, PURPLE, "health"))
        all_cons[2].add(con_class(75, 25, 350, 490, (100, 100, 100), "jump"))
        all_cons[2].add(con_class(75, 25, 3050, 490, (100, 100, 100), "jump"))
        # level 5
        all_cons[4].add(con_class(75, 25, 2450, 190, (100, 100, 100), "jump"))
        all_cons[4].add(con_class(600, 25, 3250, 295, (100, 100, 100), "jump"))

    # deletes all idle weapons          
    for weapon_grp in all_weapons:
        for weapon in weapon_grp:
            weapon_grp.remove(weapon)
            del weapon

    # establishes all idle weapons in all levels
    # level 1
    all_weapons[0].add(weapon_class(200, 150))
    # level 2
    all_weapons[1].add(weapon_class(1300, 325))
    # level 3
    all_weapons[2].add(weapon_class(2900, 150))
    # level 4
    all_weapons[3].add(weapon_class(215, 110))
    # level 5
    for i in range(5):
        all_weapons[4].add(weapon_class(1500 + (i * 170), 145))
'''
COLLABORAIVE: END -->
'''

'''
ABDULLAH: START -->
'''
# https://stackoverflow.com/questions/27867073/how-to-put-an-image-onto-a-sprite-pygame, https://coderslegacy.com/python/how-to-resize-an-image-in-pygame/ 
# these websites was used to figure out how to load an image into pygame
def set_img(img, width, height): # returns a pygame image value
    return pg.transform.scale(pg.image.load(img), (width, height))
'''
ABDULLAH: END -->
'''

'''
OSAMAH: START -->
'''
# very simply subtracts 5000 by a timer to calculate a score
def score_calc(timer):
    return 5000 - timer
'''
OSAMAH: END -->
'''

'''
ABDULLAH: START -->
'''
# draws red rectangles outline in white with each rectangle representing one health point for the player sprite
def draw_health(canvas, player):
    for i in range(1, player.health + 1):
        pg.draw.rect(canvas, RED, [(i * 36) - 30, 5, 35, 20])
        if i < player.health:
            pg.draw.line(canvas, WHITE, ((i * 36) + 5, 5), ((i * 36) + 5, 23), 4)
    pg.draw.rect(canvas, WHITE, [6, 5, player.health * 36, 20], 2)
'''
ABDULLAH: END -->
'''