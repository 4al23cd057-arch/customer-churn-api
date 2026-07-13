import joblib

encoders = joblib.load("models/encoders.pkl")

for col, encoder in encoders.items():
    print(col)
    print(encoder.classes_)
    print("----------------")