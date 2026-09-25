from data import *
from functions import *
from lingowords import * 

team_1_kaart = kaart_generator()
team_2_kaart = kaart_generator()

while playing:
    woord = woord_aanmaken(words)
    woord = list(woord)
    raden = True
    poging = 0
    while raden:
        poging += 1
        print("poging: ", poging)
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
        if poging == 5:
            print("sorry je kansen zijn op")
            team = team_switch(team)
            woord = woord_aanmaken(words)
            poging = 0
    ballen_gepakt = 0
    while ballen_gepakt < 2:
        ballen_gepakt += 1
        if team == "team 1":
            bal = ballen_pakken(team_1_ballen_lijst)
            print("de bal is: ",bal)
            if bal == "groen":
                team_1_groene_ballen += 1
            elif bal == "rood":
                team_1_rode_ballen += 1
            else:
                gepakte_ballen.append(bal)
                kaart_checken(team_1_kaart, gepakte_ballen, "team 1")
                kaart_checken(team_2_kaart, gepakte_ballen, "team 2")

        else:
            bal = ballen_pakken(team_2_ballen_lijst)
            print("de bal is: ",bal)
            if bal == "groen":
                team_2_groene_ballen += 1
            elif bal == "rood":
                team_2_rode_ballen += 1
            else:
                gepakte_ballen.append(bal)
                kaart_checken(team_2_kaart, gepakte_ballen, "team 2")
                kaart_checken(team_1_kaart, gepakte_ballen, "team 1")

    team = team_switch(team)
        