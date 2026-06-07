import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 1: Dataset (Hours vs Marks)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)   # independent variable
y = np.array([20, 40, 50, 70, 90])             # dependent variable

# Step 2: Create model
model = LinearRegression()

# Step 3: Train model
model.fit(X, y)

# Step 4: Predict
y_pred = model.predict(X)

# Step 5: Output results
print("Slope (m):", model.coef_)
print("Intercept (b):", model.intercept_)

# Step 6: Plot graph
plt.scatter(X, y)          # actual data
plt.plot(X, y_pred)        # regression line
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Simple Linear Regression")
plt.show()