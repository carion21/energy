from flask import Flask, request

from constants import LOCAL_PORT, MODE, MODEL_PATHS
from utilities import make_prediction

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/predict', methods=['POST'])
def predict():
    request_data = request.get_json()
    
    groupname = request_data["groupname"]
    upfront   = request_data["upfront"]
    unlock  = request_data["unlock"]
    gender  = request_data["gender"]
    age     = request_data["age"]
    occupation  = request_data["occupation"]
    langue  = request_data["langue"]
    region  = request_data["region"]

    data = {
        'Group Name': groupname,
        'Upfront Price': upfront,
        'Unlock Price': unlock,
        'Customer Gender': gender,
        'Customer Age': age,
        'Customer Occupation': occupation,
        'Langue': langue,
        'Region': region
        }
    
    mp = MODEL_PATHS[MODE]
    v = make_prediction(mp, data)
    
    print("=====================")
    print(" ")
    print("=====================")
    
    return {"prediction": str(v)}



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=LOCAL_PORT, debug=True)
