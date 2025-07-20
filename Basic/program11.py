# secret word game (version 1.1)
guess = ''
count = 0
limit = 5
playing = ''
secret_word = 'cow'

while True:
    guess = input('Enter a secret word(hint:animal,gives milk)')
    if guess != 'cow':
