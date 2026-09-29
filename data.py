from functions import *

def nieuwe_data():
    team = "team 1"
    correct = [0]
    playing = True
    verder = "nee"

    team_1_points = 0
    team_1_wint = False
    team_1_rode_ballen = 0
    team_1_groene_ballen = 0

    team_1_ballen_lijst = [
        "groen", "groen", "groen",
        "rood", "rood", "rood",
        2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30
    ]

    team_1_kaart = kaart_generator()

    team_2_points = 0
    team_2_wint = False
    team_2_rode_ballen = 0
    team_2_groene_ballen = 0

    team_2_ballen_lijst = [
        "groen", "groen", "groen",
        "rood", "rood", "rood",
        1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29
    ]

    team_2_kaart = kaart_generator()

    gepakte_ballen = []

    return (team, correct, playing, verder,
            team_1_points, team_1_wint,
            team_1_rode_ballen, team_1_groene_ballen,
            team_1_ballen_lijst, team_1_kaart,
            team_2_points, team_2_wint,
            team_2_rode_ballen, team_2_groene_ballen,
            team_2_ballen_lijst, team_2_kaart,
            gepakte_ballen)