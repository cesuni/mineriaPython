import pandas as pd

df = pd.read_csv('mineriadatos/users_modify.csv')

print(df.head(15))

# obtener los nombres de las columnas en una lista
col_names = df.columns.to_list()
# print(col_names)
for column in col_names:
    # conocer los valores nulos
    print("valores nulos en <" + column +
          ">: " + str(df[column].isnull().sum()))
    # conocer tipo de dato por columna
    print("tipo de valor de <" + column + " >: " + str(df[column].dtypes))

# Quitar los datos duplicados manteniendo el ultimo
df = df.drop_duplicates(keep='last', subset=['first_name'])

print(df.duplicated().sum())
print(df.shape)
df.to_csv('mineriadatos/users_modify.csv', index=False)
