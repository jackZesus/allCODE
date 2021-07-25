import numpy as np
import matplotlib as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

data = datasets.load_diabetes()  # data set load
# (['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])
# print(data.DESCR)
data_x = data.data[:,   np.newaxis, 2]  # axix index no 2 with in a array
data_x_Train = data_x[:-20]  # last 20
data_x_test = data_x[-20:]

data_y_Train = data.target[:-20]
data_y_test = data.target[-20:]

model = linear_model.LinearRegression()
model.fit(data_x_Train, data_y_Train)

data_y_predicted = model.predict(data_y_test)


print("mean sqaure error is : ", mean_squared_error(data_y_test, data_y_predicted
