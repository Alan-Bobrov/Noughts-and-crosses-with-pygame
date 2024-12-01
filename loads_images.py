from pygame.image import load

def Load(image):
    return load(f"images/{image}.png")

FieldImg = Load("field")
TournamentMenu = Load("tournament_menu")

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

CrossWon = Load("cross won")
NoughtWon = Load("nought won")
Draw = Load("draw")

SettingsMenu = Load("settings menu")