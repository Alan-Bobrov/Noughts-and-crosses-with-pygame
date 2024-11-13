from pygame.image import load

def Load(image):
    return load(f"images/{image}.png")

FieldImg = Load("field")

Zero = Load("zero")
One = Load("one")
Two = Load("two")
Three = Load("three")
Four = Load("four")
Five = Load("five")
Six = Load("six")
Seven = Load("seven")
Eight = Load("eight")
Nine = Load("nine")

Cross = Load("cross")
Nought = Load("nought")