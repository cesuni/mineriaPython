import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mineriadatos/titanic.csv')

# 2 para desconocido
# df['Survived'] = df['Survived'].fillna(2)

# S/C
#df['Cabin'] = df['Cabin'].fillna('NC')
# print(df.count())

# d = {'male': 'M', 'female': 'F'}

# lamda - reemplazo en una sola linea
# df['Sex'] = df['Sex'].apply(lambda x: d[x])

# Obtener los nombres de las columnas en una lista
# col_names = df.columns.tolist()
#df.to_csv('mineriadatos/titanic.csv', index=False)

# Cruce de tabla de informacion
ct = pd.crosstab(df['Survived'], df['Age']).plot(kind='bar')
plt.xlabel("Sobrevivio")
plt.ylabel("Cantidad de sobrevivientes por cabina")

for barra in ct.containers:
    ct.bar_label(barra, label_type='edge')

plt.show()
