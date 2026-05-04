import streamlit as st
import pandas as pd
import time as t


# Text Utility :

st.title('AYUz')
st.header('Dashboard :')
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

# Displaying Media :

st.image('image.png')

st.video('https://www.youtube.com/watch?v=pO8qyjpkBzM')

# st.audio() we can also use this !


# Creating layouts

st.sidebar.title('Menu SideBar !')

a, b, c= st.columns(3)

with a :
    st.image('image.png')

with b :
    st.image('image.png')    

with c :
    st.image('image.png')  

# showing status :

st.error('Login is failed !')
st.success('login Successful !')
st.info('Mahipal is good girl !')
st.warning('I am good boy !')

# Progess bar :

bar = st.progress(0)

for i in range(1,101):
    t.sleep(0.3)
    bar.progress(i)
    
