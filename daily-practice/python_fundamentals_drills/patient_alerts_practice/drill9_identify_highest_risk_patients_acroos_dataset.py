'''Drill 9: Identify Highest-Risk Patients Across Dataset
Goal:
Loop through all patients and visits, generate alerts (like Drill 8), 
and then highlight the patients with the highest number of high-risk alerts across all visits.
Requirements:
Per-visit alerts (all rules from Drill 8: Fever, Heart Rate, BP, Labs, Symptoms, Trends).
Track total number of alerts per patient across all visits.
At the end, print the patient(s) with the most alerts.
Print summary for each patient as before.
Expected Sample Output (rough idea):
Patient: Mia
 Visit 1:
   - Fever
   - High BP
   - Possible Infection
 Visit 2:
   - Fever
   - High heart rate
   - High BP
   - Chest Pain Alert
   - Possible Infection
   - High Blood Sugar
Patient: Liam
 Visit 1:
   Stable
 Visit 2:
   - Fever
   - High heart rate
   - Glucose Increasing
   - Breathing Alert
   - High Blood Sugar
Patient: Emma
 Visit 1:
   - Fever
   - High BP
   - Chest Pain Alert
   - High Blood Sugar
--- Highest Risk Patients ---
  - Mia (6 alerts)
Challenge Tasks for You (no solution given yet):
Use your Drill 8 logic for alerts per visit.
Track total alert count per patient across all visits.
After processing all patients, identify the patient(s) with the most alerts.
Output should be clean, with patient name once, visits indented, and summary clearly separated.'''

# Starter Data:
patients = [
    {"name": "Mia", "age": 72, "visits": [
        {"vitals": {"temp": 100.2, "heart_rate": 98, "systolic_bp": 145, "diastolic_bp": 90}, 
         "symptoms": ["fatigue"], "labs": {"wbc": 11500, "glucose": 180}},
        {"vitals": {"temp": 101.0, "heart_rate": 102, "systolic_bp": 160, "diastolic_bp": 95}, 
         "symptoms": ["chest pain"], "labs": {"wbc": 12000, "glucose": 210}}
    ]},
    {"name": "Liam", "age": 60, "visits": [
        {"vitals": {"temp": 98.6, "heart_rate": 85, "systolic_bp": 130, "diastolic_bp": 80}, 
         "symptoms": [], "labs": {"wbc": 8000, "glucose": 150}},
        {"vitals": {"temp": 100.5, "heart_rate": 110, "systolic_bp": 135, "diastolic_bp": 88}, 
         "symptoms": ["shortness of breath"], "labs": {"wbc": 9000, "glucose": 220}}
    ]},
    {"name": "Emma", "age": 55, "visits": [
        {"vitals": {"temp": 101.2, "heart_rate": 100, "systolic_bp": 142, "diastolic_bp": 85}, 
         "symptoms": ["chest pain"], "labs": {"wbc": 10000, "glucose": 230}}
    ]}
]

# to track alerts count for all patients
alerts_count_for_all_patients = {}

for pt in patients:
    name = pt["name"]
    age = pt["age"]
    prev_sbp = None
    prev_glucose = None
    alerts_count = 0

    # Trackers for summary
    had_high_glucose = False
    bp_rising_count = 0
    had_infection_with_fever = False

    print(f"Patient: {name}")

    for visit_id, visit in enumerate(pt["visits"], start=1):
        temp = visit["vitals"]["temp"]
        hr = visit["vitals"]["heart_rate"]
        sbp = visit["vitals"]["systolic_bp"]
        dbp = visit["vitals"]["diastolic_bp"]
        symptoms = visit["symptoms"]
        wbc = visit["labs"]["wbc"]
        glucose = visit["labs"]["glucose"]

        alerts = []

        # --- Per-visit alerts ---
        if ((age < 60 and temp > 100) or (age >= 60 and temp > 99)):
            alerts.append("Fever")
        if hr > 100:
            alerts.append("High heart rate")
        if sbp > 140 or dbp > 90:
            alerts.append("High BP")
        elif sbp < 90 or dbp < 60:
            alerts.append("Low BP")
        if "chest pain" in visit["symptoms"]:
            alerts.append("Chest Pain Alert")
        if "shortness of breath" in visit["symptoms"]:
            alerts.append("Breathing Alert")
        if wbc > 11000:
            alerts.append("Possible Infection")
        if glucose > 200:
            alerts.append("High Blood Sugar")
            had_high_glucose = True
        if prev_sbp is not None and sbp - prev_sbp >= 20:
            alerts.append("BP Rising Trend")
            bp_rising_count += 1
        if prev_glucose is not None and glucose > prev_glucose:
            alerts.append("Glucose Increasing")
        if "Possible Infection" in alerts and "Fever" in alerts:
            had_infection_with_fever = True
        
        alerts_count += len(alerts)

        prev_sbp = sbp
        prev_glucose = glucose

        print(f"  Visit {visit_id}:")
        if alerts:
            for a in alerts:
                print(f"   - {a}")
        else:
            print("✅  Stable")

    # --- Summary per patient ---
    print(f"--- Summary for {name} ---")
    if had_high_glucose:
        print("  - Diabetes Concern")
    if bp_rising_count >= 2:
        print("  - Hypertension Trend")
    if had_infection_with_fever:
        print("  - Possible Infection with Fever")
    if not (had_high_glucose or bp_rising_count >= 2 or had_infection_with_fever):
        print("  No major long-term concerns detected.")
    print()  # blank line between patients

    alerts_count_for_all_patients[name] = alerts_count

max_alert_pt = max(alerts_count_for_all_patients, key=lambda p: alerts_count_for_all_patients[p])
print(f" --- Highest alert for patient: ---")
print(f"{max_alert_pt}: {alerts_count_for_all_patients[max_alert_pt]} alerts")




