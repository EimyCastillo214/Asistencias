# prompt: Leer el archivo BASE PROGRAMA.csv ubicado en la carpeta MyDrive de la carpeta drive

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

# Try reading with latin-1 encoding
try:
    df = pd.read_csv('/content/drive/MyDrive/BASE PROGRAMA.csv', encoding='latin-1')
except UnicodeDecodeError:
    # If latin-1 fails, try cp1252 encoding
    df = pd.read_csv('/content/drive/MyDrive/BASE PROGRAMA.csv', encoding='cp1252')
