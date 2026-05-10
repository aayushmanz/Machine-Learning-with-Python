import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='Startup Analysis')

df = pd.read_csv('/workspaces/Machine-Learning-with-Python/StreamLit/startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')

def load_overall_analysis():
    st.title('Overall analysis')
    # total invested amount :
    total = round(df['amount'].sum())
    st.metric('Total', str(total) + ' Cr')

def investor_details(data):
    st.subheader(investor)
    investor_data = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.write('Last 5 investments : ')
    st.dataframe(investor_data)
    
    col1, col2 = st.columns(2)
    with col1 :
         big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
         st.subheader('Biggest investments : ')
         fig, ax = plt.subplots()
         ax.bar(big_series.index,big_series.values)
         st.pyplot(fig)

    with col2 :
         vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
         st.subheader('Sectors invested : ')
         fig1, ax1 = plt.subplots()
         ax1.pie(vertical_series, labels=vertical_series.index, autopct='%0.01f' )
         st.pyplot(fig1)

    col3, col4 = st.columns(2)
    with col3:
        round_series = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()  
        st.subheader('Round investments : ')
        fig2, ax2 = plt.subplots()
        ax2.pie(round_series, labels=round_series.index, autopct='%0.01f' )
        st.pyplot(fig2)
    
    with col4:
        city_series = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
        st.subheader('Cities investments : ')
        fig3, ax3 = plt.subplots()
        ax3.bar(city_series.index,city_series.values)
        st.pyplot(fig3)
    
    df['year'] = df['date'].dt.year
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()   
    st.subheader('YoY investments : ')
    fig4, ax4 = plt.subplots()
    ax4.plot(year_series.index,year_series.values)
    st.pyplot(fig4)



          


st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select one', ['Overall Anaysis', 'Startup', 'Investor'])

if option == 'Overall Anaysis':
    
    btn0 = st.sidebar.button('Show overall Analysis')
    if btn0 :
        load_overall_analysis()
        
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
        

     