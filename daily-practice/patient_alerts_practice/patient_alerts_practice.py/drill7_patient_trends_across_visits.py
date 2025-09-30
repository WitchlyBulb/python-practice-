'''Drill 7: Patient Trends Across Visits
We want to expand your alert system so it not only looks at single-visit values but also trends between visits for the same patient.
Requirements
In addition to your current checks:
BP Rising Trend → systolic increases by ≥ 20 points compared to the previous visit
Glucose Increasing → glucose is higher than the previous visit
Expected Output
Sophia, Visit 1 is stable
ALERT for Sophia, Visit 2: Fever, High BP, BP Rising Trend, Glucose Increasing
ALERT for Sophia, Visit 3: Fever, High heart rate, High BP, Breathing Alert, Possible Infection, High Blood Sugar, BP Rising Trend, Glucose Increasing
Ethan, Visit 1 is stable
ALERT for Ethan, Visit 2: Chest Pain Alert, Glucose Increasing
This drill will push you to:
Track previous visit values while looping (prev_bp, prev_glucose)
Compare them to current values
Append alerts accordingly'''

# Dataset
patients = [
    {"name": "Sophia", "age": 68, "visits": [
        {"vitals": {"temp": 99.8, "heart_rate": 88, "systolic_bp": 130, "diastolic_bp": 82}, 
         "symptoms": [], 
         "labs": {"wbc": 9000, "glucose": 150}},
        {"vitals": {"temp": 100.5, "heart_rate": 95, "systolic_bp": 155, "diastolic_bp": 92}, 
         "symptoms": [], 
         "labs": {"wbc": 9500, "glucose": 180}},
        {"vitals": {"temp": 101.0, "heart_rate": 102, "systolic_bp": 178, "diastolic_bp": 96}, 
         "symptoms": ["shortness of breath"], 
         "labs": {"wbc": 12000, "glucose": 210}}
    ]},
    {"name": "Ethan", "age": 50, "visits": [
        {"vitals": {"temp": 98.7, "heart_rate": 76, "systolic_bp": 118, "diastolic_bp": 76}, 
         "symptoms": [], 
         "labs": {"wbc": 6000, "glucose": 95}},
        {"vitals": {"temp": 99.1, "heart_rate": 82, "systolic_bp": 122, "diastolic_bp": 78}, 
         "symptoms": ["chest pain"], 
         "labs": {"wbc": 7500, "glucose": 105}}
    ]}
]
# loop through the list 'patients'
for pt in patients:
    name = pt["name"]
    age = pt["age"]
    prev_sbp = None # to track blood pressure trend
    prev_glucose = None # track glucose trend

    # loop through the visits for each patient, number each visit
    for visit_id, visit in enumerate(pt["visits"], start=1):
        temp = visit["vitals"]["temp"]
        hr = visit["vitals"]["heart_rate"]
        sbp = visit["vitals"]["systolic_bp"]
        dbp = visit["vitals"]["diastolic_bp"]
        wbc = visit["labs"]["wbc"]
        glucose = visit["labs"]["glucose"]

        # ---------- analyze alerts ----------
        # create a list of alerts for each visit of each patient
        alerts = []
        
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
        # Symptoms: "chest pain" → "Chest Pain Alert"
        if "chest pain" in visit["symptoms"]:
            alerts.append("Chest Pain Alert")
        # "shortness of breath" → "Breathing Alert"
        if "shortness of breath" in visit["symptoms"]:
            alerts.append("Breathing Alert")
        # Lab Alerts: WBC > 11000 → "Possible Infection"
        if wbc > 11000:
            alerts.append("Possible Infection")
        # Glucose > 200 → "High Blood Sugar"
        if glucose > 200:
            alerts.append("High Blood Sugar")
        # BP Rising Trend → systolic increases by ≥ 20 points compared to the previous visit
        if prev_sbp is not None and sbp - prev_sbp >= 20:
            alerts.append("BP Rising Trend")  
        # Glucose Increasing → glucose is higher than the previous visit
        if prev_glucose is not None and glucose > prev_glucose:
            alerts.append("Glucose Increasing")
        
        prev_sbp = sbp
        prev_glucose = glucose

        # ---------- OUTPUT ----------
        if alerts: 
            print(f"ALERT for {name}, Visit {visit_id}: ")
            for alert in alerts:
                print(f"  - {alert}")
        else:
            print(f"{name}, Visit {visit_id} is stable")
    print()
