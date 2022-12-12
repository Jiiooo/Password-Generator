import streamlit as st
import string
import random

language = st.sidebar.selectbox(
    "Choose your language",
    ("English", "Indonesian")
)


if language == "English":
    st.title("Password Generator")

    st.write("This page is to help you generate random password")

    option = st.selectbox(
    "Do you want to strengthen the previous password you have created or do you want to create a new password?",
    ("Strengthen the password that I have created", "Create a new password"))
    st.write("You selected:", option)
    
    if option ==  "Create a new password":

        
        length = st.slider("Password Length", 6,100)

        uppercase = st.checkbox("Uppercase Letters")
        lowecase = st.checkbox("Lowercase Letters")
        symbols = st.checkbox("Symbols")
        numbers = st.checkbox("Numbers")

        def generate_password():
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
    
        password = generate_password()
        result=st.button("Make Password")
        if result:
            st.write("Your password is:")
            st.success(password)

    
    if option == "Strengthen the password that I have created":
        title = st.text_input("Enter the password that you have created")

        length = st.slider("Password Length", 1,100)

        uppercase = st.checkbox("Uppercase Letters")
        lowecase = st.checkbox("Lowercase Letters")
        symbols = st.checkbox("Symbols")
        numbers = st.checkbox("Numbers")

        def generate_password():
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
    
        password = generate_password()

        password1 = title + password

        result=st.button("Make Password")
        if result:
            st.write("Your password is:")
            st.success(password1)

        

if language == "Indonesian":
    st.title("Pembuat Kata Sandi")

    st.write("Halaman ini untuk membantu Anda membuat kata sandi dengan acak")

    option = st.selectbox(
    "Apakah kamu ingin memperkuat kata sandi sebelumnya yang telah kamu buat atau ingin membuat kata sandi baru?",
    ("Perkuat kata sandi yang telah saya buat", "Buat kata sandi baru"))
    st.write("Kamu memilih:", option)
    
    if option ==  "Buat kata sandi baru":

        
        length = st.slider("Panjang Kata Sandi", 6,100)

        uppercase = st.checkbox("Huruf Besar")
        lowecase = st.checkbox("Huruf Kecil")
        symbols = st.checkbox("Simbol")
        numbers = st.checkbox("Angka")
        def generate_password():
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
    
        password = generate_password()
        result=st.button("Buat Kata Sandi")
        if result:
            st.write("Kata Sandi Anda adalah:")
            st.success(password)

    
    if option == "Perkuat kata sandi yang telah saya buat":
        title = st.text_input("Masukkan kata sandi yang telah kamu buat ")

        length = st.slider("Panjang Kata Sandi", 1,100)

        uppercase = st.checkbox("Huruf Besar")
        lowecase = st.checkbox("Huruf kecil")
        symbols = st.checkbox("Simbol")
        numbers = st.checkbox("Angka")


        def generate_password():
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
    
        password = generate_password()

        password1 = title + password

        result=st.button("Buat Kata Sandi")
        if result:
            st.write("Your password is:")
            st.success(password1)
