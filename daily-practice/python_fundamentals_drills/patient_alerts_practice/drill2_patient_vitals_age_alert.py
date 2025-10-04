'''Drill 2:
Patient Vitals with Age Consideration
You have a list of patients. Each patient has:
name, age, vitals: temp, heart_rate
Alert rules:
Fever:
Age < 60 → temp > 100
Age ≥ 60 → temp > 99
High heart rate:
Any age → heart_rate > 100
Task:
Loop through each patient.
Collect all applicable alerts in a list.
Print:
ALERT for [name]: Fever, High Heart Rate
Or if no alerts:
[name] is stable
Starter Data
patients = [
    {"name": "Alice", "age": 70, "vitals": {"temp": 101.2, "heart_rate": 95}},
    {"name": "Bob", "age": 55, "vitals": {"temp": 100.5, "heart_rate": 105}},
    {"name": "Charlie", "age": 40, "vitals": {"temp": 98.7, "heart_rate": 80}},
    {"name": "David", "age": 65, "vitals": {"temp": 99.5, "heart_rate": 102}}
]
💡 Hints:
Use a list alerts = [] for each patient.
Add "Fever" or "High Heart Rate" as conditions are met.
Join the list with ", ".join(alerts) when printing.'''

patients = [
    {"name": "Alice", "age": 70, "vitals": {"temp": 101.2, "heart_rate": 95}},
    {"name": "Bob", "age": 55, "vitals": {"temp": 100.5, "heart_rate": 105}},
    {"name": "Charlie", "age": 40, "vitals": {"temp": 98.7, "heart_rate": 80}},
    {"name": "David", "age": 65, "vitals": {"temp": 99.5, "heart_rate": 102}}
]

#Loop through each patient. Collect all applicable alerts in a list.
for pt in patients:
    # collect all applicable alerts in a list
    alerts = []
    # Fever: Age < 60 → temp > 100 or Age ≥ 60 → temp > 99
    if ((pt["age"] < 60 and pt["vitals"]["temp"] > 100) or
        (pt["age"] >= 60 and pt["vitals"]["temp"] > 99)):
        alerts.append("Fever")
    # High heart rate:Any age → heart_rate > 100
    if pt["vitals"]["heart_rate"] > 100:
        alerts.append("High heart rate")

    # Print: ALERT for [name]: Fever, High Heart Rate Or if no alerts: [name] is stable
    if alerts:
        print(f"ALERT for {pt['name']}: {', '.join(alerts)}")
    else:
        print(f"{pt['name']} is stable")

    


