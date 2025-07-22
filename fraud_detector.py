# fraud_detector.py (inside the functions/ directory)

import flask
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

# Initialize the Flask app
# static_folder and template_folder are not strictly necessary for a pure API function,
# but keeping them won't hurt if they were in the original app.
app = Flask(__name__)
CORS(app) # Enable CORS for frontend interaction

# Define the path to your model and scaler relative to the function file
# Assuming model and scaler are in the same directory as this function file
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'fraud_model.joblib')
SCALER_PATH = os.path.join(os.path.dirname(__file__), 'scaler.joblib')

# Load the model and scaler globally to avoid reloading on each request
try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("Model and scaler loaded successfully.") # Emojis removed
except FileNotFoundError:
    print(f"Error: Model or scaler file not found. Expected at {MODEL_PATH} and {SCALER_PATH}") # Emojis removed
    model = None
    scaler = None
except Exception as e:
    print(f"Error loading model or scaler: {e}") # Emojis removed
    model = None
    scaler = None

# NEW: Root endpoint for basic access check
@app.route('/')
def home():
    """
    Handles requests to the root URL.
    Returns a simple message to indicate the API is running.
    """
    return "Fraud Detector API is running! Send POST requests to /predict for predictions."

# This is the prediction endpoint that your frontend will call
@app.route('/predict', methods=['POST'])
def predict():
    """
    Handles prediction requests.
    Expects a JSON payload with 'time', 'amount', and 'v1' through 'v28' features.
    Returns a JSON response indicating 'result' (Fraudulent/Legitimate) and 'confidence'.
    """
    if model is None or scaler is None:
        # Return a server error if the model or scaler failed to load
        return jsonify({'error': 'Model or scaler not loaded. Please check deployment logs.'}), 500

    try:
        # Get JSON data from the request body
        data = request.get_json(force=True)
        print("Received data:", data) # Emojis removed

        # Extract V features (V1 to V28)
        # Ensure all V features are present in the incoming data
        v_features = [data[f'v{i}'] for i in range(1, 29)]

        # Scale 'amount' and 'time' using the pre-loaded scaler
        # The scaler.transform expects a 2D array, so wrap the scalar in [[ ]].
        # Then, extract the scaled scalar value using [0][0].
        scaled_amount = scaler.transform([[data['amount']]])[0][0]
        scaled_time = scaler.transform([[data['time']]])[0][0]

        # Combine all features in the correct order for the model
        # The order must match the training data: [V1...V28, scaled_Amount, scaled_Time]
        features = v_features + [scaled_amount, scaled_time]
        final_features = np.array(features).reshape(1, -1) # Reshape for single prediction

        # Make prediction and get probabilities
        prediction = model.predict(final_features)
        probability = model.predict_proba(final_features)

        # Determine result and confidence
        result = 'Fraudulent' if prediction[0] == 1 else 'Legitimate'
        confidence = round(max(probability[0]) * 100, 2) # Get confidence of the predicted class

        # Prepare response
        response = {'result': result, 'confidence': confidence}
        print("Sending response:", response) # Emojis removed
        return jsonify(response)

    except KeyError as ke:
        # Handle missing keys in the input JSON
        print(f"Missing data key: {ke}") # Emojis removed
        return jsonify({'error': f'Missing required data field: {ke}'}), 400
    except Exception as e:
        # Catch any other unexpected errors during prediction
        print(f"Error during prediction: {e}") # Emojis removed
        return jsonify({'error': str(e)}), 400

# Netlify's entry point for Python functions
# This function acts as a bridge between Netlify's event structure and your Flask app.
# You do NOT need to create a 'netlify_integration.py' file; it's provided by Netlify.
import sys
from io import BytesIO

def handler(event, context):
    """
    Netlify serverless function handler.
    Proxies the Netlify event to the Flask application.
    """
    # Use Flask's test_request_context to simulate an HTTP request for the Flask app
    with app.test_request_context(
        path=event['path'],
        method=event['httpMethod'],
        headers=event['headers'],
        data=event['body']
    ):
        # Capture the Flask response
        flask_response = app.full_dispatch_request()

        # Format the Flask response into the Netlify Functions expected format
        return {
            'statusCode': flask_response.status_code,
            'headers': dict(flask_response.headers),
            'body': flask_response.get_data(as_text=True)
        }
