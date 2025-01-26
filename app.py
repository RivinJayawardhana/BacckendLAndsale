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

    future_data3 = {
    'Type': data['Land'],  # Replace with actual values for prediction
    'Place': data['Colombo 3'],  # Replace with actual place
    'Status':data['Available'],  # Replace with the status (Available or Sold)
    'Balcony': data['Yes'],  # Yes or No for Balcony
    'Furnished': data['Yes'],  # Yes, Semi, or No
    'Loan': data['Available'],  # Available or Not Available
    '2022 Price (LKR)': ,  # Example values for the 2022 price
    '2021 Price (LKR)': ,  # Example values for the 2021 price
    '2020 Price (LKR)': ,  # Example values for the 2020 price
    'Rooms': [2],  # Example room counts
    'Bed': [8],  # Example bed counts
    'Deposit Amount (LKR)': [8130300],  # Example deposit amounts
    'Bedroom': [8],  # Example bedroom counts
    'Bathroom': [3],  # Example bathroom counts
    'Carpet Area (sqft)': [4262],  # Example carpet area in sqft
    'Age': [49],  # Example age of the property
    'Total Floors': [14],  # Example total floors
    'Room Floor': [8]  # Example room floor count
}
    
    # Make predictions
    prediction = 200000  # Placeholder, replace with model prediction
    
    # Return prediction as JSON
    return jsonify({'predicted_price': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
