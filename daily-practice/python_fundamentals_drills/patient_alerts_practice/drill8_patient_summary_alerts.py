'''Drill 8: Patient Summary Alerts
Requirements
For each patient:
Keep your current per-visit alerts (just like in Drill 7).
Add patient-level summary after all visits:
If the patient ever had "High Blood Sugar" in any visit → mark "Diabetes Concern".
If the patient had "BP Rising Trend" in ≥ 2 visits → mark "Hypertension Trend".
If the patient had "Possible Infection" in any visit and fever in the same visit → mark "Infection with Fever".
Expected Flow
Print visit-level alerts (like you did).
After the patient’s visits, print a Summary section with these higher-level conclusions.
If no summary alerts apply, print "No major long-term concerns detected."
Also track “flags” in summary lists or counters:
Example: had_high_glucose = False, bp_rising_count = 0, etc.
🔍 Sample Output (abbreviated)
ALERT for Sophia, Visit 1:
  - Fever
  - High BP

ALERT for Sophia, Visit 2:
  - High BP
  - BP Rising Trend
  - Glucose Increasing

ALERT for Sophia, Visit 3:
  - Fever
  - High heart rate
  - High BP
  - Possible Infection
  - High Blood Sugar
  - BP Rising Trend
  - Glucose Increasing
  - Breathing Alert

--- Summary for Sophia ---
  - Diabetes Concern
  - Hypertension Trend
  - Infection with Fever'''

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
    summary_tracking = []

    # trackers for summary
    had_high_glucose = False
    bp_rising_count = 0
    had_infection_with_fever = False

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
            had_high_glucose = True
        # BP Rising Trend → systolic increases by ≥ 20 points compared to the previous visit
        if prev_sbp is not None and sbp - prev_sbp >= 20:
            alerts.append("BP Rising Trend") 
            bp_rising_count += 1
        # Glucose Increasing → glucose is higher than the previous visit
        if prev_glucose is not None and glucose > prev_glucose:
            alerts.append("Glucose Increasing")
        

        # ----------- Infection + Fever combo ----------
        if "Possible Infection" in alerts and "Fever" in alerts:
            had_infection_with_fever = True

        prev_sbp = sbp
        prev_glucose = glucose

        # ---------- OUTPUT ----------
        if alerts: 
            print(f"ALERT for {name}, Visit {visit_id}: ")
            for alert in alerts:
                print(f" - {alert}")
        else:
            print(f"{name}, Visit {visit_id} is stable")

    # ---------- SUMARY ----------
    print()
    print(f"--- Summary for {name} ---")
    if had_high_glucose:
        print("  - Diabetes Concern")
    if bp_rising_count >= 2:
        print("  - Hypertension Trend")
    if had_infection_with_fever:
        print("  - Possible Infection")
    if not (had_high_glucose or bp_rising_count >= 2 or had_infection_with_fever):
        print("No major long-term concerns detected.")
    print("\n")


