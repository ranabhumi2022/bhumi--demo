import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset (Experience, Hours studied → Salary)
X = np.array([
    [1, 2],
    [2, 3],
    [3, 5],
    [4, 6],
    [5, 8]
])

y = np.array([20, 30, 50, 65, 80])

# Model
model = LinearRegression()

# Train
model.fit(X, y)

# Predict
prediction = model.predict([[6, 9]])

print("Prediction:", prediction)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
'''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# ── 1. Sample Data ─────────────────────────────────────────────────────────────
np.random.seed(42)
n = 200

X = pd.DataFrame({
    "size_sqft":   np.random.randint(500, 3500, n),
    "bedrooms":    np.random.randint(1, 6, n),
    "age_years":   np.random.randint(0, 50, n),
    "distance_km": np.round(np.random.uniform(1, 30, n), 1),
})

# Target: house price (with some noise)
y = (
    200 * X["size_sqft"]
    + 15000 * X["bedrooms"]
    - 3000 * X["age_years"]
    - 8000 * X["distance_km"]
    + np.random.normal(0, 20000, n)
)

# ── 2. Train / Test Split ───────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ── 3. Scale Features ──────────────────────────────────────────────────────────
scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc  = scaler.transform(X_test)

# ── 4. Train Model ─────────────────────────────────────────────────────────────
model = LinearRegression()
model.fit(X_train_sc, y_train)

# ── 5. Evaluate ────────────────────────────────────────────────────────────────
y_pred = model.predict(X_test_sc)

print("=" * 40)
print("       MODEL COEFFICIENTS")
print("=" * 40)
for feat, coef in zip(X.columns, model.coef_):
    print(f"  {feat:<15} {coef:>12,.2f}")
print(f"  {'Intercept':<15} {model.intercept_:>12,.2f}")

print("\n" + "=" * 40)
print("       PERFORMANCE METRICS")
print("=" * 40)
print(f"  R² Score : {r2_score(y_test, y_pred):.4f}")
print(f"  MSE      : {mean_squared_error(y_test, y_pred):,.2f}")
print(f"  RMSE     : {np.sqrt(mean_squared_error(y_test, y_pred)):,.2f}")

# ── 6. Plots ───────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("Multiple Linear Regression — Diagnostics", fontsize=14, fontweight="bold")

# (a) Actual vs Predicted
axes[0].scatter(y_test, y_pred, alpha=0.6, color="steelblue", edgecolors="white", linewidths=0.4)
lims = [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())]
axes[0].plot(lims, lims, "r--", linewidth=1.5, label="Perfect fit")
axes[0].set_xlabel("Actual")
axes[0].set_ylabel("Predicted")
axes[0].set_title("Actual vs Predicted")
axes[0].legend()

# (b) Residuals vs Predicted
residuals = y_test - y_pred
axes[1].scatter(y_pred, residuals, alpha=0.6, color="orchid", edgecolors="white", linewidths=0.4)
axes[1].axhline(0, color="red", linestyle="--", linewidth=1.5)
axes[1].set_xlabel("Predicted")
axes[1].set_ylabel("Residuals")
axes[1].set_title("Residuals vs Predicted")

# (c) Feature Coefficients (standardized → comparable)
colors = ["tomato" if c < 0 else "steelblue" for c in model.coef_]
axes[2].barh(X.columns, model.coef_, color=colors)
axes[2].axvline(0, color="black", linewidth=0.8)
axes[2].set_xlabel("Coefficient (standardized)")
axes[2].set_title("Feature Importance")

plt.tight_layout()
plt.savefig("multiple_linear_regression.png", dpi=150)
plt.show()

# ── 7. Predict on New Data ────────────────────────────────────────────────────
new_house = pd.DataFrame([{
    "size_sqft":   1800,
    "bedrooms":    3,
    "age_years":   10,
    "distance_km": 5.0,
}])
new_house_sc = scaler.transform(new_house)
predicted_price = model.predict(new_house_sc)[0]
print(f"\n  Predicted price for new house: ₹{predicted_price:,.0f}")'''