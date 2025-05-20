# prompt: Leer archivo Salidafinal.csv

import pandas as pd

# Replace 'Salidafinal.csv' with the actual file path if it's not in the current directory
try:
  df = pd.read_excel('Salidafinal.csv')
  print(df)
except FileNotFoundError:
  print("Error: 'Salidafinal.csv' not found. Please check the file path.")
except Exception as e:
  print(f"An error occurred: {e}")
  # prompt: imprimir dataframe usando Streamlit

import streamlit as st
import pandas as pd
