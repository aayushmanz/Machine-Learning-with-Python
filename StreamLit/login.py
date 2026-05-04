import streamlit as st

st.subheader('Log In : ')
email = st.text_input('Enter Your Email')
password = st.text_input('Enter your password')
gender = st.selectbox('Select gender', ['male', 'female', 'others'])

btn = st.button('Click here !')

# if the btn is clicked !
if btn:
    if email == 'ayushsuthar@gmail.com' and password == '1234':
        st.success('Welcome back sir !')
        st.balloons()
        st.write(gender)
        
    else :
        st.error('Invalid Email or Password !')   
        