from data import *
from functions import *
from lingowords import * 


(team, correct, playing, verder,
team_1_points, team_1_wint,
team_1_rode_ballen, team_1_groene_ballen,
team_1_ballen_lijst, team_1_kaart,
team_2_points, team_2_wint,
team_2_rode_ballen, team_2_groene_ballen,
team_2_ballen_lijst, team_2_kaart,
gepakte_ballen) = nieuwe_data()
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
                team_1_wint = CheckPoints(team_1_points)
            else:
                team_2_points += 1
                print(f"{team} heeft nu {team_2_points} punten")    
                team_2_wint = CheckPoints(team_2_points)
            correct = [0]
            break
        if poging == 5:
            print("sorry je kansen zijn op")
            team = team_switch(team)
            woord = woord_aanmaken(words)
            poging = 0
        
    ballen_gepakt = 0
    while ballen_gepakt < 2:
        if team_1_wint or team_2_wint:
            break
        ballen_gepakt += 1
        if team == "team 1":
            bal = ballen_pakken(team_1_ballen_lijst)
            print("de bal is: ",bal)
            if bal == "groen":
                team_1_groene_ballen += 1
                team_1_wint = CheckBallen(team_1_groene_ballen)
            elif bal == "rood":
                team_1_rode_ballen += 1
                team_2_wint = CheckBallen(team_1_rode_ballen)
                ballen_gepakt = 2
            else:
                gepakte_ballen.append(bal)
                team_1_wint = kaart_checken(team_1_kaart, gepakte_ballen, "team 1")
                team_2_wint = kaart_checken(team_2_kaart, gepakte_ballen, "team 2")

        else:
            bal = ballen_pakken(team_2_ballen_lijst)
            print("de bal is: ",bal)
            if bal == "groen":
                team_2_groene_ballen += 1
                team_2_wint = CheckBallen(team_2_groene_ballen)
            elif bal == "rood":
                team_2_rode_ballen += 1
                team_1_wint = CheckBallen(team_2_rode_ballen)
                ballen_gepakt = 2
            else:
                gepakte_ballen.append(bal)
                team_2_wint = kaart_checken(team_2_kaart, gepakte_ballen, "team 2")
                team_1_wint = kaart_checken(team_1_kaart, gepakte_ballen, "team 1")
    if team_1_wint:
        verder = win_bericht("team 1")
        if verder == "ja":
            (team, correct, playing, verder,
            team_1_points, team_1_wint,
            team_1_rode_ballen, team_1_groene_ballen,
            team_1_ballen_lijst, team_1_kaart,
            team_2_points, team_2_wint,
            team_2_rode_ballen, team_2_groene_ballen,
            team_2_ballen_lijst, team_2_kaart,
            gepakte_ballen) = nieuwe_data()
        else:
            break
    elif team_2_wint:
        verder = win_bericht("team 2")
        if verder == "ja":
            (team, correct, playing, verder,
            team_1_points, team_1_wint,
            team_1_rode_ballen, team_1_groene_ballen,
            team_1_ballen_lijst, team_1_kaart,
            team_2_points, team_2_wint,
            team_2_rode_ballen, team_2_groene_ballen,
            team_2_ballen_lijst, team_2_kaart,
            gepakte_ballen) = nieuwe_data()
        else:
            break

    team = team_switch(team)

        