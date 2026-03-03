import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#Load dos Dados
df = pd.read_csv("data/raw/titanic_dataset.csv")

#Analise Geral do Data frame
print(df.head())
print (df.info())
print (df.isnull().sum())






