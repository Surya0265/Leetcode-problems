# ML Lab Exercise 06
# Student: Suryaprakash - 23N257

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes, load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.linear_model import Ridge, Lasso, LogisticRegression

# ---------------- Linear Regression using Gradient Descent ---------------- #
def linear_regression_gd(X, y, lr=0.1, n_iter=1000):
    m = len(y)
    theta = np.random.randn(X.shape[1], 1)
    for _ in range(n_iter):
        gradients = (2/m) * X.T.dot(X.dot(theta) - y)
        theta -= lr * gradients
    return theta

# Dataset used: Diabetes dataset (for regression)
reg_data = load_diabetes()
X_reg = reg_data.data
y_reg = reg_data.target.reshape(-1, 1)

# Display sample values
print("--- Diabetes Dataset Sample ---")
print("X_reg (first 5 rows):\n", X_reg[:5])
print("y_reg (first 5 values):\n", y_reg[:5])

scaler = StandardScaler()
X_reg_scaled = scaler.fit_transform(X_reg)
X_reg_bias = np.c_[np.ones((X_reg_scaled.shape[0], 1)), X_reg_scaled]

# Apply Linear Regression
theta_lin = linear_regression_gd(X_reg_bias, y_reg)
print("\nLinear Regression Weights:\n", theta_lin.ravel())

# ---------------- Multiple Linear Regression with Gradient Descent ---------------- #
theta_multi = linear_regression_gd(X_reg_bias, y_reg)
print("\nMultiple Linear Regression Weights:\n", theta_multi.ravel())

# ---------------- Logistic Regression using Gradient Descent ---------------- #
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression_gd(X, y, lr=0.1, n_iter=1000):
    m = len(y)
    theta = np.random.randn(X.shape[1], 1)
    for _ in range(n_iter):
        z = X.dot(theta)
        predictions = sigmoid(z)
        gradients = (1/m) * X.T.dot(predictions - y)
        theta -= lr * gradients
    return theta

# Dataset used: Iris dataset (binary classification: Setosa vs Non-Setosa)
iris = load_iris()
X_class = iris.data[iris.target != 2]
y_class = iris.target[iris.target != 2].reshape(-1, 1)

# Display sample values
print("\n--- Iris Dataset Sample ---")
print("X_class (first 5 rows):\n", X_class[:5])
print("y_class (first 5 values):\n", y_class[:5])

X_train, X_test, y_train, y_test = train_test_split(X_class, y_class, test_size=0.2, random_state=42)

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
X_train_bias = np.c_[np.ones((X_train_scaled.shape[0], 1)), X_train_scaled]
X_test_bias = np.c_[np.ones((X_test_scaled.shape[0], 1)), X_test_scaled]

theta_log = logistic_regression_gd(X_train_bias, y_train)
y_pred_log = sigmoid(X_test_bias.dot(theta_log)) >= 0.5
print("\nLogistic Regression Accuracy:", accuracy_score(y_test, y_pred_log))

# ---------------- Regularized Linear Regression ---------------- #
ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)

ridge.fit(X_reg_scaled, y_reg.ravel())
lasso.fit(X_reg_scaled, y_reg.ravel())

ridge_preds = ridge.predict(X_reg_scaled)
lasso_preds = lasso.predict(X_reg_scaled)

print("\nRidge Regression MSE:", mean_squared_error(y_reg, ridge_preds))
print("Lasso Regression MSE:", mean_squared_error(y_reg, lasso_preds))

# ---------------- Regularized Logistic Regression ---------------- #
log_reg_l1 = LogisticRegression(penalty='l1', solver='liblinear')
log_reg_l2 = LogisticRegression(penalty='l2', solver='liblinear')

log_reg_l1.fit(X_train_scaled, y_train.ravel())
log_reg_l2.fit(X_train_scaled, y_train.ravel())

print("\nRegularized Logistic Regression Accuracy:")
print("L1 (Lasso) Accuracy:", log_reg_l1.score(X_test_scaled, y_test))
print("L2 (Ridge) Accuracy:", log_reg_l2.score(X_test_scaled, y_test))
