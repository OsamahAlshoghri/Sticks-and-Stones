'''
COLLABORATIVE: START -->
'''
import pygame as pg

pg.init()

# width and height of window
WIDTH = 700
HEIGHT = 500

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
TRANSPARENT = (5, 5, 5)

# https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
# this website was used to understand how to display text in pygame

STDRD_FONT = pg.font.SysFont(None, 36)  # standard font
TITLE_FONT = pg.font.SysFont("Verdana", 50)  # font for title
SMALL_FONT = pg.font.SysFont(None, 15)  # smaller font

title1 = TITLE_FONT.render("Sticks & Stones", True, BLACK)  # title text
title1Rect = title1.get_rect(center=(WIDTH//2 - 10, 100))
title2 = TITLE_FONT.render("MAY Hurt my Bones", True, BLACK)
title2Rect = title2.get_rect(center=(WIDTH//2 - 10, 160))

# "play" text. User clicks it to go to level select menu
play = STDRD_FONT.render("Play", True, BLACK)
# "play" text rectangle. dictates text's positon
playRect = play.get_rect(center=(WIDTH//2 - 10, HEIGHT//2))

# "quit" text. User clicks it to exit the window
quit = STDRD_FONT.render("Quit", True, WHITE)
# "quit" text rectangle. dictates text's position
quitRect = quit.get_rect(center=(WIDTH//2 - 10, HEIGHT//2+70))

# "exit" text. User clicks it to go back to main menu
exit = STDRD_FONT.render("Exit", True, WHITE, RED)
# "exit" text rectangle. dictates positon of text
exitRect = exit.get_rect(left=0, top=0)

reset_txt = STDRD_FONT.render("Reset Scores", True, BLACK)
reset_rect = reset_txt.get_rect(center=(WIDTH//2, (HEIGHT//2) + 100))

# variables for the "PAUSED" text on the pause menu
pause_txt = STDRD_FONT.render("PAUSED", True, BLACK)
pause_txt_rect = pause_txt.get_rect(center=(WIDTH/2, (HEIGHT/2) - 50))

# variables for the "Resume" text on the pause menu
pause_resume = STDRD_FONT.render("Resume", True, WHITE)
pause_resume_rect = pause_resume.get_rect(center=(WIDTH/2, HEIGHT/2))

# variables for the "Quit" text on the pause menu
pause_quit = STDRD_FONT.render("Quit", True, WHITE)
pause_quit_rect = pause_quit.get_rect(center=(WIDTH/2, (HEIGHT/2) + 40))

# variables for the "GAME OVER" text on the game over screen
game_over_txt = STDRD_FONT.render("GAME OVER", True, RED)
game_over_txt_rect = game_over_txt.get_rect(center=(WIDTH/2, (HEIGHT/2) - 50))

# variables for the "Restart" text on the game over screen
game_over_restart = STDRD_FONT.render("Restart", True, WHITE)
game_over_restart_rect = game_over_restart.get_rect(center=(WIDTH/2, HEIGHT/2))

# variables for the "Quit" text on the game over screen
game_over_quit = STDRD_FONT.render("Quit", True, WHITE)
game_over_quit_rect = game_over_quit.get_rect(center=(WIDTH/2, (HEIGHT/2) + 40))

lvl_comp_text = STDRD_FONT.render("LEVEL COMPLETE", True, BLACK)
lvl_comp_text_rect = lvl_comp_text.get_rect(center=(WIDTH/2, (HEIGHT/2) - 50))

lvl_comp_next = STDRD_FONT.render("Next", True, WHITE)
lvl_comp_next_rect = lvl_comp_next.get_rect(center=(WIDTH/2, (HEIGHT/2)))

lvl_comp_quit = STDRD_FONT.render("Quit", True, WHITE)
lvl_comp_quit_rect = lvl_comp_quit.get_rect(center=(WIDTH/2, (HEIGHT/2) + 40))

GRAVITY = 0.25
'''
COLLABORATIVE: END -->
'''