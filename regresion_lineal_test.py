import pickle
import numpy as np

pickled_model = pickle.load(open('medicalcost.pkl', 'rb'))
x_pred = np.array([20.0, 1.0, 20.60, 0.0, 0.0, 4.0]).reshape((-1, 1))
y_pred = pickled_model.predict(x_pred.T)
print('predicted response:  ', y_pred, sep='\n')
