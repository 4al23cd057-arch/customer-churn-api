# Customer Churn Prediction API

A Machine Learning-based REST API that predicts whether a customer is likely to churn using customer demographic and service information. The API is built with **FastAPI**, containerized using **Docker**, and deployed on **Render**.

---

## 📌 Project Overview

Customer churn is one of the biggest challenges faced by subscription-based businesses. This project helps predict whether a customer is likely to leave the service by using a trained Machine Learning model.

The API accepts customer information in JSON format and returns the predicted churn status.

---

## 🚀 Features

- Customer churn prediction
- REST API built with FastAPI
- Interactive Swagger API documentation
- Input validation using Pydantic
- Docker support
- Cloud deployment using Render
- JSON response format

---

## 🛠️ Tech Stack

- Python 3.x
- FastAPI
- Uvicorn
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Docker
- Render

---

## 📂 Project Structure

```
customer-churn-api/
│
├── app.py                 # FastAPI application
├── model.pkl              # Trained Machine Learning model
├── requirements.txt       # Project dependencies
├── Dockerfile             # Docker configuration
├── render.yaml            # Render deployment configuration (if available)
├── README.md              # Project documentation
└── dataset/               # Dataset (optional)
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/4al23cd057-arch/customer-churn-api.git

cd customer-churn-api
```

### Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the API

```bash
uvicorn app:app --reload
```

The API will start at

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📮 Prediction Endpoint

### POST

```
/predict
```

### Sample Request

```json
{
  "CustomerID": 1001,
  "Gender": "Male",
  "Age": 35,
  "Tenure": 24,
  "MonthlyCharges": 79.85,
  "TotalCharges": 1916.4,
  "Contract": "One year",
  "InternetService": "Fiber optic",
  "PaymentMethod": "Electronic check"
}
```

### Sample Response

```json
{
  "prediction": "No Churn"
}
```

---

## 🐳 Docker

### Build Docker Image

```bash
docker build -t customer-churn-api .
```

### Run Docker Container

```bash
docker run -p 8000:8000 customer-churn-api
```

Visit

```
http://localhost:8000/docs
```

---

## ☁️ Deployment

The API is deployed using **Render**.

Deployment Steps:

1. Push the project to GitHub.
2. Connect the repository to Render.
3. Render automatically builds the Docker image.
4. Deploy the API.
5. Access the public endpoint.

---

## 📊 Machine Learning Workflow

```
Dataset
    │
    ▼
Data Preprocessing
    │
    ▼
Feature Engineering
    │
    ▼
Model Training
    │
    ▼
Model Serialization (Joblib)
    │
    ▼
FastAPI REST API
    │
    ▼
Docker Container
    │
    ▼
Render Deployment
```

---

## 📈 Future Improvements

- Web-based user interface
- Batch prediction using CSV upload
- Authentication and authorization
- Prediction probability score
- Model retraining pipeline
- CI/CD using GitHub Actions

---

## 👩‍💻 Author

**Usha J T**

B.E. Computer Science & Engineering (Data Science)

Alva's Institute of Technology

---

## 📄 License

This project is developed for educational and academic purposes.
