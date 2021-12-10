#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 21:32:59 2021

@author: dinesh
"""
import pandas as pd
class Preprocessor():
    
    def preprocess(df):
        
        df['policy_bind_year'] = df['policy_bind_date'].str.extract('(\d{4})\-').astype("int64")
        df['incident_month'] = df['incident_date'].str.extract('\d{4}\-(\d{2})').astype("int64")
        df['collision_type'] = df['collision_type'].replace("?", "undocumented")
        df['police_report_available'] = df['police_report_available'].replace("?", "undocumented")
        df['property_damage'] = df['property_damage'].replace("?", "undocumented")
        
        df['insured_sex'] = df['insured_sex'].map({"FEMALE":0,"MALE":1})
        
        
        df['incident_severity'] = df['incident_severity'].map({"Trivial Damage":0,
                                                       "Minor Damage":1,
                                                       "Major Damage":2,
                                                       "Total Loss":3
                                                      }).astype("int64")
        if((df['capital-loss']<0.bool())):
            df['capital-loss'] = df['capital-loss']*(-1)
            
        to_drop = ['policy_bind_date','incident_date','incident_location','insured_zip','auto_model','policy_number','age','total_claim_amount','umbrella_limit']
        df.drop(to_drop, axis = 1, inplace = True)
        
        num_cols = ['insured_occupation', 'insured_sex', 'property_damage', 'incident_type', 'collision_type', 'insured_education_level', 'policy_state', 'authorities_contacted', 'incident_city', 'incident_state', 'insured_relationship', 'incident_month', 'policy_csl', 'insured_hobbies', 'auto_make', 'police_report_available']
        dum = pd.get_dummies(df[nom_var], drop_first=True)
        dum.reset_index(drop=True, inplace=True)
        df.reset_index(drop=True, inplace=True)
        df_dummied = pd.concat([dum, df], axis=1)
        df_dummied.drop(nom_var, axis=1, inplace=True)
        
        return df_dummied
        
