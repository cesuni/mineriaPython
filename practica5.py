import pandas as pd

df = pd.read_csv('mineriadatos/usuarios_completo.csv')
df = df[['company', 'car']]
group = df.groupby(["company", "car"])
print(group.size().reset_index(name='counts'))

########################################################

df = pd.read_csv('mineriadatos/usuarios_completo.csv')
df = df[['is_admin', 'active']]
group = df.groupby(["is_admin", "active"])
print(group.size().reset_index(name='counts'))
