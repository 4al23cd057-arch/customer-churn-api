import joblib

model = joblib.load("models/model.pkl")

print("Model type:", type(model))

if hasattr(model, "feature_names_in_"):
    print("Expected features:")
    print(model.feature_names_in_)
else:
    print("Model does not store feature names")