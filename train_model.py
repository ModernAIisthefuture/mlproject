from joblib import dump
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# Load dataset
df = pd.read_csv("BostonHousing.csv")

X = df.drop("medv", axis=1)
y = df["medv"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# (Optional) Train on entire dataset
model.fit(X, y)

# Save model
dump(model, "model.joblib")

print("Model saved successfully!")

