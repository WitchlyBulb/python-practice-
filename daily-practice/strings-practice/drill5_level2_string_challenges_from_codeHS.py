'''Write a function that will search a given string for 
the string ‘Waldo’ (in any case). If it is found, 
return here. If it is not found, return not here.'''

def find_waldo(n):
    return "here" if 'waldo' in n.lower() else "not here"

print(find_waldo("hello"))
print(find_waldo("hello waldo"))
print(find_waldo("hewaldodo"))
print(find_waldo("Hello Waldo"))
print(find_waldo("w a l d o"))

# ------------------------------------------------------
# ------------------------------------------------------

'''In this exercise, you are going to replace the 
word ‘like’ with ‘dislike’, unless the word computer is found 
after the word like, in which case you will replace ‘like’ with ‘love’.
Example:
replace_like("I like recess") --> "I dislike recess"
replace_like("I like computer science") --> "I love computer science"
'''

def replace_like(phrase):
    list_phrase = phrase.split()
    for i in range(len(list_phrase)):
        if list_phrase[i] == "like":
            if "computer" in list_phrase[i:] or "computers" in list_phrase[i:]:
                list_phrase[i] = "love"
            else:
                list_phrase[i] = "dislike"
    return ' '.join(list_phrase)

print(replace_like("I like recess"))
print(replace_like("I like computer science"))
print(replace_like("I like broccoli"))
print(replace_like("I like coding computers"))

# -----------------------------------------------------
# ---------------------------------------------------

'''In this exercise, you are given a string with two words. 
You need to return a string with those two words switched.
Example:
switch_words("Golden Bear") --> "Bear Golden"
switch_words("day snow") --> "snow day"'''

def switch_words(phrase):
    return " ".join(list(reversed(phrase.split())))
    
print(switch_words("Hello santa"))
    
# -----------------------------------------------------
# ---------------------------------------------------

'''
In this exercise, you are given a word. 
You should return the string with two dashes in added to the
 middle of the string. If the string is an even length, 
 return both dashes in the middle together. If the string has 
 an odd length, the two dashes should surround the middle letter.
Example:
split("even") --> "ev--en"
split("friends") --> "fri-e-nds"
'''

def split(phrase):
    if len(phrase) % 2 == 0:
        middle = len(phrase) // 2
        result = phrase[:middle] + "--" + phrase[middle:]
    else:
        center = len(phrase) // 2
        result = phrase[:center] + "-" + phrase[center] + "-" + phrase[(center+1):]
    return result
print(split("friends"))
print(split("friendsQ"))