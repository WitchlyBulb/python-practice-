'''Drill 5: Patient Multiple Visits Alerts
Each patient has: name, age, 
visits: a list of visit dictionaries, each with: vitals: temp, heart_rate, systolic_bp, diastolic_bp
symptoms: list of strings
Rules (per visit):
Fever: Age < 60 → temp > 100, Age ≥ 60 → temp > 99
High heart rate: hr > 100 → "High Heart Rate"
High BP: systolic_bp > 140 or diastolic_bp > 90 → "High BP"
Low BP: systolic_bp < 90 or diastolic_bp < 60 → "Low BP"
Symptoms: "chest pain" → "Chest Pain Alert", "shortness of breath" → "Breathing Alert"
Task:
Loop through each patient, then through each visit.
Print alerts for each visit:
ALERT for [name], Visit 1: Fever, High BP
ALERT for [name], Visit 2: High Heart Rate
[name], Visit 3 is stable'''

# Starter Data
patients = [
    {"name": "Mia", "age": 65, "visits": [
        {"vitals": {"temp": 100.5, "heart_rate": 95, "systolic_bp": 142, "diastolic_bp": 88}, "symptoms": ["fatigue"]},
        {"vitals": {"temp": 101.2, "heart_rate": 102, "systolic_bp": 135, "diastolic_bp": 92}, "symptoms": ["chest pain"]}
    ]},
    {"name": "Nate", "age": 50, "visits": [
        {"vitals": {"temp": 98.6, "heart_rate": 85, "systolic_bp": 118, "diastolic_bp": 75}, "symptoms": []},
        {"vitals": {"temp": 99.5, "heart_rate": 110, "systolic_bp": 125, "diastolic_bp": 80}, "symptoms": ["shortness of breath"]}
    ]}
]

# Loop through each patient, then through each visit
for pt in patients:
    name = pt["name"]
    age = pt["age"]
    visit_id = 1

    for visit_id, visit in enumerate(pt["visits"], start=1):
        temp = visit["vitals"]["temp"]
        hr = visit["vitals"]["heart_rate"]
        sbp = visit["vitals"]["systolic_bp"]
        dbp = visit["vitals"]["diastolic_bp"]

        # ---------- analyze ALERTS ----------
        # save alerts in a list:
        alerts = []
        # Fever: Age < 60 → temp > 100, Age ≥ 60 → temp > 99
        if ((age < 60 and temp > 100) or
            (age >= 60 and temp > 99)):
            alerts.append("Fever")
        # High heart rate: hr > 100 → "High Heart Rate"
        if hr > 100:
            alerts.append("High Heart Rate")
        # High BP: systolic_bp > 140 or diastolic_bp > 90 → "High BP"
        if sbp > 140 or dbp > 90:
            alerts.append("High BP")
        # Low BP: systolic_bp < 90 or diastolic_bp < 60 → "Low BP"
        elif sbp < 90 or dbp < 60:
            alerts.append("Low BP")
        # Symptoms: "chest pain" → "Chest Pain Alert", "shortness of breath" → "Breathing Alert"
        if "chest pain" in visit["symptoms"]:
            alerts.append("Chest Pain Alert")
        if "shortness of breath" in visit["symptoms"]:
            alerts.append("Breathing Alert")
        

        # ---------- OUTPUT ----------
        if alerts:
            print(f"ALERT for {name}, Visit {visit_id}: {', '.join(alerts)}")
        else:
            print(f"{name}, Visit {visit_id} is stable")
