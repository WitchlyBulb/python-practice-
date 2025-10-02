#Stage 1:
# Create a dictionary where the keys are numbers from 1 to 5, and the 
# values are just the numbers themselves 
# (so basically {1:1, 2:2, 3:3, 4:4, 5:5}).

print({n: n for n in range(1, 6)})

# -------------------------------------------------
# -------------------------------------------------

# Stage 2: Slightly harder
# Now let’s add a transformation.
# 👉 Make a dictionary where the keys are numbers from 1 to 5, 
# but the values are their squares.

print({n: n**2 for n in range(1, 6)})



#Stage 3: Add a condition
# Let’s add filtering now.
# 👉 Build a dictionary of even numbers from 1 to 10 as keys, with their cubes as values.
#Expected output:
#{2: 8, 4: 64, 6: 216, 8: 512, 10: 1000}

print({n: n ** 3 for n in range(1, 11) if n % 2 == 0})


#Stage 4: Key transformation
# Task: Take the list ["apple", "banana", "cherry"] and build a dictionary 
# where the keys are the words in uppercase and the values are their lengths.
# Expected output:
# {'APPLE': 5, 'BANANA': 6, 'CHERRY': 6}

print({n.upper(): len(n) for n in ["apple", "banana", "cherry"]})

# Stage 5: Reverse a dictionary using a comprehension.
# Take this dictionary:
# fruits = {"apple": 5, "banana": 6, "cherry": 6}
# Create a new dictionary where the keys are the values and 
# the values are the original keys.

fruits = {"apple": 5, "banana": 6, "cherry": 6}
print({y: x for x, y in fruits.items()})

# Stage 6: With condition on values
# From the same fruits dictionary:
# fruits = {"apple": 5, "banana": 6, "cherry": 6}
# Build a dictionary where you only include fruits whose 
#value is greater than 5, but flip key ↔ value like before.
# Expected output:
# {6: 'cherry'}   # banana is overwritten

fruits = {"apple": 5, "banana": 6, "cherry": 6}
print({y: x for x, y in fruits.items() if y > 5})

# Stage 7: Nested comprehension (slightly advanced)
# Say we have a nested list:
# pairs = [("a", 1), ("b", 2), ("c", 3)]
# Build a dictionary comprehension that creates:
# {'a': 1, 'b': 2, 'c': 3}
pairs = [("a", 1), ("b", 2), ("c", 3)]
print({x: y for x, y in pairs})


# Stage 8: Stage 8: Nested loops
# Build a dictionary where the keys are pairs (x, y) and 
#the values are their product. Use x from [1, 2] and y from [10, 20].
# Expected output:
# {(1, 10): 10, (1, 20): 20, (2, 10): 20, (2, 20): 40}

print({(x, y): x * y for x in [1, 2] for y in [10, 20]})





