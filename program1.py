# secret word game
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

guess = ''
count = 0
limit = 5
playing = ''

# any input from the user is considered as a string

# for word in wordsList:
#     while True:


# # while True:
# #     playing =  input('Do you want to play? (yes/no) or "q" to quit: ')

# #     if playing.lower() == 'yes':
# #         while True:
# #             guess = input('1. Enter a word (Hint --- an animal, gives us milk): ')
# #             count += 1
                    
# #             if guess != secret_word:
# #                     print('Incorrect, please try again')
# #             elif count == limit:
# #                 print('You are out of guesses.')
# #                 break
# #             elif guess == secret_word:
# #                 print('Congratulations, you got it right.\n')
# #                 guess = input('2. Enter another word --- (Hint ---- a communication device): ')
# #                 if guess != secret_word:
# #                     print('Incorrect, please try again')
# #                 elif count == limit:
# #                     print('You are out of guesses.')
# #                 break

# #     elif playing.lower() == 'no' or 'q':
# #         print('Goodbye')
# #         break
# #     else:
# #         print('Invalid choice entry, please try again.')
# #         continue
    

