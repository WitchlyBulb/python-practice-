'''Drill 1:
temps = [98.6, 101.2, 99.5, 103.1]
Task A (List comprehension):
Create a list where each temperature is labeled "fever" if above 100, otherwise "normal".
Task B (Dict comprehension):
Create a dictionary where the patient number (1,2,3,4) is the key, and the value is "fever" or "normal" according to the temperature.
'''

temps = [98.6, 101.2, 99.5, 103.1]
# Task A
print(["fever" if temp > 100 else "normal" for temp in temps])
# Task B
print({f"{i+1}": "fever" if temp > 100 else "normal" for i, temp in enumerate(temps)})

'''Drill 2:
temps = [98.6, 101.2, 99.5, 103.1]
names = ["Ana", "Ben", "Cara", "Dan"]
Task A (List comprehension):
Create a list of strings like "Ana: normal", "Ben: fever", etc.
Task B (Dict comprehension):
Create a dictionary mapping each name → status ("fever" or "normal").
'''

temps = [98.6, 101.2, 99.5, 103.1]
names = ["Ana", "Ben", "Cara", "Dan"]
# Task A:
print([f"{name}: {'fever' if temp > 100 else 'normal'}" 
       for name, temp in zip(names, temps)])
# Task B:
print({name:'fever' if temp > 100 else 'normal' for name, temp in zip(names, temps)})

'''
Drill 3 (Reinforcement & variation)
You’re given:
names = ["Ana", "Ben", "Cara", "Dan"]
temps = [98.6, 101.2, 99.5, 103.1]
heart_rates = [72, 110, 80, 120]
Task A:
Make a list like:
["Ana: normal, HR=72", "Ben: fever, HR=110", ...]
Task B:
Make a dictionary where:
Key = patient name
Value = "critical" if both temp > 102 and hr > 100
otherwise "stable"'''

names = ["Ana", "Ben", "Cara", "Dan"]
temps = [98.6, 101.2, 99.5, 103.1]
heart_rates = [72, 110, 80, 120]
# Task A:
print([f"{name}: {'fever' if temp > 100 else 'normal'}, HR={hr}" 
       for name, temp, hr in zip(names, temps, heart_rates)])
#Task B:
print({name: 'critical' if temp > 102 and hr > 100 else 'stable' 
       for name, temp, hr in zip(names, temps, heart_rates)})

'''
patients = [
    {"name": "Ana", "temp": 98.6, "hr": 72},
    {"name": "Ben", "temp": 101.2, "hr": 110},
    {"name": "Cara", "temp": 99.5, "hr": 80},
    {"name": "Dan", "temp": 103.1, "hr": 120},
]
Task A:
Using a list comprehension, extract the names of patients whose temp > 100.
Task B:
Using a dict comprehension, create:
{name: "alert" if hr > 100 else "ok"}
—but only for patients whose temp > 100 (so: a comprehension with a filter clause).
'''
patients = [
    {"name": "Ana", "temp": 98.6, "hr": 72},
    {"name": "Ben", "temp": 101.2, "hr": 110},
    {"name": "Cara", "temp": 99.5, "hr": 80},
    {"name": "Dan", "temp": 103.1, "hr": 120},
]
# Task A:
print([pt["name"] for pt in patients if pt["temp"] > 100])
# Task B:
print({pt["name"]: "alert" if pt["hr"] > 100 else "ok" for pt in patients})

'''
patients = [
    {"name": "Ana", "temp": 98.6, "hr": 72, "o2": 97},
    {"name": "Ben", "temp": 101.2, "hr": 110, "o2": 94},
    {"name": "Cara", "temp": 99.5, "hr": 80, "o2": 98},
    {"name": "Dan", "temp": 103.1, "hr": 120, "o2": 91},
]
Task A (List comprehension):Create a list of summary strings like:
["Ben: fever, HR=110, O2=94", "Dan: fever, HR=120, O2=91"]
👉 Only include patients whose temp > 100.
Task B (Dict comprehension):
Create a dictionary where:
Key = patient name
Value = "critical" if O₂ < 95 and HR > 100, otherwise "stable"
Include all patients (no filtering here).
'''
patients = [
    {"name": "Ana", "temp": 98.6, "hr": 72, "o2": 97},
    {"name": "Ben", "temp": 101.2, "hr": 110, "o2": 94},
    {"name": "Cara", "temp": 99.5, "hr": 80, "o2": 98},
    {"name": "Dan", "temp": 103.1, "hr": 120, "o2": 91}
]
# Task A
print([f"{pt['name']}: {'fever' if pt['temp'] > 100 else 'normal'}, HR={pt['hr']}, O2={pt['o2']}" 
       for pt in patients if pt['temp'] > 100])

# Task B
print({pt['name']: "critical" 
       if pt['o2'] < 95 and pt['hr'] > 100 
       else "stable" 
       for pt in patients})
