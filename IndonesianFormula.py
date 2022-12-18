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
    if not uppercase and not lowecase and not symbols and not numbers:
        st.error("Program error! Anda harus mencentang setidaknya salah satu dari box diatas untuk membuat kata sandi baru.")
    while len(password) != length:
        password.append(random.choice(characters))
    return "".join(password)

