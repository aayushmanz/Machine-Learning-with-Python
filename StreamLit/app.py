import streamlit as st
import pandas as pd

df = pd.read_csv('/workspaces/Machine-Learning-with-Python/StreamLit/startup_funding.csv')

st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select one', ['Overall Anaysis', 'Startup', 'Investor'])

if option == 'Overall Anaysis':
    st.title('Overall Anaysis')
elif option == 'Startup':
    st.sidebar.selectbox('Select startup',['Byjus','Ola','Flipkart'])
    st.title('StartUp Analysis')
else:
     st.sidebar.selectbox('Select startup',['Amir aadmi 1','Amir aadmi 2',' Amir aadmi 3'])
     st.title('Investor Analysis')
