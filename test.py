def sum(a, b):
    """Returns the sum of two numbers."""
    return a + b

def isEven(n):
    """Returns True if n is even, False otherwise."""
    if n %2 == 0:
        return True
    else:
        return False
    
def power(base, exp=2): # Default exponent is 2, can be overridden
    return base ** exp

class Person:
    def __init__(self, name, age): # self refers to the instance of the class itself
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})" # (formatted string literals), such as f"Hello, {name}!"

print(sum(3, 5))  # Output: 8

print(isEven(4))  # Output: True

print(power(3))       # 9
print(power(2, exp=3))# 8

p = Person("Muni", 35)
print(p)  # Output: Person(name=Muni, age=35)

# multiple returns
def minmax(nums):
    return min(nums), max(nums)

mn, mx = minmax([1,2,3])
print(mn, mx)  # Output: 1 3

fruits = ["apple", "banana"]         # list (mutable)
coords = (10, 20)                    # tuple (immutable)
unique_nums = {1, 2, 3}              # set
person = {"name": "Muni", "age": 35} # dict (map in Java)

# Unpacking
values = [1, 2, 3, 4, 5]
first, *middle, prev, last = values  # first = 1, middle = [2, 3, 4], last = 5
print(first, middle, prev, last)  # Output: 1 [2, 3, 4] 5

