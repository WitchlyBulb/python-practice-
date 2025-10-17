''' Drill 1 (dot vs backslash-dot)
text = "File versions: v1.0, v1a0, v2.5, v3b7"
Use regex to find only the ones that have a real dot (like v1.0, v2.5).
Then, a second regex to find any version that has any character 
between numbers (so it catches v1.0, v1a0, v2.5, v3b7).'''

import re

text = "File versions: v1.0, v1a0, v2.5, v3b7"
print(re.findall(r"\.", text))
print(re.findall(r".", text))

'''Drill 2:
text = "BP 120/80, HR 72, Temp 99"
Extract all numbers (both systolic, diastolic, 
HR, Temp) using regex and re.findall().'''

import re

text = "BP 120/80, HR 72, Temp 99"
print(re.findall(r"\d+\.\d+", text)) # find any floats in temp
print(re.findall(r"\d+", text)) # find any integers in HR, temp and BP

'''Drill 3:
Extract all vital signs
note = "Patient A: BP 120/80, HR 72, Temp 98.6°F; Patient B: BP 130/85, HR 68, Temp 101.2°F"
Using one re.findall(), extract all numbers for BP, HR, and Temp:
BP numbers like 120/80, 130/85
HR numbers like 72, 68
Temp numbers like 98.6, 101.2
Hint: You will need a pattern that matches either digits, digits with a dot, or digits with a slash.
'''

import re

note = "Patient A: BP 120/80, HR 72, Temp 98.6°F; Patient B: BP 130/85, HR 68, Temp 101.2°F"
pattern = r"\d+.\d+"
matches = re.findall(pattern, note)
print(matches)

'''Drill 4:
Safely extract BP, HR, and Temp
note = "Patient A: BP 120/80, HR 72, Temp 98.6°F; Patient B: BP 130/85, HR 68, Temp 101.2°F"
Use one re.findall() to extract:
BP numbers like 120/80, 130/85 → digits + / + digits
Temp numbers like 98.6, 101.2 → digits + literal decimal + digits
HR numbers like 72, 68 → integers
'''

import re

pattern = r"\d+/\d+|\d+\.\d+|\d+"
matches = re.findall(pattern, note)
print(matches)

'''
Drill #4 — Extract vitals + dates + IDs
Use one re.findall() to extract all:
Patient IDs → a single letter followed by digits (A123, B456)
Dates → YYYY-MM-DD format (2025-10-13)
BP → digits + slash + digits (120/80, 130/85)
Temp → digits + decimal + digits (98.6, 101.2)
HR → integers (72, 68)
Hint: Combine multiple patterns with |. Order matters — put more specific patterns first.
'''

note = """
Patient ID: A123, Date: 2025-10-13, BP 120/80, HR 72, Temp 98.6°F
Patient ID: B456, Date: 2025-10-12, BP 130/85, HR 68, Temp 101.2°F
"""
import re

print(re.findall(r"\w\d+|\d{4}-\d{2}-\d{2}|\d+/\d+|\d+\.\d+|\d+", note))

'''Drill 5
Use one re.findall() to extract:
Patient IDs → a letter + digits (A123, B456, C789)
Times → HH:MM format (08:30, 14:45, 09:15)
BP → digits + slash + digits (120/80, 130/85, 110/70)
Temp → digits + decimal + digits (98.6, 101.2, 99.1)
HR → integers (72, 68, 75)
'''

import re

log = """
Patient ID: A123, Time: 08:30, BP 120/80, HR 72, Temp 98.6°F
Patient ID: B456, Time: 14:45, BP 130/85, HR 68, Temp 101.2°F
Patient ID: C789, Time: 09:15, BP 110/70, HR 75, Temp 99.1°F
"""
print(re.findall(r"\d+/\d+|\d+\.\d+|\d{2}:\d{2}|[A-Z]\d+|\d+", log))

'''Regex Drill 6 — Simple character class
import re
text = "BP120 HR72 Temp98.6"
print(re.findall(r"\w+\s*\d+", text))
predict what matches you’ll get
'''

# Output --> ['BP120', 'HR72', 'Temp98']

'''
Regex Drill 7 — Extend the pattern
Can you now modify the pattern so it also 
captures decimals like Temp98.6 completely?
👉 Fill this in:
pattern = r"_____"
print(re.findall(pattern, text))
'''
#"\w+\d+\.\d|\w+\s*\d+"

'''Regex Drill 8:
Regex Refresher (alternation + priority)
import re
note = "Patient A: BP120/80 HR72 Temp98.6°F O2 95%"
pattern = r"\d+/\d+|\d+\.\d+|\d+"
print(re.findall(pattern, note))
Predict the output exactly
'''
#Output ['120/80', '98.6', '72', '95']

