
import streamlit as st
import pandas as pd

file = st.file_uploader('Upload CSV file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())
    