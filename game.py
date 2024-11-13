# pip install pygame
try:
    import pygame as pg
except:
    from sys import executable
    from subprocess import check_call
    check_call([executable, '-m', 'pip', 'install', 'pygame'])
    import pygame as pg

from classes import *

def NoughtsAndCrosses():
    pg.init()

    is_game = True

    screen = pg.display.set_mode((600, 600))
    screen.fill((255, 255, 255))
    pg.display.flip()

    while is_game:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_game = False
            
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                print(x, y)

        pg.display.flip()


NoughtsAndCrosses()