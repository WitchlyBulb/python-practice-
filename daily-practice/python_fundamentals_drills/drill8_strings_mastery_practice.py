
# Drill 1: s = "Hello, World!"
# a) Get "World"
s = "Hello, World!"
print(s[-6:-1])

# b) Get "Hello"
print(s[:5])

# c) Get "!"
print(s[-1])

# Drill 2: s = "abcdefghij" → get every 3rd character 
# starting at index 1 ("beh...")
s = "abcdefghij"
result = ""
for i in range(1, len(s), 3):
    result += s[i]
print(result)

# drill3   — s = "a1b2c3d4e5" → extract "12345" using slicing only.
s = "a1b2c3d4e5"
nums = s[1:2] + s[3:4] + s[5:6] + s[7:8] + s[9:10]
print(nums)

# Drill 4 — Explain / show how to reverse a string and then 
# how to take every second char from the reversed string.
reverse_s = s[::-1]
print(reverse_s)
every_second_char = ''
for i in range(1, len(s), 2):
    every_second_char += reverse_s[i]
print(every_second_char)

# Drill 5 - Using str.format() produce: "Alice is 30 years old." from name = "Alice", age = 30.
print("{name} is {age} years old.".format(name="Alice", age=30))

# Drill 5 - Using f-strings only:
#x = 7
#  Format x so that it prints inside a field width 5.
x = 7
print(f"{x:5}")

# Drill 6 - (alignment)
#word = "Hi"
#  Print "Hi" centered in a field of width 6.
word = "Hi"
print(f"{word:^6}")

# Drill 7- (width + decimals)
# pi = 3.14159265
#  Print pi with width 10 and 2 decimal places.
pi = 3.14159265
print(f"{pi:10.2f}")

# Drill 8: Format pi as center-aligned, width 10, 2 decimals.
print(f"{pi:^10.2f}")

# Drill 9:
# Print x right-aligned in width 6.(Expected: " 42").
# Print pi left-aligned in width 8, with 3 decimals.(Expected: "3.142 ")
# Print word centered in width 7.(Expected: " OK ").
x = 42
pi = 3.14159
word = "OK"

print(f"{x:6}")
print(f"{pi:<8.3f}")
print(f"{word:^7}")

# Drill 10: Signs and separators
# n = 1234567.89
# Format n so it prints as: +1,234,567.89
n = 1234567.89
print(f"{n:+,.2f}")

# Drill 11: value = 0.256
# Format value as: 25.6%
value = 0.256
print(f"{value:.1%}")

# Drill 12: Inline Expression
#score = 0.893
# Using an f-string, print: 0.89 (89.3%)
# Round score to 2 decimals for the first number
# Show score as percentage with 1 decimal in parentheses

score = 0.893
print(f"{score:.2f} ({score:.1%})")

# Drill 13: text = "a1b2c3d4"
# Use re.findall to extract all digits as a list.
text = "a1b2c3d4"
import re
print(re.findall(r"\d", text))

# Drill 14- text = "item12price34tax5"
# Use regex to extract all full numbers (12, 34, 5) as a list.
text = "item12price34tax5"
import re
print(re.findall(r"\d+", text))

# Drill 15: text = "abc123 xyz_45 99bottles"
# Extract all words (abc123, xyz_45, 99bottles) using regex.
import re
text = "abc123 xyz_45 99bottles"
print(re.findall(r"\w+", text))

# Drill 16: text = "Hello   World\tPython\nRocks"
#Extract all whitespace chunks using regex (" ", "\t", "\n").
import re
text = "Hello   World\tPython\nRocks"
print(re.findall(r"\s+", text))
print(text)

# Drill 17: Drill 5 (Character sets)
# text = "cat bat rat mat"
# Extract only "cat" and "bat" using regex.

import re
text = "cat bat rat mat"
print(re.findall(r"[cb]at", text))

'''Drill 18:
name = "Sam"
temp = 98.678
hr = 72
Goal output:
Patient: Sam     | Temp:   98.68°F | HR:   72 bpm
💡 Using f-strings, reproduce that line with proper:
left-aligned name in width 8,
right-aligned temp with 2 decimals, width 8,
right-aligned hr, width 5.
👉 Fill in:
print(f"Patient: {_____} | Temp: {_____}°F | HR: {_____} bpm")'''

name = "Sam"
temp = 98.678
hr = 72
print(f"Patient: {name:<8} | Temp: {temp:8.2f}°F | HR: {hr:5} bpm")

'''Drill 19:
import re
note = "Mia BP 118/76 HR 70 Temp 98.9°F; Leo BP 130/88 HR 95 Temp 101.2°F"
print(re.findall(r"[A-Z][a-z]+", note))
predict: what list will it print?'''
# ['Mia', 'Temp', 'Leo', Temp']

'''Drill 20: Predict output:
import re
note = "Mia BP 118/76 HR 70 Temp 98.9°F; Leo BP 130/88 HR 95 Temp 101.2°F"
print(re.findall(r"\d+/\d+", note))'''
#r"\d+/\d+"

'''Drill 21:
print(re.findall(r"\d+\.\d+", note))
'''
# r"\d+\.\d+"

'''Drill 22:
print(re.findall(r"[A-Z][a-z]+", note))
'''
# r"[A-Z][a-z]+"

'''Drill 23:
print(re.findall(r"[A-Z][a-z]+(?=\sBP)", note))
'''
# r"[A-Z][a-z]+(?=\sBP)"
'''Drill 24:
print(re.findall(r"\d+/\d+|\d+\.\d+|\d+", note))
'''
# r"\d+/\d+|\d+\.\d+|\d+"

'''Drill 25:
print(re.findall(r"[A-Z][a-z]+(?=.*101\.2)", note))
'''
# r"[A-Z][a-z]+(?=.*101\.2)"

'''Drill 26:
import re
text = "BP 118/76, HR 70 bpm, Temp 98.9°F, O2 95%"
print(re.findall(r"\d+", text))
Q1: What does this print?
Q2: Modify it to also catch the fraction 118/76 as one match (not split).
Q3: Modify it again to catch decimals and integers both (98.9, 70, 95, etc.).
'''
#['118', '76', '70', '98', '95']
# print(re.findall(r"\d+/\d+", text))
# print(re.findall(r"\d+\.\d+", text))

'''Drill 27:
import re
text = "BP 118/76, HR 70, Temp 98.9°F, ID 007, Zip 10016"
a) Match all 3-digit numbers only (e.g., 100).
b) Match all 2 to 3 digit numbers.
c) Match only the 2-number BP pattern (e.g., 118/76).
d) Match everything numeric, including BP, decimals, and IDs — but not “10016” (zip) because it’s more than 4 digits.
'''
# a) print(re.findall(r"\d{3}"))
# b) print(re.findall(r"\d{2, 3}"))
# c) print(re.findall(r"\d+/\d+"))
# d) print(re.findall(r"\d+/\d+|d+\.d+|\d{1, 4}"))

'''Drill 28:
Include decimals but still avoid long numbers
text = "BP 118/76 HR 72 Temp 98.9 Zip 10016"
Task: Match:
BP numbers (118/76)
HR (72)
Temp (98.9)
Exclude Zip (10016)
💡 Hint: combine alternation | + \b + decimal pattern.
print(re.findall(r"_____", text))
'''
text = "BP 118/76 HR 72 Temp 98.9 Zip 10016"
print(re.findall(r"\d+/\d+|\d+\.\d+|\b\d{2,3}\b", text))

