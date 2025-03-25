# secret word game (version 2)
import random

secretDictionary = {
    'python': 'Popular programming language preferred for beginners',
    'phone': 'A communication device',
    'lake': 'A large water body surrounded by landmass',
    'ocean': 'A large salty water body that occupies most of the earths surface',
    'kingdom': 'Land ruled by a king or a queen',
    'jewel': 'A precious stone',
    'valley': 'Low area between hills or mountains',
    'island': 'Piece of land surrounded by a water body',
    'dome': 'Rounded roof structure',
    'crest': 'Highest point of a wave',
    'nest': "Bird's home"
}

wordsList = list(secretDictionary.keys())
random.choice(wordsList)

score = 0
incorrect = 0

