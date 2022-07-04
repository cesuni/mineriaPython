import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('mineriadatos/usuarios_completo.csv')

df = df[['active', 'gender']]

# print(df.head(6))

pd.crosstab(df['active'], df['gender']).plot(kind='bar')
plt.title('Grafica para cruce de active y gender')
plt.show()
