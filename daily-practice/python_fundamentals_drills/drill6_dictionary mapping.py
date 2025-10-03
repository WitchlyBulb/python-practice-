'''Beginner Drill1: Create a dictionary patients that maps patient 
names to their ages:
Patient	Age
Mia	    72
Liam	65
Noah	50
Then, print each patient’s age in the format:
Mia is 72 years old
Instructions:
Create the dictionary.
Use a loop to print the statement for each patient.'''

patients = {"Mia": 72, "Liam": 65, "Noah": 50}
for patient in patients:
    print(f"{patient} is {patients[patient]} years old")

'''Beginner Drill 2 – Adding/Updating Dictionary
Task: Add a new patient "Emma" with age 40.
Update "Noah"’s age to 51.
Print all patient names with their updated ages in the 
same format as before.'''

patients["Emma"] = 40
patients["Noah"] = 51
for patient, age in patients.items():
    print(f"{patient} is {age} years old")
'''Intermediate Drill 1 – Age-Based Risk Mapping
Task:
Create a new dictionary patient_risk that maps each 
patient to a risk category based on age:
Age > 70 → "high"
Age 50–70 → "medium"
Age < 50 → "low"
Then print each patient and their risk like:
Mia: high
Liam: medium
Noah: medium
Emma: low
Use the current patients dictionary we have.'''

patient_risk = {}

for patient, age in patients.items():
    if age > 70:
        patient_risk[patient] = "high"
    elif age >= 50:
        patient_risk[patient] = "medium"
    else:
        patient_risk[patient] = "low"
    
for patient, risk in patient_risk.items():
    print(f"{patient}: {risk}")

'''Intermediate Drill 2 – Function-Based Mapping
Task:
Define a function risk_level(age) that returns:
"high" if age > 70
"medium" if 50 ≤ age ≤ 70
"low" if age < 50
Use dictionary comprehension to create patient_risk2 
mapping each patient to their risk using this function.
Print each patient and their risk.'''

def risk_level(age: int) -> str:
    if age > 70:
        return "high"
    elif age >= 50:
        return "medium"
    else:
        return "low"

patient_risk2 = {f"{patient}": risk_level(age) for patient, age in patients.items()}
for patient, risk in patient_risk2.items():
    print(f"{patient}: {risk}")


'''Advanced Drill 1 – Mapping with Conditions and enumerate()
Task:
You have a list of patient temperatures:
temps = [98.6, 101.2, 99.5, 103.1]
Create a dictionary mapping each patient number (Patient1, Patient2, …) 
to their temperature status:
temp > 102 → "critical"
temp > 100 → "fever"
else → "normal"
Print each patient and status like:
Patient1: normal
Patient2: fever
Patient3: normal
Patient4: critical
Use dictionary comprehension and enumerate.
'''

temps = [98.6, 101.2, 99.5, 103.1]

def temp_status(temp: float) -> str:
    if temp > 102:
        return "critical"
    elif temp > 100:
        return "fever"
    else:
        return "normal"
    
temp_statuses = {f"Patient{i+1}": temp_status(temp) for i, temp in enumerate(temps)}
for pt, status in temp_statuses.items():
    print(f"{pt}: {status}")

'''Advanced Drill 2 – Nested Dictionary Mapping
Scenario:
We have two lists of patient data:
temps = [98.6, 101.2, 99.5, 103.1]
heart_rates = [72, 110, 88, 130]
We want to create a nested dictionary like this:
{
  "Patient1": {"temp": "normal", "heart_rate": "normal"},
  "Patient2": {"temp": "fever", "heart_rate": "high"},
  "Patient3": {"temp": "normal", "heart_rate": "normal"},
  "Patient4": {"temp": "critical", "heart_rate": "high"}
}
Rules for classification:
Temperature
102 → "critical"
100 → "fever"
else → "normal"
Heart Rate
100 → "high"
else → "normal"
Task
Write two functions:
temp_status(temp)
hr_status(hr)
Use dictionary comprehension with enumerate to build the nested dictionary.
Print results in a neat format like:
Patient1 → Temp: normal, Heart Rate: normal
Patient2 → Temp: fever, Heart Rate: high'''

def temp_status(temp: float) -> str:
    if temp > 102.0:
        return "critical"
    elif temp > 100.0:
        return "fever"
    else:
        return "normal"
    
def hr_status(hr: int) -> str:
    if hr > 100:
        return "high"
    else:
        return "normal"

temps = [98.6, 101.2, 99.5, 103.1]
heart_rates = [72, 110, 88, 130]
 
patient_vitals = {
    f"Patient{i+1}": {
        "temp": temp_status(temp),
        "heart_rate": hr_status(hr)
    }
    for i, (temp, hr) in enumerate(zip(temps, heart_rates))
}

for pt, vitals in patient_vitals.items():
    print(f"{pt} → Temp: {vitals['temp']}, Heart Rate: {vitals['heart_rate']}")



