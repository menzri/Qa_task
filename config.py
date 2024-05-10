import random
import string

def generate_random(length=4):
    """Generates a random string of lowercase letters for random username and password."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
