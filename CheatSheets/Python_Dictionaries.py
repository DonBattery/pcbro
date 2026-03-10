# ----------------------------------------
# CREATING LISTS
# ----------------------------------------

numbers = [1, 2, 3, 4]        # A list with 4 integers
names = ["Alice", "Bob"]      # A list with strings
mixed = [1, "hello", 3.5]     # Lists can contain mixed data types
empty = []                    # Create an empty list

# You can also create lists with the list() constructor
letters = list("hello")       # ['h', 'e', 'l', 'l', 'o']


# ----------------------------------------
# ACCESSING ELEMENTS
# ----------------------------------------

numbers = [10, 20, 30, 40]

numbers[0]    # First element -> 10
numbers[1]    # Second element -> 20

numbers[-1]   # Last element -> 40
numbers[-2]   # Second from the end -> 30

# Python uses ZERO-BASED indexing


# ----------------------------------------
# SLICING LISTS
# ----------------------------------------

numbers = [10, 20, 30, 40, 50]

numbers[1:4]     # [20, 30, 40] (start inclusive, end exclusive)
numbers[:3]      # [10, 20, 30] (from start)
numbers[2:]      # [30, 40, 50] (to end)
numbers[::2]     # [10, 30, 50] (step size 2)

# Slicing creates a NEW list


# ----------------------------------------
# MODIFYING ELEMENTS
# ----------------------------------------

numbers = [10, 20, 30]

numbers[1] = 99     # Change element at index 1
# Result: [10, 99, 30]


# ----------------------------------------
# ADDING ELEMENTS
# ----------------------------------------

numbers = [1, 2, 3]

numbers.append(4)       # Adds element to the end
# [1, 2, 3, 4]

numbers.insert(1, 99)   # Insert value at index
# [1, 99, 2, 3, 4]

numbers.extend([5, 6])  # Add elements from another list
# [1, 99, 2, 3, 4, 5, 6]


# ----------------------------------------
# REMOVING ELEMENTS
# ----------------------------------------

numbers = [1, 2, 3, 4]

numbers.remove(3)   # Remove first occurrence of value
# [1, 2, 4]

numbers.pop()       # Remove and return last element
# returns 4

numbers.pop(0)      # Remove element at index
# removes first element

del numbers[1]      # Delete element at index

numbers.clear()     # Remove all elements


# ----------------------------------------
# LIST LENGTH
# ----------------------------------------

numbers = [10, 20, 30]

len(numbers)    # returns 3


# ----------------------------------------
# CHECKING MEMBERSHIP
# ----------------------------------------

numbers = [10, 20, 30]

20 in numbers       # True
99 in numbers       # False

20 not in numbers   # False


# ----------------------------------------
# LOOPING THROUGH A LIST
# ----------------------------------------

numbers = [10, 20, 30]

for n in numbers:
    print(n)       # Prints each element


# Loop with index
for i in range(len(numbers)):
    print(i, numbers[i])


# Recommended: index + value
for i, value in enumerate(numbers):
    print(i, value)


# ----------------------------------------
# SORTING
# ----------------------------------------

numbers = [5, 2, 8, 1]

numbers.sort()        # Sort list in-place
# [1, 2, 5, 8]

numbers.sort(reverse=True)   # Descending order

sorted_numbers = sorted(numbers)   # Returns NEW sorted list


# ----------------------------------------
# REVERSING
# ----------------------------------------

numbers.reverse()     # Reverse list in-place

rev = numbers[::-1]   # Create reversed copy using slicing


# ----------------------------------------
# LIST CONCATENATION
# ----------------------------------------

a = [1, 2]
b = [3, 4]

c = a + b     # [1, 2, 3, 4]

a += b        # Extends list a


# ----------------------------------------
# LIST REPEAT
# ----------------------------------------

zeros = [0] * 5    # [0, 0, 0, 0, 0]


# ----------------------------------------
# COPYING LISTS
# ----------------------------------------

a = [1, 2, 3]

b = a            # NOT a copy (same object!)

c = a.copy()     # Real copy
d = a[:]         # Another way to copy


# ----------------------------------------
# LIST COMPREHENSIONS (VERY PYTHONIC)
# ----------------------------------------

# Create list of squares
squares = [x*x for x in range(10)]

# With condition
even = [x for x in range(10) if x % 2 == 0]


# ----------------------------------------
# COMMON BUILT-IN FUNCTIONS
# ----------------------------------------

numbers = [4, 7, 1, 9]

min(numbers)    # 1
max(numbers)    # 9
sum(numbers)    # 21


# ----------------------------------------
# NESTED LISTS (LIST OF LISTS)
# ----------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0][1]    # 2