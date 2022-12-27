import streamlit as st
import EnglishFormula as e
import IndonesianFormula as i

language = st.sidebar.selectbox(
    "Choose your language",
    ("English", "Indonesian")
)

if language == "English":
    st.title("Password Generator")
    st.subheader("This page will help you generate random password")
    
    option = st.radio(
    "Do you want to strengthen the previous password you have created or do you want to create a new password?",
    ("Strengthen the password that I have created", "Create a new password"))
    st.markdown("You selected: "+ option)

    if option ==  "Create a new password":
        length = st.slider("Password Length", 1,100) 
        
        if length <= 7 and length >= 5:
            st.write("Weak")
        elif length <= 4:
            st.write("Very Weak")
        elif length <= 9 and length >= 8:
            st.write("Good ")
        elif length <=12 and length >= 10:
            st.write("Strong")
        elif length <= 100 and length >=13:
            st.write("Very Strong")

        uppercase = st.checkbox("Uppercase Letters")
        lowecase = st.checkbox("Lowercase Letters")
        symbols = st.checkbox("Symbols")
        numbers = st.checkbox("Numbers")

        result=st.button("Make password")


        if result:
            password = e.generate_password(length,uppercase,lowecase,symbols,numbers)
            st.write("Your password is:")
            st.code(password)
            st.markdown("Congratulations! You just made a new password :smile: :smile: :smile:") 
        else :
            st.write ("Click the button to make a password :grinning: :grinning: :grinning:" )
        

    if option == "Strengthen the password that I have created":
        title = st.text_input("Enter the password that you have created")
        length = st.slider("Password Length", 1,100)
        
        uppercase = st.checkbox("Uppercase Letters")
        lowecase = st.checkbox("Lowercase Letters")
        symbols = st.checkbox("Symbols")
        numbers = st.checkbox("Numbers")

        result=st.button("Make Password")
        if result:
            password = e.generate_password(length,uppercase,lowecase,symbols,numbers)
            password1 = title + password
            st.write("Your password is:")
            st.code(password1)
            if len (password1) <= 7 and len(password1) >= 5:
                st.write("Weak")
            elif len (password1) <= 4:
                st.write("Very Weak ")
            elif len (password1) <= 9 and len (password1) >= 8:
                st.write("Good ")
            elif len (password1) <=12 and len (password1) >= 10:
                st.write("Strong ")
            elif len (password1)<= 100 and len (password1) >=13:
                st.write("Very Strong ")

            st.markdown("Congratulations! You just made a new password :smile: :smile: :smile:")
        else :
            st.write ("Click the button to make a password :grinning: :grinning: :grinning:" )

if language == "Indonesian":
    st.title("Pembuat Kata Sandi")
    st.subheader("Halaman ini akan membantu Anda membuat kata sandi dengan acak")

    option = st.radio(
    "Apakah kamu ingin memperkuat kata sandi sebelumnya yang telah kamu buat atau ingin membuat kata sandi baru?",
    ("Perkuat kata sandi yang telah saya buat", "Buat kata sandi baru"))
    st.markdown("Kamu memilih: "+ option)
    
    if option ==  "Buat kata sandi baru":
        length = st.slider("Panjang Kata Sandi", 1,100)

        if length <= 7 and length >= 5:
            st.write("Lemah")
        elif length <= 4:
            st.write("Sangat Lemah")
        elif length <= 9 and length >= 8:
            st.write("Bagus ")
        elif length <=12 and length >= 10:
            st.write("Kuat")
        elif length <= 100 and length >=13:
            st.write("Sangat Kuat")

        uppercase = st.checkbox("Huruf Besar")
        lowecase = st.checkbox("Huruf Kecil")
        symbols = st.checkbox("Simbol")
        numbers = st.checkbox("Angka")

        result=st.button("Buat Kata Sandi")
        if result:
            password = i.generate_password(length,uppercase,lowecase,symbols,numbers)
            st.write("Kata Sandi Anda adalah:")
            st.code(password)
            st.markdown("Selamat! Kamu baru saja membuat kata sandi baru :smile: :smile: :smile:") 
        else :
            st.write ("Klik tombol untuk membuat kata sandi :grinning: :grinning: :grinning:" )
    
    if option == "Perkuat kata sandi yang telah saya buat":
        title = st.text_input("Masukkan kata sandi yang telah kamu buat ")
        length = st.slider("Panjang Kata Sandi", 1,100)


        uppercase = st.checkbox("Huruf Besar")
        lowecase = st.checkbox("Huruf kecil")
        symbols = st.checkbox("Simbol")
        numbers = st.checkbox("Angka")

        result=st.button("Buat Kata Sandi")
        if result:
            password = i.generate_password(length,uppercase,lowecase,symbols,numbers)
            password1 = title + password
            st.write("Kata sandi Anda adalah:")
            st.code(password1)
            if len (password1) <= 7 and len(password1) >= 5:
                st.write("Lemah")
            elif len (password1) <= 4:
                st.write("Lemah")
            elif len (password1) <= 9 and len (password1) >= 8:
                st.write("Bagus")
            elif len (password1) <=12 and len (password1) >= 10:
                st.write("Kuat")
            elif len (password1)<= 100 and len (password1) >=13:
                st.write("Sangat Kuat")
            st.markdown("Selamat! Kamu baru saja membuat kata sandi baru :smile: :smile: :smile:") 
        else :
            st.write ("Klik tombol untuk membuat kata sandi :grinning: :grinning: :grinning:" )
