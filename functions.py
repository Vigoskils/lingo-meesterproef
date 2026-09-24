import random

def woord_aanmaken(lijst:list) -> str:
    random.shuffle(lijst)
    woord = lijst[1]
    return woord

def laten_zien(woord:list, correct:list) -> str:
    laten_zien = ""
    for i in range(5):
        if i in correct:
            laten_zien += woord[i]
        else:
            laten_zien += "*"
    return laten_zien
            

def woord_raden(team:str, laat_zien:str) -> str:
    guessing = True
    while guessing:
        print(laat_zien)
        woord = input(f"welk word wil je raden {team}? ")
        woord = list(woord)
        if len(woord) != 5:
            print("het moet een 5 letter woord zijn")
        else:
            guessing = False
    return woord