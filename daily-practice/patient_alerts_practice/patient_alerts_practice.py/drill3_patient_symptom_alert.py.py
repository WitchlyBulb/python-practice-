'''Drill 3: Multiple Symptom Alerts
Each patient has: name, age, vitals: temp, heart_rate, symptoms: list of strings
Rules:
If temp > 100 → "Fever"
If heart_rate > 100 → "High Heart Rate"
If "chest pain" is in symptoms → "Chest Pain Alert"
If "shortness of breath" is in symptoms → "Breathing Alert"
Task:
Collect all alerts in a list per patient.
Print:
ALERT for [name]: ... if alerts exist
[name] is stable otherwise
Starter Data
patients = [
    {"name": "Emma", "age": 60, "vitals": {"temp": 101.5, "heart_rate": 98}, "symptoms": ["cough", "chest pain"]},
    {"name": "Frank", "age": 45, "vitals": {"temp": 98.6, "heart_rate": 110}, "symptoms": ["fatigue"]},
    {"name": "Grace", "age": 70, "vitals": {"temp": 99.1, "heart_rate": 85}, "symptoms": ["shortness of breath"]},
    {"name": "Henry", "age": 50, "vitals": {"temp": 98.4, "heart_rate": 75}, "symptoms": []}
]
Expected Output
ALERT for Emma: Fever, Chest Pain Alert
ALERT for Frank: High Heart Rate
ALERT for Grace: Breathing Alert
Henry is stable'''

#Starter Data
patients = [
    {"name": "Emma", "age": 60, "vitals": {"temp": 101.5, "heart_rate": 98}, "symptoms": ["cough", "chest pain"]},
    {"name": "Frank", "age": 45, "vitals": {"temp": 98.6, "heart_rate": 110}, "symptoms": ["fatigue"]},
    {"name": "Grace", "age": 70, "vitals": {"temp": 99.1, "heart_rate": 85}, "symptoms": ["shortness of breath"]},
    {"name": "Henry", "age": 50, "vitals": {"temp": 98.4, "heart_rate": 75}, "symptoms": []}
]

for pt in patients:
    name = pt["name"]
    temp = pt["vitals"]["temp"]
    hr = pt["vitals"]["heart_rate"]

    # collect all alerts in a list
    alerts = []

    # If temp > 100 → "Fever"
    if temp > 100:
        alerts.append("Fever")
    # If heart_rate > 100 → "High Heart Rate"
    if hr > 100:
        alerts.append("High Heart Rate")
    # If "chest pain" is in symptoms → "Chest Pain Alert"
    if "chest pain" in pt["symptoms"]:
        alerts.append("Chest Pain Alert")
    # If "shortness of breath" is in symptoms → "Breathing Alert"
    if "shortness of breath" in pt["symptoms"]:
        alerts.append("Breathing Alert")

    #Print:ALERT for [name]: ... if alerts exist, [name] is stable otherwise
    if alerts:
        print(f"ALERT for {name}: {', '.join(alerts)}")
    else:
        print(f"{name} is stable")

    
