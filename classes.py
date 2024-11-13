class Field:
    def __init__(self) -> None:
        f = [[[(0, 0), "-", 0] for _ in range(3)] for __ in range(3) ]
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

    def Attack(self, x, y, who_attack) -> bool:
        if self.field[y][x][1] == "-":
            self.field[y][x][1] = who_attack
            return True, self.TestEndGame()
        else:
            return False, False



f = Field()
f.PrintField()
print(f.Attack(0, 2, "X"))
print(f.Attack(1, 2, "X"))
print(f.Attack(2, 2, "X"))
f.PrintField()