import streamlit as st
import pandas as pd

st.title("Streamlit Data Display Example")
st.write("Welcome to Streamlit") 

df =pd.DataFrame({
    'Column A': [1, 2, 3, 4],
    'Column B': ['A', 'B', 'C', 'D']
})

st.write(df)