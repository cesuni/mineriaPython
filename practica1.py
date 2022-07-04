import pandas as pd

# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/users_data2.csv')

# Muestra las primeras 5 filas
# print(df.head())

# Muestra la dimencion de el dataset/dataframe
# print(df.shape)

# Tipos de datos que recibe la columna
# print(df.dtypes)

# Muestra datos null, columnas, tipo de datos
# print(df.info())

# Describir dataframe
# print(df.describe())

# Mustra las columnas con el numero de sus datos y los elementos faltantes
# print(df.count())

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

# llenar columna faltante: avatar gender lenguage
df['avatar'] = df['avatar'].fillna('default.png')

df['gender'] = df['gender'].fillna('D')

df['lenguage'] = df['lenguage'].fillna('Desconocido')

# genera un nuevo csv con las modificaciones
df.to_csv('mineriadatos/users_modify.csv', index=False)

# excel viewer
