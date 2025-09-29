'''Drill 4: Comprehensive Patient Alert
Each patient has: name, age, vitals: temp, heart_rate, systolic_bp, diastolic_bp, symptoms: list of strings
Rules:
Fever alert: Age < 60 → temp > 100, Age ≥ 60 → temp > 99
High heart rate: hr > 100 → "High Heart Rate"
High blood pressure: systolic_bp > 140 → "High BP", diastolic_bp > 90 → "High BP"
Low blood pressure: systolic_bp < 90 → "Low BP", diastolic_bp < 60 → "Low BP"
Symptom alerts: "chest pain" → "Chest Pain Alert", "shortness of breath" → "Breathing Alert"
Task:
Collect all alerts in a list per patient.
Print:
ALERT for [name]: ... if any alerts exist
[name] is stable otherwise
Starter Data
patients = [
    {"name": "Ivy", "age": 72, "vitals": {"temp": 100.5, "heart_rate": 95, "systolic_bp": 145, "diastolic_bp": 85}, "symptoms": ["fatigue"]},
    {"name": "Jack", "age": 50, "vitals": {"temp": 101.2, "heart_rate": 105, "systolic_bp": 135, "diastolic_bp": 78}, "symptoms": ["chest pain"]},
    {"name": "Kate", "age": 65, "vitals": {"temp": 98.9, "heart_rate": 80, "systolic_bp": 120, "diastolic_bp": 75}, "symptoms": ["shortness of breath"]},
    {"name": "Leo", "age": 45, "vitals": {"temp": 98.4, "heart_rate": 70, "systolic_bp": 110, "diastolic_bp": 70}, "symptoms": []}
]
'''
#Starter Data
patients = [
    {"name": "Ivy", "age": 72, "vitals": {"temp": 100.5, "heart_rate": 95, "systolic_bp": 145, "diastolic_bp": 85}, "symptoms": ["fatigue"]},
    {"name": "Jack", "age": 50, "vitals": {"temp": 101.2, "heart_rate": 105, "systolic_bp": 135, "diastolic_bp": 78}, "symptoms": ["chest pain"]},
    {"name": "Kate", "age": 65, "vitals": {"temp": 98.9, "heart_rate": 80, "systolic_bp": 120, "diastolic_bp": 75}, "symptoms": ["shortness of breath"]},
    {"name": "Leo", "age": 45, "vitals": {"temp": 98.4, "heart_rate": 70, "systolic_bp": 110, "diastolic_bp": 70}, "symptoms": []}
]
for pt in patients:
    name = pt["name"]
    age = pt["age"]
    temp = pt["vitals"]["temp"]
    hr = pt["vitals"]["heart_rate"]
    sbp = pt["vitals"]["systolic_bp"]
    dbp = pt["vitals"]["diastolic_bp"]

    # Collect all alerts in a list per patient.
    alerts = []

    # Fever alert: Age < 60 → temp > 100, Age ≥ 60 → temp > 99
    if ((age < 60 and temp > 100) or 
        (age >= 60 and temp > 99)):
        alerts.append("Fever")
    # High heart rate: hr > 100 → "High Heart Rate"
    if hr > 100:
        alerts.append("High Heart Rate")
    # High blood pressure: systolic_bp > 140 → "High BP", diastolic_bp > 90 → "High BP"
    if (sbp > 140 or dbp > 90):
        alerts.append("High BP")
        # Low blood pressure: systolic_bp < 90 → "Low BP", diastolic_bp < 60 → "Low BP"
    elif (sbp < 90 or dbp < 60):
        alerts.append("Low BP")
    # Symptom alerts: "chest pain" → "Chest Pain Alert", "shortness of breath" → "Breathing Alert"
    if "chest pain" in pt["symptoms"]:
        alerts.append("Chest Pain Alert")
    if "shortness of breath" in pt["symptoms"]:
        alerts.append("Breathing Alert")
    
    if alerts:
        print(f"ALERT for {name}: {', '.join(alerts)}")
    else:
        print(f"{name} is stable")
