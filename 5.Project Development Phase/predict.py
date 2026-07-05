import joblib
import numpy as np

# Load the trained model
model = joblib.load("models/flood_model.pkl")

def predict_flood(data):
    """
    Predict flood occurrence.
    Input: List of 10 values
    Output: Prediction (0 or 1)
    """
    data = np.array(data).reshape(1, -1)
    prediction = model.predict(data)
    return prediction[0]