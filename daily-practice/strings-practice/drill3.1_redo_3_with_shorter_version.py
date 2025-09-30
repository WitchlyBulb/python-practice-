'''Write a function that returns a given string with the value 
found at the 2nd index removed. 
(Note: The stirng will always have at least 3 characters.)'''

def remove_second_index(n):
    return n[:2] +n[3:]
print(remove_second_index("halleluyah"))


def remove_index_using_enumerate(k):
    return ''.join([ch for i, ch in enumerate(k) if i != 2])
print(remove_index_using_enumerate("jack and jill"))
