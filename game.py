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

    field = Field()
    is_game = True
    infinite_mode = False
    now_move = "X" # X or O
    tournament_mode = False
    X_score = 0
    O_score = 0
    winner_found = False
    digits = {
        "0": Zero,
        "1": One,
        "2": Two,
        "3": Three,
        "4": Four,
        "5": Five,
        "6": Six,
        "7": Seven,
        "8": Eight,
        "9": Nine
    }

    def ClearField(score, who, X_score, O_score, screen):
        if score:
            if who == "X":
                X_score += 1
            elif who == "O":
                O_score += 1

        field = Field()
        now_move = "X"
        winner_found = False

        screen = pg.display.set_mode((600, 600))
        screen.fill((255, 255, 255))
        screen.blit(FieldImg, (0, 0))

        return X_score, O_score, field, now_move, winner_found


    while is_game:
        screen.blit(FieldImg, (0, 0))
        field.DrawField(screen)
        if tournament_mode == True:
            screen.blit(TournamentMenu, (0, 152))
            O_score_str = str(O_score)
            X_score_str = str(X_score)

            for i in range(len(X_score_str)):
                screen.blit(digits[X_score_str[i]], (120 + i * 48, 280))

            for i in range(len(O_score_str)):
                screen.blit(digits[O_score_str[i]], (120 + i * 48, 392))
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
                                X_score, O_score, field, now_move, winner_found = ClearField(True, "X", X_score, O_score, screen)
                            else:
                                X_score, O_score, field, now_move, winner_found = ClearField(True, "O", X_score, O_score, screen)
                        else:
                            if now_move == "X":
                                screen.blit(CrossWon, (40, 224))
                            elif now_move == "O":
                                screen.blit(NoughtWon, (40, 224))
                            winner_found = True

                    if winner_found == False and field.CountFreePlace() == 0:
                        winner_found = True
                        screen.blit(Draw, (16, 224))
                    
                    if end_attack[0]:
                        if now_move == "X":
                            now_move = "O"
                        else:
                            now_move = "X"

                elif ((336 <= x <= 536) and (488 <= y <= 576)) or ((328 <= x <= 544) and (496 <= y <= 568)) or ((320 <= x <= 552) and (504 <= y <= 560)):
                    X_score, O_score, field, now_move, winner_found = ClearField(False, None, X_score, O_score, screen)
            
                elif (x - 63)**2 + (y - 63)**2 <= 60**2 :
                    print("--------", x, y)
                
                elif tournament_mode == True:
                    if ((32 <= x <= 232) and (488 <= y <= 576)) or ((24 <= x <= 240) and (496 <= y <= 568)) or ((16 <= x <= 248) and (504 <= y <= 560)):

                        X_score = 0
                        O_score = 0
                        screen = pg.display.set_mode((600, 600))
                        screen.fill((255, 255, 255))
                        screen.blit(FieldImg, (0, 0))

                        print("---------------2")


        pg.display.flip()


NoughtsAndCrosses()
