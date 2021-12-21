#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:42:50 2021

@author: dinesh
"""

from typing import Optional

from pydantic import BaseModel


class InsuranceData(BaseModel):
    months_as_customer: int
    age: int
    policy_number: int
    policy_bind_date: str
    policy_state: str
    policy_csl: str
    policy_deductable: float
    policy_annual_premium: float
    umbrella_limit: Optional[int] = None
    insured_zip: Optional[int] = None
    insured_sex: str
    insured_education_level: str
    insured_occupation: str
    insured_hobbies: str
    insured_relationship: str
    capital_gains: Optional[int] = 0
    capital_loss: Optional[int] = 0
    incident_date: str
    incident_type: str
    collision_type: str
    incident_severity: str
    authorities_contacted: str
    incident_state: str
    incident_city: str
    incident_location: str
    incident_hour_of_the_day: int
    number_of_vehicles_involved: int
    property_damage: str
    bodily_injuries: int
    witnesses: int
    police_report_available: str
    total_claim_amount: int
    injury_claim: int
    property_claim: int
    vehicle_claim: int
    auto_make: Optional[str] = None
    auto_model: Optional[str] = None
    auto_year: Optional[int] = None
