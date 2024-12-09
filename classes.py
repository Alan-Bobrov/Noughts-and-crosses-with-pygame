# pip install pygame
try:
    import pygame as pg
except:
    from sys import executable
    from subprocess import check_call
    check_call([executable, '-m', 'pip', 'install', 'pygame'])
    import pygame as pg

from loads_images import *
from random import randint

class Field:
    def __init__(self) -> None:
        f = [[[(280 + 112 * X, 160 + 112 * Y), "-", 0] for X in range(3)] for Y in range(3) ]
        self.field = f
    
    def PrintField(self) -> None:
        field = self.field
        for i in field:
            for j in i:
                print(j[1], end=" ")
            print()
        print()
        print()
        print()

    def DrawField(self, screen) -> None:
        for i in self.field:
            for j in i:
                if j[1] == "X":
                    screen.blit(Cross, (j[0][0], j[0][1]))
                elif j[1] == "O":
                    screen.blit(Nought, (j[0][0], j[0][1]))

    def CountSomething(self, something="-") -> int:
        counter = 0
        for i in self.field:
            for j in i:
                if j[1] == something:
                    counter += 1
        return counter
    
    def AllCoordsSomething(self, something="-", age_sort=True) -> list:
        list_something = []
        if age_sort:
            for i in range(3):
                for j in range(3):
                    if self.field[i][j][1] == something:
                        list_something.append([self.field[i][j][2], (i, j)])
            list_something.sort(reverse=True)
            return list_something
        else:
            for i in range(3):
                for j in range(3):
                    if self.field[i][j][1] == something:
                        list_something.append([self.field[i][j][2], (i, j)])
            return list_something
    
    def TestEndGame(self) -> bool:
        field = self.field

        for i in range(3):
            if field[i][0][1] == field[i][1][1] == field[i][2][1] and field[i][0][1] != "-":
                return True
            
            elif field[0][i][1] == field[1][i][1] == field[2][i][1] and field[0][i][1] != "-":
                return True
            
        if field[0][0][1] == field[1][1][1] == field[2][2][1] and field[0][0][1] != "-":
            return True
        
        if field[2][0][1] == field[1][1][1] == field[0][2][1] and field[2][0][1] != "-":
            return True
        
        return False

    def Attack(self, x, y, who_attack) -> tuple:
        if self.field[y][x][1] == "-":
            self.field[y][x][1] = who_attack
            return True, self.TestEndGame()
        else:
            return False, False
        
    def Aging(self, pr=False) -> None:
        for i in self.field:
            for j in i:
                if j[1] != "-":
                    j[2] = j[2] + 1
                if pr:
                    print(j[2], end=" ")
            if pr:
                print()

class Bot:
    def __init__(self, name="funny bot :)") -> None: 
        self.name = name

    
    def attack(self, field) -> tuple:
        counter = 0
        while True:
            counter += 1
            x = randint(0, 2)
            y = randint(0, 2)
            if field.field[y][x][1] == "-":
                return x, y
            if counter == 500:
                return 0, 0

            
# f = Field()
# f.PrintField()
# print(f.Attack(0, 2, "X"))
# print(f.Attack(1, 2, "X"))
# print(f.Attack(2, 2, "X"))
# f.PrintField()
