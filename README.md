# Insurance_fraud_detection
Detect Fraud 
Build a small application, also locally but preffered in any cloud you want, based on the insurance_claims.csv in order to:
1)    The classification target attribute is the fraud_reported column: Y (Yes) / N (No)
2)    Analyse the original columns from data sets, identify and remove all kind of outliers and data issues that would endanger the accurate modelling. Show why those transformations were needed and prepare a wrapper for future similar data
3)    Divide the data properly into training, testing and prediction data sets
4)    Create the classification model, prove its efficiency on the testing model and apply it for prediction data set showing also the basis ruleset for the model
5)    Create an application including the previous sets and imagine the application should work on any future data with the same structure (columns and types) as the one in the csv file.

Used fast API for exposing the API to predict if fraud or not given data in json as below:

Input for evaluation:
=====================

{
    "months_as_customer": 134,
    "age": 29,
    "policy_number": 687698,
    "policy_bind_date": "2000-09-06",
    "policy_state": "OH",
    "policy_csl": "100/300",
    "policy_deductable": 2000,
    "policy_annual_premium": 1413.14,
    "umbrella_limit": 5000000,
    "insured_zip": 430632,
    "insured_sex": "FEMALE",
    "insured_education_level": "PhD",
    "insured_occupation": "sales",
    "insured_hobbies": "board-games",
    "insured_relationship": "own-child",
    "capital-gains": 35100,
    "capital-loss": 0,
    "incident_date": "2015-02-22",
    "incident_type": "Multi-vehicle Collision",
    "collision_type": "Rear Collision",
    "incident_severity": "Minor Damage",
    "authorities_contacted": "Police",
    "incident_state": "NY",
    "incident_city": "Columbus",
    "incident_location": "7121 Francis Lane",
    "incident_hour_of_the_day": 7,
    "number_of_vehicles_involved": 3,
    "property_damage": "NO",
    "bodily_injuries": 2,
    "witnesses": 3,
    "police_report_available": "NO",
    "total_claim_amount": 34650,
    "injury_claim": 7700,
    "property_claim": 3850,
    "vehicle_claim": 23100,
    "auto_make": "Dodge",
    "auto_model": "RAM",
    "auto_year": 2007
  }
