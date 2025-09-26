"""
Challenge: Mini Journal App
Goal: Build a small program that lets the user keep a “daily journal” in a text file.
Requirements:
File: "journal.txt"
Program should keep running until the user types "stop"
Each iteration:
Ask the user for a new journal entry
Automatically Save each entry with both the date and the time 
(hint: from datetime import datetime → datetime.now().strftime("%Y-%m-%d %H:%M")).
After the user stops, the program should read the file and print:
Line numbers
Date
Journal entry
Bonus (optional):
If the journal entry contains the word "exercise", add a tag [HEALTH] next to itStart with the smart journal code you just learned.
Add at least 3 more keyword–tag pairs of your choice. Example:
"sleep" → [REST]
"study" → [LEARNING]
"food" → [NUTRITION]
Make sure a single line can get multiple tags if it matches multiple keywords.
Example input:
I studied a lot today and drank water
Output should include both [LEARNING] and [HYDRATION].
Test your program by entering at least 5 journal lines (with and without keywords).
Print the journal with line numbers at the end.
"""

from datetime import datetime

tags = {
    "[HEALTH]": ["exercise", "exercised", "meditation"],
    "[REST]": ["sleep", "slept"],
    "[LEARNING]": ["study","studied"],
    "[NUTRITION]": ["food", "diet"],
    "[HYDRATION]": ["water", "fluids"]
}

#function to add time + space + user input + space + tags if applicable
def add_entry(user_input):
    line = str(datetime.now().strftime("%Y-%m-%d %H:%M")) + " " + user_input
    found_tags = {}
    for x, y in tags.items():
        for word in y:
            if word in user_input.lower():
                found_tags.add(x)
    if found_tags:
        line += " " + " ".join(found_tags)
    return line

# first line
with open("journal.txt", "w") as f:
    first_line = input("Add a line: ")
    f.write(add_entry(first_line) + "\n")

# append more lines, until user enters 'stop'
with open("journal.txt", "a") as f:
    while True:
        new_line = input("Add another line (or type 'stop' to quit): ")
        if new_line.lower().strip() == "stop":
            break
        else:
            f.write(add_entry(new_line) + "\n")

with open("journal.txt", "r") as f:
    i = 1
    for l in f:
        print(f"{i}: {l.strip()}")
        i += 1
