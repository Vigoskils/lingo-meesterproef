import random

def woord_aanmaken(lijst:list) -> str:
    random.shuffle(lijst)
    woord = lijst[1]
    return woord