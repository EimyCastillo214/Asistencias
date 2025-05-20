# prompt: leer en streamlit archivo .xlsx

import streamlit as st
import pandas as pd

st.title("Read .xlsx file in Streamlit")

uploaded_file = st.file_uploader("Upload an .xlsx file", type="xlsx")

if uploaded_file is not None:
  try:
    df = pd.read_excel(uploaded_file)
    st.write("Here's a preview of the data:")
    st.dataframe(df)
  except Exception as e:
    st.error(f"Error reading the file: {e}")
