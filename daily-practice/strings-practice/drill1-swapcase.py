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