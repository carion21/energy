from typing import Optional
import pandas as pd
from joblib import load


def format_data(data : dict) -> dict:
    """
    Format data
    """
    for k,v in data.items():
        data[k] = [v]
    return data

def make_prediction(modelpath : str, data : dict) -> int:
    """
    Make prediction on data
    """
    v = -1
    model = load(modelpath)
    data = format_data(data)
    indiv = pd.DataFrame(data)
    respe = model.predict(indiv)
    if len(respe) == 1:
        v = respe[0]
    return v