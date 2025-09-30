'''Patient BP & Temp Alerts
You have a list of patients. Each patient has:
name, vitals with temp, systolic_bp, diastolic_bp
Rules for alerts:
Temp > 100 → "Fever"
Systolic BP > 140 → "High BP"
Diastolic BP < 60 → "Low BP"
Task:
Loop through each patient.
Collect all applicable alerts in a list.
Print alerts as:
ALERT for [name]: Fever, High BP
Or print
[name] is stable
if no alerts.
Starter Data:
patients = [
    {"name": "Anna", "vitals": {"temp": 99.5, "systolic_bp": 145, "diastolic_bp": 82}},
    {"name": "Ben", "vitals": {"temp": 101.3, "systolic_bp": 130, "diastolic_bp": 58}},
    {"name": "Cara", "vitals": {"temp": 98.7, "systolic_bp": 118, "diastolic_bp": 76}}
👉 Your turn: Write the code for this drill.
(Hint: It’s the same pattern as the fever/heart rate one — just with 3 conditions instead of 2.)'''

patients = [
    {"name": "Anna", "vitals": {"temp": 99.5, "systolic_bp": 145, "diastolic_bp": 82}},
    {"name": "Ben", "vitals": {"temp": 101.3, "systolic_bp": 130, "diastolic_bp": 58}},
    {"name": "Cara", "vitals": {"temp": 98.7, "systolic_bp": 118, "diastolic_bp": 76}},
    {"name": "David", "vitals": {"temp": 102, "systolic_bp": 150, "diastolic_bp": 55}}
]
for pt in patients:
    alerts = []
    if pt["vitals"]["temp"] > 100:
        alerts.append("Fever")
    if pt["vitals"]["systolic_bp"] > 140:
        alerts.append("High BP")
    if pt["vitals"]["diastolic_bp"] < 60:
        alerts.append("Low BP")

    if alerts:
        print(f"ALERT for {pt['name']}: {', '.join(alerts)}")
    else:
        print(f"{pt['name']} is stable")
