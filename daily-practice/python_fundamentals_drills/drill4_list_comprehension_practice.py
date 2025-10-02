#Create a list of squares of numbers from 1 to 5 using
#a list comprehension.
list_of_squares = [ x** 2 for x in range(1,6)]
print(list_of_squares)

# Make a list of even numbers between 1 and 10 using 
# a list comprehension.
list_even_numbers = [n for n in range(1, 11) if n % 2 == 0]

#Create a list of the first letters of each word 
# in ["apple", "banana", "cherry"].
list_first_letters = [fruit[0] for fruit in ["apple", "banana", "cherry"]]
print(list_first_letters)

#Make a list of numbers from 1 to 20, but only include numbers 
#that are multiples of 3.
multiples_of_3 = [n for n in range(1, 21) if n % 3 == 0]
print(multiples_of_3)

#Given the string "healthcare", make a list of all 
# vowels in it using a list comprehension.
print([n for n in "healthcare" if n in "aeiouAEIOU"])
print([v for v in "aeiouAEIOU" if v in "healthcare"])

#Create a list of numbers from 0 to 10, but replace even 
# numbers with "even" and keep odd numbers as-is.
print([n if n % 2 != 0 else "even" for n in range(11)])

#Create a list from numbers 1 to 10 where:
#-replace multiples of 2 with "two"
#-replace multiples of 3 with "three
#-keep other numbers as-is.
print([
    "six" if n % 6 == 0 
    else "two" if n % 2 == 0 
    else "three" if n % 3 == 0 
    else n 
    for n in range(1,11)
    ])

# Given the list [10, 15, 20, 25, 30], 
# create a new list where each number is:
# - "big" if greater than 20
#- "medium" if between 15 and 20 (inclusive)
# - "small" otherwise
# Use a single list comprehension with if ... else.
print([
    "small" if n < 15 
    else "medium" if n <= 20 
    else "big" 
    for n in [10, 15, 20, 25, 30]])

# Create a list of the lengths of each word in 
# ["data", "science", "python", "AI"], but:
#if length > 5 → "long"
#otherwise → the actual length
#Use a single list comprehension.

fields = ["data", "science", "python", "AI"]
print(["long" if len(field) > 5 else len(field) for field in fields])

#Given the list [3, 6, 9, 12, 15], create a new list where 
# each number is:
# - squared if it’s less than 10
# - cubed if it’s 10 or more
# - Use a single list comprehension.
print([n ** 2 if n < 10 else n ** 3 for n in [3, 6, 9, 12, 15]])

#Given the list [2, 5, 8, 11, 14, 17], create a new list 
# where each number becomes:
#"small_even" if it’s even and less than 10
#"big_even" if it’s even and 10 or more
#"small_odd" if it’s odd and less than 10
#"big_odd" if it’s odd and 10 or more
#Use a single list comprehension with nested if ... else.
print([
    "small_even" if n < 10 and n % 2 == 0
    else "big_even" if n >= 10 and n % 2 == 0
    else "small_odd" if n < 10
    else "big_odd"
    for n in [2, 5, 8, 11, 14, 17]
])

# Problem 12 (next level):
#Given [12, 7, 0, 19, 8], create a new list where each 
# number becomes:
#"zero" if the number is 0
#"even" if it’s even and not zero
#"odd" if it’s odd
#Use a single list comprehension.
#This one tests order of conditions.

print(["zero" if n == 0
      else "even" if n % 2 == 0
      else "odd"
      for n in [12, 7, 0, 19, 8]
      ])

# Problem 13 (nested lists):
# Given the list of lists [[1, 2], [3, 4], [5, 6]], 
# create a flattened list containing all numbers.
print([x for n in [[1, 2], [3, 4], [5, 6]] for x in n])

#Problem 14 (multiple iterables):
#Given list1 = [1, 2, 3] and list2 = [4, 5], create 
# a list of all sums of pairs (x + y) for every x in
#  list1 and y in list2.
print([x + y for x in [1, 2, 3] for y in [4, 5]])

# Problem 15 (nested + condition):
# Given matrix = [[1, 2, 3], [4, 5, 6]],
# create a flattened list of only the even numbers.
print([x for n in [[1, 2, 3], [4, 5, 6]] for x in n if x % 2 == 0])

#Problem 16 (nested + transformation):
# Given matrix = [[1, 2], [3, 4]], create a flattened 
# list where each number is squared.
print([x ** 2 for n in [[1, 2], [3, 4]] for x in n])

# Problem 17 (nested + conditional transformation):
# Given matrix = [[1, 2], [3, 4]], create a flattened list where:
# even numbers → squared
# odd numbers → unchanged
# Use a single comprehension.
print([x ** 2 if x % 2 == 0
       else x 
       for n in [[1, 2], [3, 4]] 
       for x in n])

# Problem 18 (full-power comprehension):
# You have two lists:
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# Create a flattened list of x * y for every pair (x, y) but only include the products that are even.
# Use a single list comprehension.
# This combines: multiple iterables, a transformation (x * y), a filter (even products)

print([
    x * y
    for x in [1, 2, 3]
    for y in [4, 5, 6]
    if (x * y) % 2 == 0
])