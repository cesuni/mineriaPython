import matplotlib.pyplot as plt
from os import kill
import pandas as pd

df = pd.read_csv('mineriadatos/usuarios_completo.csv')

# dimencion
# print(df.shape)

# cabecera
#col_names = df.columns.to_list()
# print(col_names)

# Mustra las columnas con el numero de sus datos y los elementos faltantes
# print(df.count())

# Muestra datos null, columnas, tipo de datos
# print(df.info())

# Conocer si hay datos duplicados
# print(df.duplicated().sum())

# obtener los nombres de las columnas en una lista
col_names = df.columns.to_list()
# print(col_names)

for column in col_names:
    # conocer los valores nulos
    print("valores nulos en <" + column +
          ">: " + str(df[column].isnull().sum()))
    # conocer tipo de dato por columna
    print("tipo de valor de <" + column + " >: " + str(df[column].dtypes))

# llenar columna faltante: gener gender lenguage
df['company'] = df['company'].fillna('indefined')

df['car'] = df['car'].fillna('none')

df['active'] = df['active'].fillna('none')

df['favorite_app'] = df['favorite_app'].fillna('none')

df['avatar'] = df['avatar'].fillna('default.png')

df['active'] = df['active'].fillna('none')

df['is_admin'] = df['is_admin'].fillna('false')

df['department'] = df['department'].fillna('none')

df['gender'] = df['gender'].fillna('I')

# genera un nuevo csv con las modificaciones
df.to_csv('mineriadatos/usuarios_completo.csv', index=False)

df['gender'].value_counts().plot(kind="bar")
plt.show()
