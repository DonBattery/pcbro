# ------------------------------------------------------------
# Word counter program
# ------------------------------------------------------------
# This program counts the appearance of each word in a text
#
# Rules:
# 1. The program stores the text in a string variable.
# 2. Split the text into words. (trim withe spaces)
# 3. Count the appearance of each word using a dictionary.
# 4 EXTRA STEP: instead of reading the string from a variable, open a text file and read line by line.
# 5 EXTRA STEP: print the results in alphabetical order.
# ------------------------------------------------------------

my_dict = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}

for key in my_dict:
    print(key, my_dict[key])