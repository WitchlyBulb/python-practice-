'''Drill 6: Patient Alerts with Labs
Each patient has: name, age, visits: a list of visit dictionaries, each with:
vitals: temp, heart_rate, systolic_bp, diastolic_bp, symptoms: list of strings
labs: dictionary with wbc (white blood cell count), glucose
Rules (per visit):
Fever: Age < 60 → temp > 100, Age ≥ 60 → temp > 99
High heart rate: hr > 100
High BP: systolic > 140 or diastolic > 90
Low BP: systolic < 90 or diastolic < 60
Symptoms:
"chest pain" → "Chest Pain Alert"
"shortness of breath" → "Breathing Alert"
Lab Alerts:
WBC > 11000 → "Possible Infection"
Glucose > 200 → "High Blood Sugar"
Task:
Loop through each patient and each visit, analyze all three categories (vitals, symptoms, labs), and print alerts.'''

patients = [
    {"name": "Olivia", "age": 70, "visits": [
        {"vitals": {"temp": 100.8, "heart_rate": 96, "systolic_bp": 142, "diastolic_bp": 88}, 
         "symptoms": ["fatigue"], 
         "labs": {"wbc": 12000, "glucose": 180}},
        {"vitals": {"temp": 98.9, "heart_rate": 105, "systolic_bp": 135, "diastolic_bp": 80}, 
         "symptoms": ["chest pain"], 
         "labs": {"wbc": 8000, "glucose": 210}}
    ]},
    {"name": "Paul", "age": 55, "visits": [
        {"vitals": {"temp": 99.0, "heart_rate": 88, "systolic_bp": 118, "diastolic_bp": 75}, 
         "symptoms": [], 
         "labs": {"wbc": 7000, "glucose": 95}},
        {"vitals": {"temp": 101.5, "heart_rate": 112, "systolic_bp": 125, "diastolic_bp": 78}, 
         "symptoms": ["shortness of breath"], 
         "labs": {"wbc": 13000, "glucose": 220}}
    ]}
]

# Loop through patient list
for pt in patients:
    name = pt["name"]
    age = pt["age"]

    # Loop through diff visits for same patient, number each visit
    for visit_id, visit in enumerate(pt["visits"], start=1):
        temp = visit["vitals"]["temp"]
        hr = visit["vitals"]["heart_rate"]
        sbp = visit["vitals"]["systolic_bp"]
        dbp = visit["vitals"]["diastolic_bp"]
        wbc = visit["labs"]["wbc"]
        glucose = visit["labs"]["glucose"]

        # list of alerts per visit
        alerts = []

        # ---------- analyze alerts ----------
        # Fever: Age < 60 → temp > 100, Age ≥ 60 → temp > 99
        if ((age < 60 and temp > 100) or
            (age >= 60 and temp > 99)):
            alerts.append("Fever")
        # High heart rate: hr > 100    
        if hr > 100:
            alerts.append("High heart rate")
        # High BP: systolic > 140 or diastolic > 90
        if sbp > 140 or dbp > 90:
            alerts.append("High BP")
        # Low BP: systolic < 90 or diastolic < 60
        elif sbp < 90 or dbp < 60:
            alerts.append("Low BP")        
        # Symptoms:"chest pain" → "Chest Pain Alert"
        if "chest pain" in visit["symptoms"]:
            alerts.append("Chest Pain Alert")
        # "shortness of breath" → "Breathing Alert"
        if "shortness of breath" in visit["symptoms"]:
            alerts.append("Breathing Alert")
        # WBC > 11000 → "Possible Infection"
        if wbc > 11000:
            alerts.append("Possible Infection")
        # Glucose > 200 → "High Blood Sugar"
        if glucose > 200:
            alerts.append("High Blood Sugar")

        # ---------- output ----------
        if alerts:
            print(f"ALERT for {name}, Visit {visit_id}: {', '.join(alerts)}")
        else:
            print(f"{name}, Visit {visit_id} is stable")
