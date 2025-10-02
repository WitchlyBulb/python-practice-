'''The caps lock key is broken! Write a function that will turn all capital 
letters to lowercase and all lowercase letters to uppercase in a given string. 
For example, if the given string was hI mOM!, the output shoudl be Hi Mom!'''

def swapcase(n):
    result = []
    for char in n:
        if char.isupper():
            result.append(char.lower())
        elif char.islower():
            result.append(char.upper())
        else:
            result.append(char) # if non-alphabetic characters
    return ''.join(result)

print(swapcase("hI mOM!"))

# ------------------------------------
# ---------------------------------------

'''Drill 2: Manual case toggle (no built-in swapcase)
Write a function that:
Loops over each character in a string
If uppercase → make it lowercase
If lowercase → make it uppercase
Leave all other characters unchanged'''

def toggle_case (word):
    return ''.join([char.lower() if char.isupper()
                   else char.upper() if char.islower()
                   else char
                   for char in word])

print(toggle_case("Hi mom!"))

# -------------------------------------------------
# -------------------------------------------------

'''Write a function that returns a given string with the value 
found at the 2nd index removed. 
(Note: The stirng will always have at least 3 characters.)'''

def remove_second_index(n):
    return n[:2] +n[3:]
print(remove_second_index("halleluyah"))


# -------------------------------------------------
# -------------------------------------------------

'''You are traveling the seven seas. 
Given a string representing land, find the character
 ‘X’ (marks the spot) and return the index of the treasure! 
 Return -1 if no treasure exists. If there are multiple treasures, 
 return the one with the smallest index.'''

def treasure_hunt(land_str):
	return land_str.find("X")

print(treasure_hunt("no treasure"))
print(treasure_hunt("X marks the spot X"))

# returns -1 if X not there

