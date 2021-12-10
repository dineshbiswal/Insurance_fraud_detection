#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:35:28 2021

@author: dinesh
"""

import uvicorn
from fastapi import FastAPI
from InsuranceData import InsuranceData
from Preprocessor import Preprocessor
import pickle
import pandas as pd

app = FastAPI()
pickle_in = open("model/insurance_fruad_model.pklinsurance_fruad_model.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Welcome , '}


@app.post('/dopredict')
def predict_insurance_fraud(data:InsuranceData):
    data = data.dict()
    df = pd.DataFrame(data)
    
    df = Preprocessor.preprocess(df)
    
    
    prediction = classifier.predict(df)
    if(prediction[0] > 0.5):
        prediction ="Fraud"
    else:
        prediction ="Not Fraud"
    return {
        'prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload
