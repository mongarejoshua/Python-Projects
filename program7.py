# random password gen
import random, string

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters))


print(password)

