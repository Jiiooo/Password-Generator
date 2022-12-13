import random
import string

def generate_password(length,uppercase,lowecase,symbols,numbers):
    password = []
    characters = []
    if uppercase:
        characters.extend(list(string.ascii_uppercase))
    if lowecase:
        characters.extend(list(string.ascii_lowercase))
    if symbols:
        characters.extend(list(string.punctuation))
    if numbers:
        characters.extend(list(string.digits))
    while len(password) != length:
        password.append(random.choice(characters))
    return "".join(password)