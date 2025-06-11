from fastapi import FastAPI, HTTPException, Header
from tensorflow.keras.models import load_model
import numpy as np
import os

app = FastAPI()

# Load your model
lstm_model = load_model('lstm_model.keras')

API_KEY = os.environ.get("API_KEY", "changeme")  # Use env variable for security

def authenticate(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

@app.post("/predict")
def predict(data: dict, api_key: str = Header(...)):
    authenticate(api_key)
    X = np.array(data["inputs"])
    preds = lstm_model.predict(X)
    return {"prediction": preds.tolist()}

import os

API_KEY = os.environ.get("API_KEY")
print(f"API Key in use: {API_KEY}")  # For debugging only!
