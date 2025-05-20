# prompt: leer en archivo BASE DE DATOS.csv

import pandas as pd

df = pd.read_csv('BASE DE DATOS.csv')

print(df.head())
