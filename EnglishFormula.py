import streamlit as st
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
    if not uppercase and not lowecase and not symbols and not numbers:
        st.error("Program error! You must check at least one of the boxes above to create a password.")

