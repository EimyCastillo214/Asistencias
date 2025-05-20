# prompt: leer archivo BASE DE DATOS.xlsx

import pandas as pd

file_path = 'BASE DE DATOS.csv'
df = pd.read_excel(file_path)
print(df.head())
