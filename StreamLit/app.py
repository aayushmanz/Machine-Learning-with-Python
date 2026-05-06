import streamlit as st
import pandas as pd

df = pd.read_csv('/workspaces/Machine-Learning-with-Python/StreamLit/startup_cleaned.csv')

st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select one', ['Overall Anaysis', 'Startup', 'Investor'])

if option == 'Overall Anaysis':
    st.title('Overall Anaysis')
elif option == 'Startup':
    st.sidebar.selectbox('Select startup',sorted(df['startup'].unique().tolist()))
    st.title('StartUp Analysis')
    btn1 = st.sidebar.button('Find StartUps Details')
else:
     st.sidebar.selectbox('Select startup',set(df['investors'].str.split(',').sum()))
     st.title('Investor Analysis')
     btn1 = st.sidebar.button('Find Invester Details')
     