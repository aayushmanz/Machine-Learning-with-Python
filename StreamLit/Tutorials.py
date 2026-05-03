import streamlit as st
import pandas as pd


# Text Utility :

st.title('Startup Dashboard')
st.header('I am CEO')
st.subheader('my company is the best in the world !')


st.write('This is my normal text for you !')
st.markdown("""
### My Fav Anime :
- DBZ
- Demon Slayer
- Vinland saga
""")

st.code("""
def number(input):
    return number**2

a = number(12)    
""")

st.latex('(a + b)^2 = (a - b) (a + b)')


# Display Elements :

data = pd.DataFrame({
    'name' : ['Ayush', 'Ankit', 'Ajay'],
    'marks' : [50,60,90],
    'package' : [90, 50, 40]
})

st.dataframe(data)

st.metric('Revenue', 'Rs 3L', '3%')

st.json({
    'name' : ['Ayush', 'Ankit', 'Ajay'],
    'marks' : [50,60,90],
    'package' : [90, 50, 40]
})
