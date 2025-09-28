from datetime import datetime

tags = {
    "[HEALTH]": ["exercise", "exercised", "meditation"],
    "[REST]": ["sleep", "slept", "rest", "rested"],
    "[LEARNING]": ["study","studied"],
    "[NUTRITION]": ["food", "diet"],
    "[HYDRATION]": ["water", "fluids"]
}

#function to add time + space + user input + space + tags if applicable
def add_entry(user_input):
    line = str(datetime.now().strftime("%Y-%m-%d %H:%M")) + " " + user_input
    found_tags = set()
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

'''Challenge: Journal Analyzer
Goal: Take your existing journal.txt and generate a summary report.
Requirements:
Read the file line by line.
For each line:
Count how many words the user typed (ignore the date/time).
Count how many tags exist on that line.
Print a summary at the end:
Total number of lines
Total number of words written
Count of each tag across the whole journal
Hints:
You can use .split() to count words:
words = line.split()[2:]  # skip the first two parts if your date/time is "YYYY-MM-DD HH:MM"
word_count = len(words)
For counting tags, you can loop through your tags dictionary and check if the tag exists in the line.'''

with open("journal.txt") as f:
    line_count = 0
    word_count = 0
    tag_count = 0
    for line in f:
        list_of_words_in_line = line.split()[2:]
        for word in list_of_words_in_line:
            if word in tags.keys():
                tag_count += 1
            word_count += 1
        line_count += 1
    print("---------- SUMMARY -----------")
    print(f"Total number of lines: {line_count}")
    print(f"Total number of words: {word_count}")
    print(f"Total number of tags: {tag_count}")
            
