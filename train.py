import os
import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

df = pd.read_csv("data/churn.csv")

encoders = {}

categorical_columns = [
    "Gender",
    "Subscription Type",
    "Contract Length"
]

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le
# Features
X = df.drop("Churn", axis=1)

# Target
y = df["Churn"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy :", accuracy_score(y_test, pred))

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/model.pkl")
joblib.dump(encoders, "models/encoders.pkl")

print("Model Saved Successfully")