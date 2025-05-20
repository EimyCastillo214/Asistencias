# prompt: leer archivo BASE DE DATOS.csv

import pandas as pd
excel_file_path = "BASE DE DATOS.xlsx"
df = pd.read_excel(excel_file_path)
print(df.to_string())

# prompt: usando streamlit muestrame las columnas del archivo BASE DE DATOS.csv

import streamlit as st
import pandas as pd

excel_file_path = "BASE DE DATOS.xlsx"
df = pd.read_excel(excel_file_path)

st.write("Las columnas del archivo BASE DE DATOS.xlsx son:")
st.write(df.columns.tolist())
