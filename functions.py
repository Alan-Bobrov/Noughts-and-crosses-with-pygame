from classes import *

def СhangeСoordinates(x, y) -> tuple:
    new_x, new_y = None, None
    for i in range(3):
        if 280 + 112 * i <= x:
            new_x = i
        if 160 + 112 * i <= y:
            new_y = i
    
    return new_x, new_y

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
