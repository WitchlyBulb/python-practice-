'''In this exercise, you are going to count by 2, 
starting at 2 and ending with the provided number.
You should return the numbers as a space seperated string.
Example:
count_by_two(10) --> "2 4 6 8 10 "
count_by_two(4) --> "2 4 "'''

def count_by_two(end):
    return " ".join(str(i) for i in range (2, end+1, 2)) + " "

# -----------------------------------------------------
# -----------------------------------------------------
'''In this exercise, you are given a starting value, 
an ending value, and an increment. Return how many 
times the loop executes given these parameters.
Example:
loop_count(3, 10, 3) --> 3
loop_count(5, 15, 1) --> 10'''

def loop_count(start, end, increment):
    if increment == 0:
        raise ValueError("Increment cannot be zero.")
    return len(range(start, end, increment))

# -----------------------------------------------------
# -----------------------------------------------------

'''For this exercise, you are going to return an 
output that countdown from a provided starting value. 
Each number should be space seperated.
Example:
countdown(10) --> "10 9 8 7 6 5 4 3 2 1 0 "
countdown(5) --> "5 4 3 2 1 0 "'''

def countdown(start):
    return " ".join(str(num) for num in range (start, -1, -1)) + " "
    
# -----------------------------------------------------
# -----------------------------------------------------

'''Given a starting value, ending value, and an increment
 value, add up all the numbers in the range 
 (inclusive of the end points).
Example:
sum(0, 10, 2) --> 30 # 2 + 4 + 6 + 8 + 10
sum(25, 30, 5) --> 55 # 25 + 30'''


# -----------------------------------------------------
# -----------------------------------------------------
'''Given a starting value, ending value, and an increment
 value, add up all the numbers in the range (inclusive 
 of the end points).
Example:
sum(0, 10, 2) --> 30 # 2 + 4 + 6 + 8 + 10
sum(25, 30, 5) --> 55 # 25 + 30'''
def find_sum(start: int, end: int, increment: int) -> int:
    x = 0
    for i in range(start, end+1, increment):
        x += i
    return(x)

# -----------------------------------------------------
# -----------------------------------------------------
'''
In this exercise, you are going to return the average 
over a range of numbers, from the start value to the 
end value (inclusive of both end points). Example: 
find_average(10, 20) --> 15 
find_average(0, 1000) --> 500
'''
def find_avg(start: int, end: int) -> float:
    nums = range(start, end+1)
    return sum(nums)/len(nums)

print(find_avg(10, 20))
print(find_avg(0, 1000))

# -----------------------------------------------------
# -----------------------------------------------------
'''In this exercise, you are given an number. 
You should return the factorial of the number. 
Remember factorial is multiplying that number times all of the numbers 
below it.
5 factorial = 5 * 4 * 3 * 2 * 1
Example:
factorial(5) --> 120
factorial(3) --> 6'''
def find_factorial(num):
    x = 1
    for i in range(num, 1, -1):
        x *= i
    return x

# -----------------------------------------------------
# -----------------------------------------------------
'''In this exercise, you will be given a shopping list and an item. 
Return True if the item is on the shopping list, otherwise return False.
Example:
shopping_list(["milk", "eggs", "bread"], "milk") --> True
shopping_list(["milk", "eggs", "bread"], "candy") --> False'''
def shopping_list(my_list, item):
    return (item in my_list)

# -----------------------------------------------------
# -----------------------------------------------------
'''In a treasure-hunting game, each character in the string path 
represents a tile the player steps on. Write a function 
countTreasures that takes a string path and returns the 
number of treasure tiles the player found. A treasure tile 
is represented by the character '$'. All other characters 
can be ignored.'''

def countTreasures(path: str) -> int:
    return path.count("$")

# -----------------------------------------------------
# -----------------------------------------------------

'''Write a function countdown_timer that takes an integer start 
representing the number of seconds to count down from. 
The function should return a string with each second listed in 
descending order, separated by a dash (-), ending at 0. 
For example, if start is 3, the return value should be '3-2-1-0'. 
The start will always be a non-negative integer.
'''
def countdown_timer(start: int) -> str:
    return "-".join(str(i) for i in range(start, -1, -1))

