from data import *
from functions import *
from lingowords import * 

while playing:
    woord = woord_aanmaken(words)
    woord = woord_aanmaken(words)
    woord = list(woord)
    raden = True
    while raden:
        laat_zien = laten_zien(woord, correct)
        geraden = woord_raden(team, laat_zien)
        correct = woord_checken(woord, geraden, correct)
        if geraden == woord:
            print(f"{team} heeft het het woord goed geraden")
            if team == "team 1":
                team_1_points += 1
                print(f"{team} heeft nu {team_1_points} punten")
            else:
                team_2_points += 1
                print(f"{team} heeft nu {team_2_points} punten")    
            correct = [0]
            break