from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict_customer

app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0"
)


class Customer(BaseModel):
    CustomerID: int
    Age: int
    Gender: str
    Tenure: int
    Usage_Frequency: int
    Support_Calls: int
    Payment_Delay: int
    Subscription_Type: str
    Contract_Length: str
    Total_Spend: float
    Last_Interaction: int


@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API is Running"}


@app.post("/predict")
def predict(customer: Customer):

    data = {
        "CustomerID": customer.CustomerID,
        "Age": customer.Age,
        "Gender": customer.Gender,
        "Tenure": customer.Tenure,
        "Usage Frequency": customer.Usage_Frequency,
        "Support Calls": customer.Support_Calls,
        "Payment Delay": customer.Payment_Delay,
        "Subscription Type": customer.Subscription_Type,
        "Contract Length": customer.Contract_Length,
        "Total Spend": customer.Total_Spend,
        "Last Interaction": customer.Last_Interaction,
    }

    return predict_customer(data)