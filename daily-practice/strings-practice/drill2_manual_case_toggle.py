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


