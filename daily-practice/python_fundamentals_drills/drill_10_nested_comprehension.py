'''Drill 1 – Flattening
readings = [
    [98.6, 101.2],
    [99.5, 103.1],
    [97.8, 100.9]
]
Task A:
Create one flat list of all readings (no sublists).
Expected:[98.6, 101.2, 99.5, 103.1, 97.8, 100.9]
Task B
Create a list of readings above 100 using a nested comprehension + filter.'''
readings = [
    [98.6, 101.2],
    [99.5, 103.1],
    [97.8, 100.9]
]
# Task A
print([x for n in readings for x in n])
# Task B
print([x for n in readings for x in n if x > 100])

'''Drill 2 – Healthcare Nested Comprehension
patients = [
    {"name": "Ana", "temps": [98.6, 99.1], "hr": [72, 75], "o2": [97, 96]},
    {"name": "Ben", "temps": [101.2, 100.5], "hr": [110, 108], "o2": [94, 93]},
]
Create a flat list of alerts:
"Name: fever" if temp > 100
"Name: HR high" if hr > 100
"Name: O2 low" if o2 < 95
Use one nested comprehension — output should look like:
['Ben: fever', 'Ben: HR high', 'Ben: O2 low', ...]'''
patients = [
    {"name": "Ana", "temps": [98.6, 99.1], "hr": [72, 75], "o2": [97, 96]},
    {"name": "Ben", "temps": [101.2, 100.5], "hr": [110, 108], "o2": [94, 93]},
]
print([
    f"{pt['name']}: fever" for pt in patients for temp in pt['temps'] if temp > 100] +
    [f"{pt['name']}: HR high" for pt in patients for hr in pt['hr'] if hr > 100], 
    [f"{pt['name']}: O2 low" for pt in patients for o2 in pt['o2'] if o2 < 95])
