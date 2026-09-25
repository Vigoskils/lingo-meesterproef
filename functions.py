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