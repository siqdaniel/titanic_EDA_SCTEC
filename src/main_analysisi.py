import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 




#load dos dados
df = pd.read_csv("data/raw/titanic_dataset.csv")

#Tratamento e Limpeza dos Dados

#Remocao de Colunas com valores nulos excessivos ou sem valor preditivo
df = df.drop(["Cabin", "PassengerId", "Name", "Ticket"], axis=1)
df.isnull().sum()

#Substituicao de valor nulos da variavel embarked pela moda:
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Embarked"].isnull().sum()


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
(int(df["Survived"].mean() * 100) )

#Hipotese de que mulheres tiveram maior taxa de sobrevivencia:
survival_by_sex = (df.groupby("Sex")["Survived"].mean() * 100)

#proporção real dentro do grupo.

(df.groupby("Sex")["Survived"].value_counts(normalize=True)) #Nao Implementado

# Hipotese de que passageiros da primeira classe tiveram maior chance de sobrevivencia:
survival_by_class = (df.groupby("Pclass")["Survived"].mean() *100)

# Analise da taxa de sobrevivencia por idade:
(df.groupby("AgeGroup")["Survived"].mean() * 100)

#Analise da taxa de sobrevivencia pela tarifa de embarque: 
(df.groupby("Survived")["Fare"].mean())


# VISUALIZACOES GRAFICAS:

# SOBREVIVENCIA POR SEXO:

sns.barplot(
    x=survival_by_sex.index,
    y=survival_by_sex.values
)

plt.ylabel("Taxa de Sobrevivência (%)")
plt.title("Taxa de Sobrevivência por Sexo")
plt.savefig("outputs/figures/survival_by_sex.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# SOBREVIVENCIA POR CLASSE:

sns.barplot(
    x=survival_by_class.index,
    y=survival_by_class.values
)

plt.ylabel("Taxa de Sobrevivência (%)")
plt.title("Taxa de Sobrevivência por Classe")
plt.savefig("outputs/figures/survival_by_class.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()


# Histograma comparativo:
fig, ax = plt.subplots(figsize=(8,5))

sns.histplot(data=df, x="Age", hue="Survived", kde=True, bins=30, ax=ax)

ax.set_title("Distribuição de Idade por Sobrevivência")

fig.tight_layout()
fig.savefig("outputs/figures/idade_por_sobrevivencia.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close(fig)


