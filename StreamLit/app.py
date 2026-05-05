import streamlit as st
import pandas as pd

df = pd.read_csv('/workspaces/Machine-Learning-with-Python/StreamLit/startup_funding.csv')

st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select one', ['Overall Anaysis', 'Startup', 'Investor'])

if option == 'Overall Anaysis':
    st.title('Overall Anaysis')
elif option == 'Startup':
    st.sidebar.selectbox('Select startup',sorted(df['Startup Name'].unique().tolist()))
    st.title('StartUp Analysis')
    btn1 = st.sidebar.button('Find StartUps Details')
else:
     st.sidebar.selectbox('Select startup',sorted(df['Investors Name'].fillna('Unknown').unique().tolist()))
     st.title('Investor Analysis')
     btn1 = st.sidebar.button('Find Invester Details')