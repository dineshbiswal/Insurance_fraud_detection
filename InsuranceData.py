#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:42:50 2021

@author: dinesh
"""

from pydantic import BaseModel


class InsuranceData(BaseModel):
    witnesses:int64
    incident_state:object
    incident_city:object
    incident_location:object
    incident_hour_of_the_day:int64
    number_of_vehicles_involved:int64
    property_damage:object
    bodily_injuries:int64
    police_report_available:object
    incident_severity:object
    total_claim_amount:int64
    injury_claim:int64
    property_claim:int64
    vehicle_claim:int64
    auto_make:object
    auto_model:object
    auto_year:int64
    authorities_contacted:object
    collision_type:object
    age:int64
    insured_zip:int64
    policy_number:int64
    policy_bind_date:object
    policy_state:object
    policy_csl:object
    policy_deductable:int64
    policy_annual_premium:float64
    umbrella_limit:int64
    insured_sex:object
    incident_type:object
    insured_education_level:object
    insured_occupation:object
    insured_hobbies:object
    insured_relationship:object
    capital-gains:int64
    capital-loss:int64
    incident_date:object
    
    