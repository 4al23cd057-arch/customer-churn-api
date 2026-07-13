import joblib
import pandas as pd

model = joblib.load("models/model.pkl")
encoders = joblib.load("models/encoders.pkl")


def predict_customer(data):
    df = pd.DataFrame([data])

    print("Before encoding:")
    print(df)
    print(df.columns)

    for col, encoder in encoders.items():
        if col in df.columns:
            df[col] = encoder.transform(df[col].astype(str))

    print("After encoding:")
    print(df)
    print(df.columns)

    print("Model expects:")
    print(model.feature_names_in_)

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0]

    return {
        "prediction": int(prediction),
        "churn": "Yes" if prediction == 1 else "No",
        "confidence": round(float(max(probability)), 4)
    }