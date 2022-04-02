import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
import pandas as pd

# Load the diabetes dataset
boston = datasets.load_boston()

bos = pd.DataFrame(boston.data, columns=boston.feature_names)
bos['target'] = boston.target

print(bos.head(7))

X = bos.drop('target', axis=1)
Y = bos['target']

print(bos.describe())

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33, random_state = 5)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

lm = LinearRegression()
lm.fit(X_train, Y_train)

Y_pred = lm.predict(X_test)

# Plot outputs
# plt.scatter(X_test, Y_test,  color='black')
# plt.plot(X_test, Y_pred, color='blue', linewidth=3)

plt.scatter(Y_test, Y_pred)
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Prices vs Predicted prices: $Y_i$ vs $\hat{Y}_i$")
plt.show()
mse = mean_squared_error(Y_test, Y_pred)
print(mse)


