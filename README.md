
# Credit Card Fraud Detection API

This repository contains a complete implementation of a Credit Card Fraud Detection system powered by a Machine Learning model and deployed using Serverless architecture.

---

## 📘 Project Summary

This project aims to demonstrate the deployment of a machine learning classification model as an API that detects fraudulent credit card transactions. It uses anonymized transaction data to train a model and exposes a REST API for real-time fraud detection.

---

## 🌐 Live API

The API is deployed using **Netlify Functions** and allows users to perform fraud predictions through simple HTTP requests.

- `GET /` - Base endpoint returns a welcome message.
- `POST /predict` - Accepts transaction data and returns a prediction along with model confidence.

---

## 🔧 Technologies Used

- **Python 3.10+**
- **scikit-learn** - For model training
- **pandas & numpy** - Data manipulation and analysis
- **joblib** - Model serialization
- **Netlify Functions** - Serverless API deployment
- **FastAPI or Flask (if local testing is required)**

---

## 🏗️ Folder Structure

```
├── netlify.toml
├── my_functions/
│   ├── fraud_detector.py
│   ├── fraud_model.joblib
│   └── scaler.joblib
└── public/
    └── .gitkeep
```

---

## 🧠 Machine Learning Model

The model is trained using a dataset that includes anonymized features (V1-V28), `Time`, and `Amount`. The target variable is `Class` where:

- `0` = Legitimate Transaction
- `1` = Fraudulent Transaction

### Preprocessing Includes:

- Normalization using `StandardScaler`
- Feature extraction and cleaning
- Model training using Logistic Regression, Random Forest, or an ensemble

### Sample Input Format

```json
{
  "Time": 472.0,
  "V1": -1.359807134,
  "V2": -0.072781173,
  ...
  "V28": 0.021879,
  "Amount": 149.62
}
```

### Sample Output

```json
{
  "result": "Fraudulent",
  "confidence": 91.57
}
```

---

## 🚀 Deployment Guide

### Step 1: Train Your Model

Use your local environment to train the model using Jupyter or Python. Save the final model and scaler using `joblib.dump`.

### Step 2: Prepare Your API Script

Write your handler (`fraud_detector.py`) using Netlify function format.

### Step 3: Setup Netlify

- Connect your GitHub repo to Netlify
- Ensure `netlify.toml` is configured properly:
```toml
[build]
  functions = "my_functions"
  publish = "public"
```

### Step 4: Deploy

Push your code and let Netlify handle deployment automatically. The API will be live in seconds.

---

## 🖼️ Screenshots
<img width="1920" height="930" alt="ccfd1" src="https://github.com/user-attachments/assets/eb64b76f-3f8d-41c3-8c78-910ca18b5fe5" />

<img width="1920" height="930" alt="ccfd3" src="https://github.com/user-attachments/assets/476cc138-5a27-42c7-a9e6-e0affdbcef97" />

<img width="1920" height="928" alt="ccfd2" src="https://github.com/user-attachments/assets/18a21777-83fa-4092-81e0-6703533b9e56" />

---

## 📌 Use Cases

- Real-time fraud detection system
- Backend component of financial dashboards
- Educational tool for demonstrating ML deployment
- API integration with mobile or web apps

---

## 📄 License

This project is licensed under the MIT License. You are free to use, modify, and distribute it.

---

## 🙋 Contact

If you have any questions or suggestions, feel free to open an issue or contact the repository owner.

---

