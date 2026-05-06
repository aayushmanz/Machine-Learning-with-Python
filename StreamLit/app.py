import streamlit as st
import pandas as pd

df = pd.read_csv('/workspaces/Machine-Learning-with-Python/StreamLit/startup_cleaned.csv')

def investor_details(data):
    st.subheader(investor)
    investor_data = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.write('Last 5 investments : ')
    st.dataframe(investor_data)


st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select one', ['Overall Anaysis', 'Startup', 'Investor'])

if option == 'Overall Anaysis':
    st.title('Overall Anaysis')
elif option == 'Startup':
    st.sidebar.selectbox('Select startup',sorted(df['startup'].unique().tolist()))
    st.title('StartUp Analysis')
    btn1 = st.sidebar.button('Find StartUps Details')
else:
     investor = st.sidebar.selectbox('Select startup',sorted(set(df['investors'].str.split(',').sum())))
     st.title('Investor Analysis')
     btn2 = st.sidebar.button('Find Invester Details')
     if btn2:
        investor_details(investor)
        

     