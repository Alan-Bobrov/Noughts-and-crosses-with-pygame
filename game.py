# pip install pygame
try:
    import pygame as pg
except:
    from sys import executable
    from subprocess import check_call
    check_call([executable, '-m', 'pip', 'install', 'pygame'])
    import pygame as pg

from classes import *
from loads_images import *
from functions import *

def NoughtsAndCrosses():
    pg.init()
    screen = pg.display.set_mode((600, 600))
    screen.fill((255, 255, 255))
    screen.blit(FieldImg, (0, 0))

    is_game = True
    infinite_mode = False
    now_move = "X" # X or O
    tournament_mode = False

    field = Field()


    while is_game:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_game = False
            
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                print(x, y)

                if () and ():
                    x, y = СhangeСoordinates
                    end_attack = field.Attack(x, y, now_move)

                    if end_attack[1] == True:
                        print(f"Win code will be here (winner - {now_move}) ")
                    
                    if end_attack[0]:
                        if now_move == "X":
                            now_move = "O"
                        else:
                            now_move = "X"


        pg.display.flip()


NoughtsAndCrosses()