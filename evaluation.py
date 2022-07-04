# i m p o r t a c i o n e s
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mineriadatos/train.csv')

# consulta dataset
# print(df.head())

# dimencion del dataset
# print(df.shape)

# Tipos de datos que recibe la columna
# print(df.dtypes)

# Muestra datos null, columnas, tipo de datos
# print(df.info())

# Describir dataframe
# print(df.describe())

# registros por columna
# print(df.count())

# datos duplicados
# print(df.duplicated().sum())

# llenado de campos nulos
# df['Age'] = df['Age'].fillna('unknown')
# df['Cabin'] = df['Cabin'].fillna('S/C')

# realizacion de cambios en el csv
# df.to_csv('mineriadatos/train.csv', index=False)

# Cruce de tabla de informacion
# ct = pd.crosstab(df['Survived'], df['Embarked']).plot(kind='bar')
# vplt.xlabel("Sobrevivio")
#vplt.ylabel("Cantidad de sobrevivientes por clase")

# for barra in ct.containers:
#    ct.bar_label(barra, label_type='edge')

# plt.show()
