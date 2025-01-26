from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS  # Import flask_cors

# Load the saved model
model = joblib.load("house_price_model.pkl")

# Initialize Flask app
app = Flask(__name__)

# Apply CORS to the Flask app
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.get_json()
    print("Received data:", data)
    
    # Convert data into a DataFrame
    input_data = pd.DataFrame([data])
    
    # Make predictions
    prediction = 200000  # Placeholder, replace with model prediction
    
    # Return prediction as JSON
    return jsonify({'predicted_price': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
