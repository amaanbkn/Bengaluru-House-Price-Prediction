from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and data
model = pickle.load(open('RidgeModel.pkl', 'rb'))
data = pd.read_csv('cleaned_data.csv')

@app.route('/')
def home():
    # Get unique locations for the dropdown
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = float(request.form.get('bhk'))
    bath = float(request.form.get('bath'))
    sqft = float(request.form.get('total_sqft'))

    # Create a dataframe for the input
    input_df = pd.DataFrame([[location, sqft, bath, bhk]], 
                            columns=['location', 'total_sqft', 'bath', 'bhk'])
    
    # Make prediction
    prediction = model.predict(input_df)[0]

    return str(np.round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True, port=5001)