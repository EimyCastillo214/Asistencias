# prompt: Leer archivo BASE PROGRAMA .csv

import pandas as pd

# Replace 'BASE PROGRAMA.csv' with the actual file path if it's not in the current directory
try:
  df = pd.read_excel('BASE PROGRAMA.csv')
  print(df)
except FileNotFoundError:
  print("Error: 'BASE PROGRAMA.csv' not found. Please check the file path.")
except Exception as e:
  print(f"An error occurred: {e}")
  # prompt: imprimir dataframe usando Streamlit

import streamlit as st
import pandas as pd
