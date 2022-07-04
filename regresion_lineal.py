from copyreg import pickle
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('mineriadatos/insurance.csv')
# print('dataframe')
# print(df)

# print(df.shape)
# print(df.info)
# print(df.describe)

d = {'female': 1, 'male': 0}
df['sex'] = df['sex'].apply(lambda x: d[x])
print(df)

d = {'yes': 1, 'no': 0}
df['smoker'] = df['smoker'].apply(lambda x: d[x])
print(df)

d = {'southwest': 1, 'northwest': 2, 'southeast': 3, 'northeast': 4}
df['region'] = df['region'].apply(lambda x: d[x])
print(df)

df1 = df[['region', 'sex', 'changes']]
# create cruze de tablas entre coñumnas y filas
ct = pd.crosstab([df1['sex']], df1['region']).plot(kind)


all_cols = df.to_numpy()
y = all_cols[:, 6]
y = np.array(y)
print('y = ', y)

x = all_cols[:, 0:6]
x = np.array(x)
print('x = ')
print(x)

plt.scatter(x[:, 0], y)
plt.show()


# Definition of model

model = LinearRegression()
model.fit(x, y)

LinearRegression()

# Analizar el modelo
r_sq = model.score(x, y)
print()
print()

print('coefficient of determination: ', r_sq)

print()
print()
print('--------- Result to model math of regretion ----------')
print()
print()
print('intercept (b):', model.intercept_)
print('slope(s):', model.coef_)
print()


#  Model Evaluation
#
# add datos para respuesta de medicion
#
#           age    sex     BMI    Children smoker  region
# x_pred = [21],    1,    30.60,     1,      2,      1]

print()
print()
print('Insertar los valores de las variables independietes -x- medidas para predecir')
print('la variable de independietne -charges-')
print()
print()
x_pred = np.array([20.0, 1.0, 20.60, 0.0, 0.0, 4.0]).reshape((-1, 1))
print(x_pred.T)
print()

y_pred = model.predict(x_pred.T)
print('predicated response: ', y_pred, sep='\n')

# Save the model
open('medicalcosts.pkl', 'wb')
pickle.dump(model, open('medicalcosts.pkl', 'wb'))
