import random
import string

def generate_random(length=4):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
