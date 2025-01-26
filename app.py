from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS  # Import flask_cors

# Load the saved model
model = joblib.load("house_price_model.pkl")
preprocessor=joblib.load("preprocessor.pkl")
# Initialize Flask app
app = Flask(__name__)

# Apply CORS to the Flask app
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
 data = request.get_json()
 
    
    # Convert data into a DataFrame
 input_data = pd.DataFrame([data])

 future_data = {
    'Type': ['Land'],  # Replace with actual values for prediction
    'Place': ['Colombo 3'],  # Replace with actual place
    'Status': ['Available'],  # Replace with the status (Available or Sold)
    'Balcony': ['Yes'],  # Yes or No for Balcony
    'Furnished': ['Yes'],  # Yes, Semi, or No
    'Loan': ['Available'],  # Available or Not Available
    '2022 Price (LKR)': [1000],  # Example values for the 2022 price
    '2021 Price (LKR)': [800],  # Example values for the 2021 price
    '2020 Price (LKR)': [1300],  # Example values for the 2020 price
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
 new_data_df = pd.DataFrame(future_data)
 new_data_processed = preprocessor.transform(new_data_df)
 predicted_price = model.predict(new_data_processed)
 predicted_price = predicted_price.tolist()  

 future_data2 = {
    'Type': ['Land'],  # Replace with actual values for prediction
    'Place': ['Colombo 3'],  # Replace with actual place
    'Status': ['Available'],  # Replace with the status (Available or Sold)
    'Balcony': ['Yes'],  # Yes or No for Balcony
    'Furnished': ['Yes'],  # Yes, Semi, or No
    'Loan': ['Available'],  # Available or Not Available
    '2022 Price (LKR)': predicted_price,  # Example values for the 2022 price
    '2021 Price (LKR)': [800],  # Example values for the 2021 price
    '2020 Price (LKR)': [1000],  # Example values for the 2020 price
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
 new_data_df2 = pd.DataFrame(future_data2)
 new_data_processed2 = preprocessor.transform(new_data_df2)

 predicted_price2 = model.predict(new_data_processed2)
 predicted_price2 = predicted_price2.tolist()  


 future_data3 = {
    'Type': ['Land'],  # Replace with actual values for prediction
    'Place': ['Colombo 3'],  # Replace with actual place
    'Status': ['Available'],  # Replace with the status (Available or Sold)
    'Balcony': ['Yes'], # Replace with the status (Available or Sold)
    'Balcony': ['Yes'],  # Yes or No for Balcony
    'Furnished': ['Yes'],  # Yes, Semi, or No
    'Loan': ['Available'],  # Available or Not Available
    '2022 Price (LKR)': predicted_price,  # Example values for the 2022 price
    '2021 Price (LKR)': predicted_price2,  # Example values for the 2021 price
    '2020 Price (LKR)': [1000],  # Example values for the 2020 price
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

 new_data_df3 = pd.DataFrame(future_data3)
 new_data_processed3 = preprocessor.transform(new_data_df3)
 predicted_price3 = model.predict(new_data_processed3)
 predicted_price3 = predicted_price3.tolist()  
    # Return prediction as JSON
 return jsonify({
            'predicted_price1': predicted_price,
            'predicted_price2': predicted_price2,
            'predicted_price3': predicted_price3
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
