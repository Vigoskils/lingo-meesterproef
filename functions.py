import random
from termcolor import colored, cprint, COLORS

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

def woord_checken(woord:list, geraden:list, correct:list) -> list:
    dictionary = {}
    geraden_correct = []
    word_copy = woord.copy()
    for i in range(5):
        dictionary[i] = "on_black"
        if woord[i] == geraden[i]:
            dictionary[i] = "on_green"
            geraden_correct.append(i)
            if i not in correct:
                correct.append(i)
    correct_copy = geraden_correct.copy()
    correct_copy.sort(reverse=True)
    print(geraden_correct)
    for number in correct_copy:
        word_copy.pop(number)
    print(word_copy)
    
    for i in range(5):
        if geraden[i] in word_copy and dictionary[i] != "on_green":
            dictionary[i] = "on_yellow"
            for j in range(len(word_copy)):
                if word_copy[j] == geraden[i]:
                    word_copy.pop(j)
                    break
    print(dictionary)
    for i in range(5):
        if i == 4:
            cprint(f"{geraden[i]}", on_color=dictionary[i])
        else:
            cprint(f"{geraden[i]}", on_color=dictionary[i], end='')
    return correct

def ballen_pakken(ballen_lijst):
    random.shuffle(ballen_lijst)
    return ballen_lijst.pop(0)

def kaart_generator():
    bingo_kaart = []
    while len(bingo_kaart) < 16:
        getal = random.randint(1,30)
        if getal not in bingo_kaart:
            bingo_kaart.append(getal)
    i = 0
    print("-----kaart-----")
    for nummer in bingo_kaart:
        i += 1
        if i == 4:
            i = 0
            print(nummer)
        else:
            print(f"{nummer:3}", end=' ')
    return bingo_kaart

def kaart_checken(bingo_kaart, gepakt, team):
    dictionary = {

    }
    for j in range(len(bingo_kaart)):
        if bingo_kaart[j] in gepakt:
            dictionary[j] = "on_green"
        else:
            dictionary[j] = "on_black"
    print(team, ":")
    print("-----kaart-----")
    for i in range(len(bingo_kaart)):
        if (i+1)%4 == 0:
            cprint(f"{bingo_kaart[i]}", on_color=dictionary[i], end="\n")
        else:
            cprint(f"{bingo_kaart[i]:3}", on_color=dictionary[i], end=' ')

    lijn = False
    for i in range(4):
        correct = 0
        for j in range(0+4*i,4+4*i):
            if dictionary[j] == "on_green":
                correct += 1
                if correct == 4:
                    lijn = True
                    print("je hebt een horizontale lijn")

    for i in range(4):
        correct = 0
        for j in range(0+i,13+i,4):
            if dictionary[j] == "on_green":
                correct += 1
                if correct == 4:
                    lijn = True
                    print("je hebt een verticale lijn")

    for i in range(2):
        correct = 0
        for j in range(0+3*i,16-3*i, 5-2*i):
            if dictionary[j] == "on_green":
                correct += 1
                if correct == 4:
                    lijn = True
                    print("je hebt een diagonale lijn")

    return lijn

def team_switch(team):
    if team == "team 1":
        return "team 2"
    else:
        return "team 1"

def CheckPoints(points):
    if points == 10:
        print("dat betekent dat je hebt gewonnen")
        return True
    else:
        return False

def CheckBallen(ballen):
    if ballen == 3:
        return True
    else:
        return False

def win_bericht(team):
    print(f"dat betekent dat {team} heeft gewonnen")
    return input("willen jullie nog een ronde spelen").lower()