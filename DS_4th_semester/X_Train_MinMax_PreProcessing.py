from sklearn import preprocessing
import numpy as np
x_train = np.array([[1.,-1.,2.],[2.,0.,0.],[0.,1.,-1.]])
min_max_scaler = preprocessing.MinMaxScaler()
x_train_minmax=min_max_scaler.fit_transform(x_train)
print(x_train_minmax)