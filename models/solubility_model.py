import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score
import pickle


dataset = pd.read_csv(r'..\data\delaney_solubility_with_descriptors.csv')
print(dataset)
X = dataset.drop(['logS'], axis = 1)
Y = dataset.iloc[:,-1]

### Linear Regression Model
model = LinearRegression()
model.fit(X,Y)
###
y_pred = model.predict(X)

print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)
print('Mean squared error (MSE): %.2f'
      % mean_squared_error(Y, y_pred))
print('Coefficient of determination (R^2): %.2f'
      % r2_score(Y, y_pred))

pickle.dump(model , open('solubility_model.pkl' , 'wb'))