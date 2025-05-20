# prompt: leer archivo BASE DE DATOS.csv

import pandas as pd
excel_file_path = "BASE DE DATOS.xlsx"
df = pd.read_excel(excel_file_path)
print(df.to_string())
