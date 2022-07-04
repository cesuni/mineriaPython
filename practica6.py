import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mineriadatos/users_modify.csv')

df = df[['gender', 'role']]

# print(df.head(6))

pd.crosstab(df['gender'], df['role']).plot(kind='bar')
plt.show()
