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

'''Drill 14 — Filter + Math + f-String
You’re analyzing patient temperatures in Fahrenheit:
temps = [98.6, 102.4, 99.1, 104.3, 97.9]
Task:
Write a single-line comprehension that:
Keeps only temps above 100
Converts each to Celsius ((F - 32) * 5/9)
Rounds to 1 decimal place
Formats them as strings like "Temp: 38.0°C"
Expected output:
['Temp: 39.1°C', 'Temp: 40.2°C']'''
print([f"Temp: {round((F - 32) * 5/9, 1)}°C" for F in temps if F > 100])

'''Drill 15 — Dual Filtering + f-Strings
You have two parallel patient data lists:
temps = [98.6, 101.3, 99.5, 103.2, 102.1]
o2_levels = [97, 95, 89, 92, 90]
Each temps[i] matches o2_levels[i] for the same patient.
Task:
Write a single-line comprehension that:
Keeps only patients with
temp > 100, and
o₂ < 94
Prints a formatted string:
"Alert: Temp 38.4°C, O₂ 89%"
(Convert temp to Celsius, rounded to 1 decimal)
Expected output:
['Alert: Temp 39.6°C, O₂ 89%', 'Alert: Temp 38.9°C, O₂ 90%']
Hint:
Use zip(temps, o2_levels) to iterate through both lists together.'''
temps = [98.6, 101.3, 99.5, 103.2, 102.1]
o2_levels = [97, 95, 89, 92, 90]
print([f"Alert: Temp {round((F - 32) * 5/9, 1)}°C, O2 {o2}" 
       for F, o2 in zip(temps, o2_levels) 
       if F >100 and o2 < 94])

'''Drill 16:
Zip Drill  — Basic pairing
names = ["Ana", "Ben", "Cara"]
temps = [98.6, 101.3, 99.5]
Task:
Use zip() in a one-line comprehension to create:
['Ana: 98.6', 'Ben: 101.3', 'Cara: 99.5']'''
names = ["Ana", "Ben", "Cara"]
temps = [98.6, 101.3, 99.5]
print([f'{name}: {temp}' for name, temp in zip(names, temps)])

'''Drill 17 — Add Conditional Logic
Same data:
names = ["Ana", "Ben", "Cara"]
temps = [98.6, 101.3, 99.5]
Task:
Use zip() + conditional comprehension to produce:
['Ana: Normal', 'Ben: Fever', 'Cara: Normal']
👉 "Fever" if temp > 100, else "Normal".
One clean line.'''
print([f"{name}: Fever" if temp > 100 
       else f"{name}: Normal" 
       for name, temp in zip(names, temps)])


'''Drill 18:triple zip + math + condition:
combine temperature, oxygen, and heart rate for 
each patient and generate a quick health alert summary.
🧩 Given:
names = ["Mia", "Sam", "Ana", "Leo"]
temps = [101.2, 98.6, 100.8, 99.5]
o2_levels = [93, 97, 89, 96]
hr = [110, 85, 102, 90]
🎯 Your task:
Write a comprehension that produces this kind of list:
['Mia: Fever, Low O2, High HR', 
 'Sam: Normal', 
 'Ana: Fever, Low O2, High HR', 
 'Leo: Normal']
Rules:
“Fever” if temp > 100
“Low O2” if o2 < 94
“High HR” if hr > 100
If none of the above, just show “Normal”.
Use zip(names, temps, o2_levels, hr) in one line. '''

names = ["Mia", "Sam", "Ana", "Leo"]
temps = [101.2, 98.6, 100.8, 99.5]
o2_levels = [93, 97, 89, 96]
hr = [110, 85, 102, 90]

temp_status = [filter(lambda temp: temp > 100, temps)]
o2_status = [filter(lambda o2: o2 < 94, o2_levels)]
hr_status = [filter(lambda h: h > 100, hr)]

print([f"{name}: Fever, Low O2, High HR" 
       if temp > 100 and o2 < 94 and h > 100 
       else f"{name}: Normal" 
       for name, temp, o2, h 
       in zip(names, temps, o2_levels, hr)])

