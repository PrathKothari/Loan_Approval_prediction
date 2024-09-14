from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

model_path = "./model_tree.pkl"

# Load the model
try:
    model = joblib.load(model_path)
except Exception as e:
    logging.error(f"Failed to load model: {e}")
    raise RuntimeError("Failed to load model")

# Initialize the FastAPI app
app = FastAPI()

class InputData(BaseModel):
    Married: int
    Dependents: int
    Education: int
    Self_Employed: int
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: int
    Total_Income: float

@app.post("/predict")
async def predict(data: InputData):
    try:
        features = np.array([[data.Married, data.Dependents, data.Education, data.Self_Employed, data.LoanAmount, data.Loan_Amount_Term, data.Credit_History, data.Property_Area, data.Total_Income]])
        prediction = model.predict(features)
        return {"prediction": int(prediction)}
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Prediction error occurred")

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI ML model!"}
