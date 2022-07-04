from tokenize import group
import pandas as pd

df = pd.read_csv('mineriadatos/users_modify.csv')

# seleccionar col para analisis
df = df[['gender', 'role']]

# print(df.head(6))

# agrupar gender y role del dataframe
group = df.groupby(["gender", "role"])
print(group.size().reset_index(name='counts'))
