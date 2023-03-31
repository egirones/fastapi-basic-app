"""
Name: Edgar Gironés
Date: 21.03.2023
"""

import pickle
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from train_predict.predict import inference
from train_predict.utils import preprocess_data


class ItemToPredict(BaseModel):
    age: int
    workclass: str
    fnlgt: int
    education: str
    education_num: int
    marital_status: str
    occupation: str
    relationship: str
    race: str
    sex: str
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: str


with open("./model/model.pkl", 'rb') as pickle_file:
    model = pickle.load(pickle_file)
with open("./model/encoder.pkl", 'rb') as pickle_file:
    encoder = pickle.load(pickle_file)

description = """
    Basic API API helps you do awesome ML. 🚀

    ## Predict

    Allows you to predict the salary based on personal information.
    See below for more option
    """

app = FastAPI(
    title="Basic API",
    description=description
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/predict")
async def predict(fields: ItemToPredict):
    preprocessed_fields = preprocess_data(fields)
    predicted = inference(model, preprocessed_fields)
    return predicted


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
