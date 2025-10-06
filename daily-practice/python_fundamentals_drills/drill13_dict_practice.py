# 1. Create a dictionary for a patient: name: "Clara", HR: 88, Temp: 99.5
#    Print the temperature using f-string formatting.
patient = {"name": "Clara", "HR": 88, "Temp": 99.5} print(f"{patient['name']}'s HR: {patient['HR']}")


# 2. Try to print the "BP" key. If it doesn't exist, print: "No BP recorded"
#    Do it in one line using print(... if ... else ...).
print(patient.get("BP", "No BP recorded"))

# 3. Update Clara's Temp to 101.2 and add "O2": 94 in a single update() call.
patient.update({"Temp": 101.2, "O2": 94}) print(patient)

# 4. From the dictionary below, make a new dictionary that only contains
#    vitals above 95.
vitals = {"HR": 88, "BP": 110, "Temp": 101.2, "O2": 94}
high_vitals = {x:y for x,y in vitals.items() if y > 95} print(high_vitals)

# 5. From this hospital dictionary, print "Room2's patient: Charlie"
hospital = {
    "Room1": {"name": "Anna", "HR": 90},
    "Room2": {"name": "Charlie", "HR": 76}
}
print(hospital["Room2"]["name"])

# 6. From the vitals dict, print the key with the **highest** value.
vitals = {"HR": 88, "BP": 110, "Temp": 101.2, "O2": 94} print(max(vitals, key=vitals.get))
print(max(vitals, key=vitals.get))

# 7. From the nested hospital dict below, find which patient has the **highest BP**.
hospital = {
    "Room1": {"name": "Alice", "HR": 85, "BP": 130},
    "Room2": {"name": "Bob", "HR": 78, "BP": 140}
}
bp_values = [] for x, y in hospital.items(): bp_values.append(y["BP"]) max_bp = max(bp_values) for y in hospital.values(): if y["BP"] == max_bp: print(y["name"])

# 8. Create a new dictionary from hospital where keys are room numbers
#    and values are only the HR values.
hospital = { "Room1": {"name": "Alice", "HR": 85, "BP": 130}, "Room2": {"name": "Bob", "HR": 78, "BP": 140} } bp_values = [] for x, y in hospital.items(): bp_values.append(y["BP"]) max_bp = max(bp_values) for y in hospital.values(): if y["BP"] == max_bp: print(y["name"])
new_dict = {} for x, y in hospital.items(): new_dict.update({x: y["HR"]}) print(new_dict)

# 9. Remove the "Temp" key from vitals safely (no error if missing).
vitals = {"HR": 88, "BP": 110, "Temp": 101.2, "O2": 94} if vitals["Temp"]: del vitals["Temp"] else: print("no error") print(vitals)

# 10. Check if "Room3" exists in hospital. If not, add it with:
# name:"Diana", HR: 82, BP: 125.
hospital = { "Room1": {"name": "Alice", "HR": 85, "BP": 130}, "Room2": {"name": "Bob", "HR": 78, "BP": 140} } hospital.get("Room3"), hospital.update({"Room3": {"name": "Diana", "HR": 82, "BP": 125}}) print(hospital)