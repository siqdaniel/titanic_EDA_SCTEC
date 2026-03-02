import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from pathlib import Path


#load dos dados
df = pd.read_csv("data/raw/titanic_dataset.csv")

#Tratamento e Limpeza dos Dados

#Remocao de Colunas com valores nulos excessivos ou sem valor preditivo
df = df.drop(["Cabin", "PassengerId", "Name", "Ticket"], axis=1)
print (df.isnull().sum())

#Substituicao de valor nulos da variavel embarked pela moda:
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
print(df["Embarked"].isnull().sum())


#Tratamento dos nulos da variavel Age pela imputacao da mediana de
#Pclass + sex:

df["Age"] = df.groupby(["Pclass", "Sex"])["Age"].transform(
    lambda x: x.fillna(x.median())
)
df["Age"].isnull().sum()
df["Age"].describe()

#Criacao de AgeGroup para cetagorizar por idade:

def categorizar_idade(idade):
    if idade <= 12:
        return "Crianca"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 59:
        return "Adulto"
    else:
        return "Idoso"

df["AgeGroup"] = df["Age"].apply(categorizar_idade)


# INSIGHTS: 

#Taxa Geral de Sobrevivencia: 
print(  int(df["Survived"].mean() * 100) )

#Hipotese de que mulheres tiveram maior taxa de sobrevivencia:
print(df.groupby("Sex")["Survived"].mean() * 100)

#proporção real dentro do grupo.

print(df.groupby("Sex")["Survived"].value_counts(normalize=True))
