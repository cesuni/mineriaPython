import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mineriadatos/titanic.csv')

# Cambiar datos null por un 2 para desconocido
df['Survived'] = df['Survived'].fillna(2)

# Cambiar datos null por S/C en columna cabin
df['Cabin'] = df['Cabin'].fillna('S/C')
print(df.count())

# Cambiar un diccionario con los valores originales por valores
# de reemplazo
d = {'male': 'M', 'female': 'F'}

# Utilizamos un lambda para el reemplazo en una sola linea
df['Sex'] = df['Sex'].apply(lambda x: d[x])

# Obtener los nombres de las columnas en una lista
col_names = df.columns.tolist()

# Cruce de tabla de informacion
ct = pd.crosstab(df['Survived'], df['Sex']).plot(kind='bar')
plt.xlabel("Sobrevivio")
plt.ylabel("Cantidad de sobrevivientes por genero")

for barra in ct.containers:
    ct.bar_label(barra, label_type='edge')

plt.show()
