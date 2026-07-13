import mlflow
import mlflow.sklearn
import joblib

# Load model
model = joblib.load("models/model.pkl")

# Start MLflow run
with mlflow.start_run():

    # Log model
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="customer_churn_model",
        registered_model_name="CustomerChurnModel"
    )

    print("Model registered successfully!")