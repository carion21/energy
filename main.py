from fastapi import FastAPI

from classes.individu import Individu
from classes.prediction import Prediction
from constants import MODE, MODEL_PATHS
from utilities import format_data, make_prediction

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict")
async def predict(indiv : Individu):
    data = {
        'Group Name': indiv.groupname,
        'Upfront Price': indiv.upfront,
        'Unlock Price': indiv.unlock,
        'Customer Gender': indiv.gender,
        'Customer Age': indiv.age,
        'Customer Occupation': indiv.occupation,
        'Langue': indiv.langue,
        'Region': indiv.region
        }
    mp = MODEL_PATHS[MODE]
    v = make_prediction(mp, data)
    
    print("=====================")
    print(" ")
    print("=====================")
    
    return {"prediction": str(v)}
