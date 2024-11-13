def СhangeСoordinates(x, y) -> tuple:
    new_x, new_y = None, None
    for i in range(3):
        if 280 + 112 * i <= x:
            new_x = i
        if 160 + 112 * i <= y:
            new_y = i
    
    return new_x, new_y
