import streamlit as st

st.subheader('Log In : ')
email = st.text_input('Enter Your Email')
password = st.text_input('Enter your password')

btn = st.button('Click here !')

# if the btn is clicked !
if btn:
    if email == 'ayushsuthar@gmail.com' and password == '1234':
        st.success('Welcome back sir !')
    else :
        st.error('Invalid Email or Password !')    