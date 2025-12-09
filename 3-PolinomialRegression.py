import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score


df = pd.read_csv("3-customersatisfaction.csv")
print(df.head())
print(df.info())
df=df.drop("Unnamed: 0",axis=1)

plt.scatter(df["Customer Satisfaction"],df["Incentive"],color="red")
plt.xlabel("Customer Satisfaction")
plt.ylabel("Incentive")
plt.show()

X_train,X_test,y_train,y_test=train_test_split(df[["Customer Satisfaction"]],df["Incentive"],test_size=0.3,random_state=20)

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

regression=LinearRegression()
regression.fit(X_train,y_train)

y_predicted=regression.predict(X_test)
score=r2_score(y_test,y_predicted)
print("\nR2-score:",score)

plt.scatter(X_train,y_train,color="green")
plt.plot(X_train,regression.predict(X_train),color="blue")
plt.show()



poly=PolynomialFeatures(degree=2) #for polynomial regression
X_train_poly=poly.fit_transform(X_train)
X_test_poly=poly.transform(X_test)
print(X_train_poly)
print(X_test_poly)

regression=LinearRegression()
regression.fit(X_train_poly,y_train)
y_predicted=regression.predict(X_test_poly)
score=r2_score(y_test,y_predicted)
print("Score:",score)

print("coefficients:",regression.coef_)
print("intercept:",regression.intercept_)
plt.scatter(X_train,y_train,color="green")
plt.scatter(X_train,regression.predict(X_train_poly),color="blue")
plt.show()


poly=PolynomialFeatures(degree=3,include_bias=True)
X_train_poly=poly.fit_transform(X_train)
X_test_poly=poly.transform(X_test)

regression=LinearRegression()
regression.fit(X_train_poly,y_train)

y_predicted=regression.predict(X_test_poly)
score=r2_score(y_test,y_predicted)
print("Score:",score)

print("coefficients:",regression.coef_)
print("intercept:",regression.intercept_)
plt.scatter(X_train,y_train,color="green")
plt.scatter(X_train,regression.predict(X_train_poly),color="blue")
plt.show()