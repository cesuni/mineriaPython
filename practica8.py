from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mineriadatos/titanic.csv')

# connect veryfication
# print(df.head(6))

# --dataset--
# print(df.shape)
# print(df.duplicated().sum())
# print(df.info)
# print(df.describe)
# print(df.count())

df['Survived'] = df['Survived'].fillna(2)
df['Cabin'] = df['Cabin'].fillna('S\C')
# print(df.count())

d = {'male': 'M', 'female': 'F'}
df['Sex'] = df['Sex'].apply(lambda x: d[x])

# for x in df['Sex']:
#   df['Sex'] = df['Sex']

print(df['Sex'])

col_names = df.columns.to_list()

# for column in col_names:
#    print("Valores nulos en <" + column + ">: " + str(df[column].isnull))

ct = pd.crosstab(df['Survived'], df['Sex']).plot(kind='bar')
plt.xlabel("Sobrevivio")
plt.ylabel("Cantidad de sobrevivientes")

for barra in ct.containers:
    ct.bar_label(barra, label_type="edge")

plt.show()
