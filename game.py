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
    now_move = "X" # X or O
    X_score = 0
    O_score = 0
    winner_found = False
    num_move = 0
    bot = Bot()

    settings = True
    play_with_bot = True
    tournament_mode = True
    infinite_mode = False
    #(play_with_bot, tournament_mode, infinite_mode)

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
        # Different 
        screen.blit(FieldImg, (0, 0))
        field.DrawField(screen)
        if tournament_mode == True and settings == False:
            screen.blit(TournamentMenu, (0, 152))
            O_score_str = str(O_score)
            X_score_str = str(X_score)

            for i in range(len(X_score_str)):
                screen.blit(digits[X_score_str[i]], (120 + i * 48, 280))

            for i in range(len(O_score_str)):
                screen.blit(digits[O_score_str[i]], (120 + i * 48, 392))

        if settings == True:
            screen.blit(SettingsMenu, (8, 152))
            tuple_settings = (play_with_bot, tournament_mode, infinite_mode)
            for i in range(3):
                if tuple_settings[i] == True:
                    screen.blit(On, (168, 168 + 112 * i))
                else:
                    screen.blit(Off, (168, 168 + 112 * i))

        if now_move == "X":
            screen.blit(Cross, (496,  48))
        else:
            screen.blit(Nought, (496,  48))

        if settings == False:
            if winner_found == True:
                if now_move == "X":
                    screen.blit(CrossWon, (40, 224))
                elif now_move == "O":
                    screen.blit(NoughtWon, (40, 224))
            elif winner_found == False and field.CountFreePlace() == 0:
                if tournament_mode == False:
                    screen.blit(Draw, (16, 224))

        # The bot's move, if it is active
        if play_with_bot == True and winner_found == False and num_move % 2 == 1:
            coords = bot.attack(field)
            end_bot_attack = field.Attack(coords[0], coords[1], "O")
            if end_bot_attack[1] == True:
                if tournament_mode == True:
                    if now_move == "X":
                        X_score, O_score, field, now_move, winner_found = ClearField(True, "X", X_score, O_score, screen)
                        num_move = 0
                    else:
                        X_score, O_score, field, now_move, winner_found = ClearField(True, "O", X_score, O_score, screen)
                        num_move = 0
                else:
                    print("test")
                    winner_found = True

            # print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
            # print(coords)
            num_move += 1
            field.PrintField()

            if winner_found == False:
                if now_move == "X":
                    now_move = "O"
                else:
                    now_move = "X"

        # Interaction with the game window
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_game = False
            
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                #print(x, y)
                
                if (280 <= x <= 592) and (160 <= y <= 472) and (winner_found == False or tournament_mode):
                    x, y = СhangeСoordinates(x, y)
                    end_attack = field.Attack(x, y, now_move)
                    field.PrintField()

                    if end_attack[1] == True:
                        if tournament_mode == True:
                            if now_move == "X":
                                X_score, O_score, field, now_move, winner_found = ClearField(True, "X", X_score, O_score, screen)
                                num_move = 0
                            else:
                                X_score, O_score, field, now_move, winner_found = ClearField(True, "O", X_score, O_score, screen)
                                num_move = 0
                        else:
                            winner_found = True

                    if winner_found == False and field.CountFreePlace() == 0 and tournament_mode == True:
                            X_score, O_score, field, now_move, winner_found = ClearField(False, None, X_score, O_score, screen)
                            num_move = 0
                    
                    if end_attack[0] and winner_found == False:
                        if now_move == "X":
                            now_move = "O"
                        else:
                            now_move = "X"
                        
                    num_move += 1

                elif ((336 <= x <= 536) and (488 <= y <= 576)) or ((328 <= x <= 544) and (496 <= y <= 568)) or ((320 <= x <= 552) and (504 <= y <= 560)):
                    X_score, O_score, field, now_move, winner_found = ClearField(False, None, X_score, O_score, screen)
                    num_move = 0

                # On/Off the settings menu
                elif (x - 63)**2 + (y - 63)**2 <= 60**2 :
                    screen = pg.display.set_mode((600, 600))
                    screen.fill((255, 255, 255))
                    screen.blit(FieldImg, (0, 0))
                    if settings:
                        settings = False
                    else:
                        settings = True
                
                # Clear the tournament menu
                elif tournament_mode == True:
                    if ((32 <= x <= 232) and (488 <= y <= 576)) or ((24 <= x <= 240) and (496 <= y <= 568)) or ((16 <= x <= 248) and (504 <= y <= 560)):
                        X_score = 0
                        O_score = 0
                        screen = pg.display.set_mode((600, 600))
                        screen.fill((255, 255, 255))
                        screen.blit(FieldImg, (0, 0))

                # Actions with settings menu
                if settings == True:
                    if (168 <= x <= 256):
                        if (168 <= y <= 256):
                            if play_with_bot:
                                play_with_bot = False
                            else:
                                play_with_bot = True

                        elif (168 + 112 <= y <= 256 + 112):
                            if tournament_mode:
                                tournament_mode = False
                            else:
                                tournament_mode = True

                        elif (168 + 224<= y <= 256 + 224):
                            if infinite_mode:
                                infinite_mode = False
                            else:
                                infinite_mode = True
                        


        pg.display.flip()


NoughtsAndCrosses()
