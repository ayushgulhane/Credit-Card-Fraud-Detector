🕵️ Credit Card Fraud Detection API
Project Overview
This repository hosts a machine learning model designed for real-time credit card fraud detection. It exposes a Flask-based API endpoint, deployed as a Netlify Serverless Function, that can predict whether a given transaction is legitimate or fraudulent based on various transaction features.

The model is trained on a dataset of credit card transactions, using various anonymized features (V1-V28), transaction Time, and Amount. It aims to help financial institutions and payment gateways identify and prevent fraudulent activities efficiently.
<img src="https://placehold.co/600x200/cccccc/333333?text=Credit+Card+Fraud+Detection" alt="Credit Card Fraud Detection Illustration" width="600"/>

Features
Real-time Prediction: Quickly predicts the likelihood of fraud for new transactions via a REST API.

Machine Learning Model: Utilizes a pre-trained scikit-learn model (e.g., Logistic Regression, Random Forest, or a custom ensemble) for classification.

Data Preprocessing: Incorporates necessary data scaling for Time and Amount features, consistent with the training pipeline.

Serverless Deployment: Deployed as a Netlify Function for scalability, cost-efficiency, and ease of maintenance.

CORS Enabled: Allows secure cross-origin requests from frontend applications.

API Endpoints
The API is deployed on Netlify Functions. Once deployed, you will get a base URL.
The primary prediction endpoint is:

GET /: A simple endpoint to check if the API is running.

Response: Fraud Detector API is running! Send POST requests to /predict for predictions.

POST /predict: Accepts transaction data and returns a fraud prediction.

Method: POST

Content-Type: application/json

Request Body Example:

{
  "time": 12345,
  "amount": 50.75,
  "v1": 0.1, "v2": 0.2, "v3": 0.3, "v4": 0.4, "v5": 0.5, "v6": 0.6, "v7": 0.7, "v8": 0.8, "v9": 0.9, "v10": 1.0,
  "v11": 1.1, "v12": 1.2, "v13": 1.3, "v14": 1.4, "v15": 1.5, "v16": 1.6, "v17": 1.7, "v18": 1.8, "v19": 1.9, "v20": 2.0,
  "v21": 2.1, "v22": 2.2, "v23": 2.3, "v24": 2.4, "v25": 2.5, "v26": 2.6, "v27": 2.7, "v28": 2.8
}

Note: All v features (v1 to v28) are mandatory.

Response Body Example:

{
  "result": "Legitimate",
  "confidence": 99.85
}

or

{
  "result": "Fraudulent",
  "confidence": 75.12
}

Error Responses:

400 Bad Request: If required data fields are missing or data format is incorrect.

500 Internal Server Error: If the model or scaler files could not be loaded on the server.

Deployment on Netlify
This project is configured for seamless deployment on Netlify Functions.

Project Structure
your-fraud-detection-project/
├── netlify.toml
├── requirements.txt
├── my_functions/             # Contains your function code and model artifacts
│   ├── fraud_detector.py     # The Flask application acting as the serverless function
│   ├── fraud_model.joblib    # Your trained machine learning model
│   └── scaler.joblib         # Your trained scaler for preprocessing
└── public/                   # Dummy directory required by Netlify for publishing
    └── .gitkeep              # (Optional: ensures 'public' folder is committed to Git)

<img src="https://placehold.co/600x200/cccccc/333333?text=Netlify+Deployment+Architecture" alt="Netlify Deployment Architecture Diagram" width="600"/>

netlify.toml Configuration
The netlify.toml file configures the build and deployment settings for Netlify:

[build]
  publish = "public" # Points to the dummy public directory
  command = "echo 'No build command needed for static files'" # No frontend build

[functions]
  directory = "my_functions" # Specifies the directory where your Python function is
  node_bundler = "esbuild" # Optional: for faster JS builds, but fine for Python
  # python_version = "3.9" # Uncomment if you need a specific Python version

Steps to Deploy
Clone the Repository:

git clone https://github.com/ayushgulhane/Credit-Card-Fraud-Detector.git
cd Credit-Card-Fraud-Detector

Ensure Model & Scaler Files: Make sure your trained fraud_model.joblib and scaler.joblib files are placed inside the my_functions/ directory.

Create Dummy public Directory: If you haven't already, create an empty public directory at the root of your project:

mkdir public
touch public/.gitkeep # Optional: to ensure it's tracked by Git

Commit and Push: Commit all your changes and push them to your GitHub repository.

Connect to Netlify:

Go to Netlify and log in.

Click "Add new site" -> "Import an existing project".

Connect your Git provider (GitHub, GitLab, etc.) and select this repository.

Netlify will automatically detect your netlify.toml settings. Confirm the build command (echo 'No build command needed for static files') and publish directory (public). Ensure the functions directory is set to my_functions.

Click "Deploy site".

Netlify will then build and deploy your Flask API as a serverless function. You can find the function's URL under the "Functions" tab in your Netlify dashboard.
<img src="https://placehold.co/600x200/cccccc/333333?text=Netlify+Dashboard+Logs" alt="Netlify Dashboard Logs Screenshot" width="600"/>

Local Development & Testing
To run the Flask API locally for development and testing:

Create a Virtual Environment (recommended):

python -m venv venv
source venv/bin/activate # On Windows: .\venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

Ensure Model & Scaler: Place your fraud_model.joblib and scaler.joblib files directly in the same directory as fraud_detector.py (i.e., my_functions/).

Run the Flask App: Navigate into the my_functions directory and run the Flask application directly.

cd my_functions
export FLASK_APP=fraud_detector.py
flask run

The API will usually be available at http://127.0.0.1:5000/.

Screenshots
Here are some screenshots of the Credit Card Fraud Detector UI, demonstrating the input fields and prediction output:

Initial Input
<img src="http://googleusercontent.com/file_content/3" alt="Credit Card Fraud Detector UI - Initial Input" width="600"/>

Transaction Details Input
<img src="http://googleusercontent.com/file_content/2" alt="Credit Card Fraud Detector UI - Transaction Details" width="600"/>

Legitimate Transaction Prediction
<img src="http://googleusercontent.com/file_content/1" alt="Credit Card Fraud Detector UI - Legitimate Prediction" width="600"/>

Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Future Enhancements
This project provides a solid foundation for credit card fraud detection. Here are some areas for future development and improvement:

Model Retraining Pipeline: Implement an automated system for retraining the model with new data periodically or when performance metrics indicate a need for an update. This is crucial as fraud patterns evolve over time.

Advanced Feature Engineering: Explore creating more sophisticated features from raw transaction data, such as:

Aggregated features (e.g., number of transactions in the last hour/day/week, average transaction amount for a user).

Time-based features (e.g., time since last transaction, time of day).

Velocity features (e.g., number of transactions from a new IP address).

Explainability (XAI): Integrate tools like SHAP or LIME to provide insights into why a particular transaction was flagged as fraudulent. This can greatly assist human analysts in their investigations.

Feedback Loop: Develop a mechanism for human analysts to provide feedback on model predictions (e.g., marking a false positive as legitimate, or identifying a false negative). This feedback can then be used to continuously improve the model.

Real-time Data Streaming: For higher throughput and lower latency, consider integrating with a real-time data streaming platform (e.g., Apache Kafka, Amazon Kinesis) to process transactions as they occur.

Monitoring Dashboard: Create a comprehensive dashboard to visualize model performance metrics (precision, recall, F1-score, AUC), data drift, and concept drift over time.

Alerting System: Set up automated alerts for anomalies in model performance, data quality issues, or high volumes of suspicious transactions.

User Interface Enhancement: Develop a more interactive and robust frontend application that can handle real-time input, display predictions, and potentially offer options for manual review.

Scalability Improvements: For very high transaction volumes, explore deploying the model on more robust cloud ML platforms (e.g., AWS SageMaker, Google Cloud Vertex AI) that offer advanced scaling and MLOps capabilities.
