# Use map + lambda to convert this list of temps into 
# labels "Fever" (≥ 100.4) or "OK" (< 100.4). 
# Assign the result to label_temps and print it.
# temps = [98.6, 101.2, 99.5, 100.4, 102.1]

temps = [98.6, 101.2, 99.5, 100.4, 102.1]
label_temps = list(map(lambda temp: "Fever" if temp >= 100.4 else "OK", temps))
print(label_temps)

# --------------------------------------------------------------------
# --------------------------------------------------------------------

# Drill 2 — using sorted + key (intro level)
# We’ll now use lambda inside sorted.
# patients = ["Zara", "Mohammed", "Aisha", "John"]

patients = ["Zara", "Mohammed", "Aisha", "John"]
sorted_patients = sorted(patients, key=lambda pt: pt[0])
print(sorted_patients)

# --------------------------------------------------------------------
# --------------------------------------------------------------------

# Drill 3: What would happen if we changed the key to pt[-1] instead 
#of pt[0]
patients = ["Zara", "Mohammed", "Aisha", "John"]
sorted_patients = sorted(patients, key=lambda pt: pt[-1])
print(sorted_patients)
# --> ['Zara', 'Aisha', 'Mohammed', 'John']

# --------------------------------------------------------------------
# --------------------------------------------------------------------

#Drill4:
# patients = [("Zara", 25), ("Mohammed", 40), ("Aisha", 30), ("John", 20)]
# 👉 Task: Sort this list by age first, and if ages 
# are the same, then by name alphabetically.

patients = [("Zara", 25), ("Mohammed", 40), ("Aisha", 30), ("John", 20)]
sorted_patients = sorted(patients, key=lambda pt: (pt[1],pt[0]))
print(sorted_patients)

# --------------------------------------------------------------------
# --------------------------------------------------------------------

# Drill 5: Using the same list of patients, sort them by name length, 
# and if two names have the same length, sort by age.

sort_by_len_and_age = sorted(patients, key=lambda pt: (len(pt[0]), pt[1]))
print(sort_by_len_and_age)

# --------------------------------------------------------------------
# --------------------------------------------------------------------

# Drill 6: vitals = {"Alice": 98, "Bob": 102, "Charlie": 99}
# Find the patient with the highest temperature using max and a lambda.

vitals = {"Alice": 98, "Bob": 102, "Charlie": 99}
max_temp = max(vitals, key=lambda pt: vitals[pt])
print(max_temp)

# --------------------------------------------------------------------
# --------------------------------------------------------------------

# Drill 7: 
# patients = [("Zara", 25), ("Mohammed", 40), ("Aisha", 30), ("John", 20)]
# Task: Find the **oldest patient** (max age) using max + lambda
# Only write the line that finds and prints the patient

patients = [("Zara", 25), ("Mohammed", 40), ("Aisha", 30), ("John", 20)]
print(max(patients, key=lambda pt: pt[1]))

# --------------------------------------------------------------------
# --------------------------------------------------------------------

# Drill 8:
# vitals = {"Alice": 98, "Bob": 102, "Charlie": 99}
# Task: Find the patient with the **lowest temperature** using min + lambda
# Just write the line that finds and prints the patient

vitals = {"Alice": 98, "Bob": 102, "Charlie": 99}
print(min(vitals, key=lambda pt: vitals[pt]))

# --------------------------------------------------------------------
# --------------------------------------------------------------------

#Drill 9
# 1. Filter patients with temp >= 100
# 2. Sort by heart rate ascending
# 3. Extract just the names into a list
# Write a single expression using filter + sorted + map + lambda

patients = [
    {"name": "Alice", "temp": 98, "hr": 80},
    {"name": "Bob", "temp": 102, "hr": 110},
    {"name": "Charlie", "temp": 99, "hr": 95},
    {"name": "David", "temp": 102, "hr": 120},
]

print(
    list(
        map(
            lambda pt: pt["name"], 
            sorted(
                    filter(lambda pt: pt["temp"] >= 100, patients), 
                    key=lambda pt: pt["hr"]
                )
            )
        )
)



# --------------------------------------------------------------------
# --------------------------------------------------------------------

# Drill 10:
# Task: 
# 1. Filter patients with hr >= 100
# 2. Sort by temperature ascending
# 3. Return a list of names
# Hint: Use a list comprehension like the clean one-liner

patients = [
    {"name": "Alice", "temp": 98, "hr": 80},
    {"name": "Bob", "temp": 102, "hr": 110},
    {"name": "Charlie", "temp": 99, "hr": 95},
    {"name": "David", "temp": 102, "hr": 120},
]
print([
    pt["name"] 
    for pt in sorted(
        filter(lambda pt: pt["hr"] >= 100, patients), 
        key=lambda pt: pt["temp"]
        )
        ])

# --------------------------------------------------------------------
# --------------------------------------------------------------------

# Drill 11:
# Using the same patients list:
# Task:
# 1. Filter patients with temp >= 100
# 2. Sort by heart rate descending
# 3. If heart rate is equal, sort by name ascending
# 4. Return a list of names in a single clean one-liner

print([
    pt["name"] 
    for pt in sorted(
        filter(lambda pt: pt["temp"] >= 100, patients), 
        key=lambda pt: (-pt["hr"], pt["name"])
        )
        ])

# --------------------------------------------------------------------
# --------------------------------------------------------------------

# Drill 12: Patients with temp and hr
# Task:
# 1. Filter patients with temp >= 100
# 2. Compute risk = temp*0.6 + hr*0.4 for sorting
# 3. Sort by risk descending
# 4. Return a list of "Name: Risk" (rounded to 1 decimal) in a clean one-liner

patients = [
    {"name": "Alice", "temp": 98, "hr": 80},
    {"name": "Bob", "temp": 101, "hr": 110},
    {"name": "Charlie", "temp": 99, "hr": 95},
    {"name": "David", "temp": 102, "hr": 120},
]

print([
    f"{pt['name']}: {round(pt['temp']*0.6 + pt['hr']*0.4, 1)}"
    for pt in sorted(
        filter(lambda pt: pt["temp"] > 100, patients),
        key=lambda pt: pt["temp"]*0.6 + pt["hr"]*0.4,
        reverse=True
    )
])

# --------------------------------------------------------------------
# --------------------------------------------------------------------

# Drill 13 — Risk Score by Temp + HR
# Task:
# 1. Filter patients with HR >= 100
# 2. Compute risk = temp*0.5 + hr*0.5
# 3. Sort by risk descending
# 4. Return a list of "Name: Risk" rounded to 1 decimal

print([f"{pt['name']} : {round((pt['temp'] * 0.5 + pt['hr'] * 0.5), 1)}"
    for pt in sorted(
        filter(lambda pt: pt["hr"] > 100, patients), 
        key=lambda pt: pt["temp"] * 0.5 + pt["hr"] * 0.5, 
        reverse=True)])

# --------------------------------------------------------------------
# --------------------------------------------------------------------

# Drill 14 — Risk Score with Temp & HR, ascending
# Same patients list
# Task:
# 1. Filter patients with temp >= 100
# 2. Compute risk = temp*0.7 + hr*0.3
# 3. Sort by risk ascending
# 4. Return a list of "Name: Risk" rounded to 1 decimal

print([f"{pt['name']}: {round(pt['temp'] * 0.7 + pt['hr'] * 0.3, 1)}" 
      for pt in sorted(
          filter(lambda pt: pt["temp"] >= 100, patients), 
          key=lambda pt: (pt["temp"] * 0.7 + pt["hr"] * 0.3))])

# --------------------------------------------------------------------
# --------------------------------------------------------------------

# Drill 15 — Dual Key Sort + Risk
# Same patients list
# Task:
# 1. Filter patients with temp >= 100
# 2. Compute risk = temp*0.6 + hr*0.4
# 3. Sort by risk descending, then by name ascending if risk ties
# 4. Return a list of "Name: Risk" rounded to 1 decimal
# Try writing this one-liner — this combines multi-level sort + computed risk + clean output.

print([f"{pt['name']}: {round(pt['temp'] * 0.6 + pt['hr'] * 0.4, 1)}" 
       for pt in sorted(
        filter(lambda pt: pt['temp'] >= 100, patients), 
        key=lambda pt: (-(pt['temp'] * 0.6 + pt['hr'] * 0.4), pt['name'])
       )
    ])
