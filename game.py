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

    is_game = True
    infinite_mode = False
    now_move = "X" # X or O
    tournament_mode = False
    X_score = 0
    Y_score = 0

    field = Field()

    # #screen.blit(Cross, (280, 160))
    # screen.blit(Cross, (280, 160))
    # # screen.blit(Cross, (280 + 112, 160))
    # # screen.blit(Cross, (280 + 112 * 2, 160))
    # screen.blit(Cross, (280, 160 + 112))
    while is_game:
        screen.blit(FieldImg, (0, 0))
        field.DrawField(screen)
        if now_move == "X":
            screen.blit(Cross, (496,  48))
        else:
            screen.blit(Nought, (496,  48))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_game = False
            
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                print(x, y)

                if (280 <= x <= 616) and (160 <= y <= 496):
                    print('----------1')
                    x, y = СhangeСoordinates(x, y)
                    print("--", x, y)
                    end_attack = field.Attack(x, y, now_move)

                    if end_attack[1] == True:
                        print(f"Win code will be here (winner - {now_move}) ")
                    
                    if end_attack[0]:
                        if now_move == "X":
                            now_move = "O"
                        else:
                            now_move = "X"
            
                elif (x**2 - 56**2) + (y**2 - 56**2) <= 56**2 :
                    print("--------")



        pg.display.flip()


NoughtsAndCrosses()