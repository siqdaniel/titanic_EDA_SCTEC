# Questoes Levantadas Para Analise: 

# Qual foi a taxa geral de sobrevivência?

# Sexo influenciou a sobrevivência?

# Classe social influenciou a sobrevivência?

# Idade influenciou a sobrevivência?

# Objetivo:

Compreender o comportamento geral dos dados e identificar padrões associados à sobrevivência dos passageiros do Titanic.

Tratamento de Dados

Foram removidas colunas irrelevantes (Cabin, Name, Ticket, PassengerId). Valores nulos em Embarked foram preenchidos pela moda. Idades ausentes foram imputadas pela mediana segmentada por Classe e Sexo. Criou-se a variável AgeGroup para análise categórica.

Análises Realizadas

Calculou-se a taxa geral de sobrevivência (~38%). Foram avaliadas relações entre Survived e Sexo, Classe e Idade. Utilizaram-se agrupamentos (groupby), filtros e visualizações (barplots e histograma).

Principais Insights

Mulheres apresentaram taxa significativamente maior de sobrevivência. Passageiros da 1ª classe tiveram maior probabilidade de sobreviver. Crianças demonstraram maior taxa relativa em comparação a adultos e idosos.

Conclusão

Os resultados indicam forte influência de fatores sociais (sexo e classe) na sobrevivência, sugerindo priorização estrutural durante a evacuação.

## Repositório

Este projeto está versionado utilizando Git e pode ser acessado em:
https://github.com/siqdaniel/titanic_EDA_SCTEC

