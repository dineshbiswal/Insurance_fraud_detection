#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:35:28 2021

@author: dinesh
"""

import uvicorn
from fastapi import FastAPI

from InsuranceData import InsuranceData

import pandas as pd
import pickle

app = FastAPI()
# loading saved models
classifier = pickle.load(open("model/xgb_best_model.pkl", "rb"))
preprocessor = pickle.load(open("model/preprocessor_pipeline.pkl", "rb"))


@app.get('/')
def index():
    return {'message': 'Welcome ,to the fraud detection application '}


@app.post('/dopredict')
def predict_insurance_fraud(data: InsuranceData):
    data = data.dict()
    df = pd.DataFrame(data, index=[0])

    # preprocessing data
    df['policy_bind_year'] = df['policy_bind_date'].str.extract('(\d{4})\-').astype('int')

    df['incident_month'] = df['incident_date'].str.extract('\d{4}\-(\d{2})').astype('int')
    unreported_cols = df.columns[df.isin(['?']).any()]
    if unreported_cols.any():
        df[unreported_cols] = df[unreported_cols].replace('?', 'unreported')

    large_cat = ['policy_bind_date', 'incident_date', 'incident_location',
                 'insured_zip', 'auto_model', 'policy_number', 'age', 'total_claim_amount']
    df.drop(large_cat, axis=1, inplace=True)
    df.reset_index(inplace=True, drop=True)
    df = preprocessor.transform(df)

    prediction = classifier.predict(df)
    if prediction[0] == 0:
        prediction = "Not Fraud"
    else:
        prediction = "Fraud"
    return {
        'prediction': prediction
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn app:app --reload
