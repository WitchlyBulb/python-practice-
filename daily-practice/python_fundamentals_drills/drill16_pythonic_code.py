'''Drill 1:
Turn the following multi-line code into one line using comprehension:
oxygen_levels = [96, 88, 91, 99]
status = []
for o2 in oxygen_levels:
    if o2 < 92:
        status.append("Low O₂")
    else:
        status.append("Normal")
print(status)'''

print(["Low O₂" if o2 < 92 else "Normal" for o2 in [96, 88, 91, 99]])

'''Drill 2:
temps = [98.6, 101.2, 99.5, 103.1]
Write one line that creates a list of only the temperatures greater than 100.
Output should look like:
[101.2, 103.1]'''

temps = [98.6, 101.2, 99.5, 103.1]
print([temp for temp in temps if temp > 100])
#OR
print([temp for temp in [98.6, 101.2, 99.5, 103.1] if temp > 100])

'''Drill3
Given:
temps = [98.6, 101.2, 99.5, 103.1]
Write a single-line comprehension that produces this list:
['normal', 'fever', 'normal', 'fever']
'''
temps = [98.6, 101.2, 99.5, 103.1]
print(["fever" if temp > 100 else "normal" for temp in temps ])

'''Drill4
Given:
heart_rates = [72, 105, 98, 120, 88]
Write a single line comprehension that:
Keeps only heart rates over 100
Converts them to the string "High HR"
✅ Expected output:
['High HR', 'High HR']
'''
heart_rates = [72, 105, 98, 120, 88]

'''Drill 5: Filtering vs Conditional Expression
You only want to keep patient temperatures that show fever.
temps = [98.6, 101.2, 99.5, 103.1, 97.9]
👉 Write a one-liner that returns only temps greater than 100.
✅ Expected output:
[101.2, 103.1]'''

temps = [98.6, 101.2, 99.5, 103.1, 97.9]
print([temp for temp in temps if temp > 100])

'''Drill 6:
Conditional expression comprehension
Now you want to label each temperature:
"fever" if > 100
"normal" otherwise
✅ Expected output:
['normal', 'fever', 'normal', 'fever', 'normal']
'''
print(["fever" if temp > 100 else "normal" for temp in temps])

'''Drill 7
Filtering comprehension
You have the oxygen levels of several patients:
o2_levels = [98, 90, 92, 88, 97]
Task: Write a one-liner to return only the low O₂ levels (< 92).
✅ Expected output:
[90, 88]
Focus on skipping all others.
'''
o2_levels = [98, 90, 92, 88, 97]
print([o2 for o2 in o2_levels if o2 < 92])

'''Drill 8:
Conditional expression comprehension
Same oxygen levels:
o2_levels = [98, 90, 92, 88, 97]
Task: Label each level as:
"Low" if < 92
"Normal" otherwise
✅ Expected output:
['Normal', 'Low', 'Normal', 'Low', 'Normal']'''

print(["Low" if o2 < 92 else "Normal" for o2 in o2_levels])

'''Drill 9:
You have patient heart rates:
heart_rates = [72, 105, 98, 120, 88]
Task:
Keep only heart rates over 100
Convert them to the string "High HR"
✅ Expected output:
['High HR', 'High HR']
'''
heart_rates = [72, 105, 98, 120, 88]
print(['High HR' for hr in heart_rates if hr > 100])

'''Drill 10:
Conditional Expression + Full List
Let’s test labeling everything — no skips this time.
Same heart rates:
Task:
Label each heart rate as:
"High HR" if > 100
"Normal" otherwise
✅ Expected output:
['Normal', 'High HR', 'Normal', 'High HR', 'Normal']
Single-line, using conditional expression comprehension.
'''
print(["High HR" if hr > 100 else "Normal" for hr in heart_rates])

'''Drill 11
You have patient temperatures:
temps = [98.6, 101.2, 99.5, 103.1, 100.5]
Task:
Keep only temperatures above 100
Convert them to "Fever"
Skip anything ≤ 100
✅ Expected output:
['Fever', 'Fever', 'Fever']
'''
temps = [98.6, 101.2, 99.5, 103.1, 100.5]
print(["Fever" for temp in temps if temp > 100])

'''Drill 12:
Drill 6 — Harder Mix
Now we combine filtering, transformation, and inline math.
Patient temperatures (in Fahrenheit):
temps = [98.6, 101.2, 99.5, 103.1]
Task:
Keep only temps > 100
Convert them to Celsius using the formula: (F - 32) * 5/9
✅ Expected output (rounded to 1 decimal):
[38.4, 39.5]'''
temps = [98.6, 101.2, 99.5, 103.1]
print([round((F - 32) * 5/9, 1) for F in temps if F > 100])

'''Drill 13:
Label temperatures as “Fever” or “Normal”, but also convert to Celsius for temps > 100.
temps = [98.6, 101.2, 99.5, 103.1]
Task:
If temp > 100 → "Fever: X°C" (rounded)
Else → "Normal"
Single-line comprehension
✅ Expected output:
['Normal', 'Fever: 38.4°C', 'Normal', 'Fever: 39.5°C']
This combines conditional expression + transformation in one line.
'''
print([f"Fever: {round((F - 32) * 5/9, 1)}°C" if F > 100 else "Normal" for F in temps])
