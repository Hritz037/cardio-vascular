from flask import Flask
from models import db, Patient, HealthMetrics, HeartRisk
from datetime import datetime

# Configure and initialize your database here

def add_patient_data():
    p1 = {
        "aadhaar_number": "123455678986",
        "BMI": ["19.3", "19.4", "19.2", "19.5"],
        "Sbp": ["114", "90", "95", "90"],  # Removed 'mm hg' for simplicity
        "DBP": ["80", "79.8", "80.2", "79.7"],
        "Hbg": ["13.6", "13.3", "13.5", "13.7"],
        "Heart attack risk": ["High risk", "mild risk", "low risk", "completely healthy"],
        "Date": ["23/01/2024", "19/02/2024", "14/03/2024", "03/04/2024", "30/04/2024"],
        "Heart attack risk": [2, 1, 0, 0]
    }

    # Check if patient exists
    patient = Patient.query.filter_by(aadhaar_number=p1['aadhaar_number']).first()
    # if not patient:
    #     return "Patient not found", 404

    # Convert string risk levels to integers or enums as required

    for i in range(len(p1['BMI'])):
        # Create HealthMetrics entry
        date = datetime.strptime(p1['Date'][i], date_format)
        health_metric = HealthMetrics(
            patient_id=patient.id,
            date=date,
            bmi=float(p1['BMI'][i]),
            sbp=int(p1['Sbp'][i]),
            dbp=float(p1['DBP'][i]),
            haemoglobin=float(p1['Hbg'][i])
        )
        db.session.add(health_metric)

        # Create HeartRisk entry
        heart_risk = HeartRisk(
            patient_id=patient.id,
            date=date,
            risk_level=p1['Heart attack risk'][i]
        )
        db.session.add(heart_risk)

    # Commit the session to save all data
    db.session.commit()

    return "Patient data added successfully", 200

add_patient_data()
