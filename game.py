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
    X_score = 0
    Y_score = 0
    winner_found = False

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

                if (280 <= x <= 592) and (160 <= y <= 472) and (winner_found == False or tournament_mode):
                    print('----------1')
                    x, y = СhangeСoordinates(x, y)
                    print("--", x, y)
                    end_attack = field.Attack(x, y, now_move)
                    field.PrintField()

                    if end_attack[1] == True:
                        if tournament_mode == True:
                            if now_move == "X":
                                X_score += 1
                            else:
                                Y_score += 1
                        else:
                            print(f"Win code will be here (winner - {now_move}) ")
                            winner_found = True
                    
                    if end_attack[0]:
                        if now_move == "X":
                            now_move = "O"
                        else:
                            now_move = "X"

                elif (337 <= x <= 536) and (488 <= y <= 575):
                    screen.blit(FieldImg, (0, 0))
                    
                    field = Field()
                    now_move = "X"
                    winner_found = False

                    screen = pg.display.set_mode((600, 600))
                    screen.fill((255, 255, 255))
                    screen.blit(FieldImg, (0, 0))
            
                elif (x - 63)**2 + (y - 63)**2 <= 60**2 :
                    print("--------", x, y)
                



        pg.display.flip()


NoughtsAndCrosses()