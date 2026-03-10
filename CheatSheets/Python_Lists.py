# ----------------------------------------
# WHAT IS A DICTIONARY?
# ----------------------------------------

# A dictionary stores data as KEY → VALUE pairs.
# Keys must be unique and immutable (strings, numbers, tuples).
# Values can be anything.

person = {
    "name": "Alice",
    "age": 25,
    "city": "London"
}


# ----------------------------------------
# CREATING DICTIONARIES
# ----------------------------------------

# Empty dictionary
d = {}

# Another way to create an empty dictionary
d = dict()

# Creating with values
scores = {
    "Alice": 10,
    "Bob": 8,
    "Carol": 12
}

# Using the dict constructor
user = dict(name="John", age=30)


# ----------------------------------------
# ACCESSING VALUES
# ----------------------------------------

person = {"name": "Alice", "age": 25}

person["name"]      # "Alice"
person["age"]       # 25

# If the key does not exist, Python raises a KeyError


# ----------------------------------------
# SAFE ACCESS WITH get()
# ----------------------------------------

person = {"name": "Alice"}

person.get("name")      # "Alice"

person.get("age")       # None (no error)

person.get("age", 0)    # Default value if key missing


# ----------------------------------------
# ADDING OR MODIFYING VALUES
# ----------------------------------------

person = {"name": "Alice"}

# Add a new key
person["age"] = 25

# Modify existing value
person["age"] = 26


# ----------------------------------------
# REMOVING ITEMS
# ----------------------------------------

person = {"name": "Alice", "age": 25}

del person["age"]       # Delete by key

age = person.pop("age") # Remove and return value

person.clear()          # Remove everything


# ----------------------------------------
# CHECKING IF KEY EXISTS
# ----------------------------------------

person = {"name": "Alice", "age": 25}

"name" in person        # True
"city" in person        # False


# ----------------------------------------
# DICTIONARY LENGTH
# ----------------------------------------

person = {"name": "Alice", "age": 25}

len(person)     # Number of key-value pairs


# ----------------------------------------
# LOOPING THROUGH A DICTIONARY
# ----------------------------------------

scores = {"Alice": 10, "Bob": 8}

# Loop through keys
for name in scores:
    print(name)

# Loop through values
for score in scores.values():
    print(score)

# Loop through key-value pairs
for name, score in scores.items():
    print(name, score)


# ----------------------------------------
# GETTING KEYS, VALUES, ITEMS
# ----------------------------------------

scores = {"Alice": 10, "Bob": 8}

scores.keys()      # dict_keys(['Alice', 'Bob'])
scores.values()    # dict_values([10, 8])
scores.items()     # dict_items([('Alice',10), ('Bob',8)])


# ----------------------------------------
# COPYING DICTIONARIES
# ----------------------------------------

a = {"x": 1, "y": 2}

b = a           # NOT a copy (same object)

c = a.copy()    # Real copy


# ----------------------------------------
# MERGING DICTIONARIES
# ----------------------------------------

a = {"x": 1}
b = {"y": 2}

c = a | b       # Python 3.9+ merge operator
# {'x':1, 'y':2}

a.update(b)     # Modifies a


# ----------------------------------------
# DICTIONARY COMPREHENSIONS
# ----------------------------------------

# Create dictionary of squares
squares = {x: x*x for x in range(5)}

# Result:
# {0:0, 1:1, 2:4, 3:9, 4:16}


# ----------------------------------------
# NESTED DICTIONARIES
# ----------------------------------------

students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 21, "grade": "B"}
}

students["Alice"]["grade"]   # "A"


# ----------------------------------------
# COMMON PATTERN: COUNTING
# ----------------------------------------

text = "banana"
counts = {}

for letter in text:
    if letter not in counts:
        counts[letter] = 0
    counts[letter] += 1

# Result:
# {'b':1, 'a':3, 'n':2}


# ----------------------------------------
# SHORTER COUNTING WITH get()
# ----------------------------------------

text = "banana"
counts = {}

for letter in text:
    counts[letter] = counts.get(letter, 0) + 1