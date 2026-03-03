# ------------------------------------------------------------
# Number Guessing Game
# ------------------------------------------------------------
# This program thinks about a number and the player needs to find it out by guessing.
#
# Rules:
# 1. The program generates a whole integer number between 1 and 20
# 2. Then it enters into a loop
# 3.      The player enters a number
# 4.      The program tells if it is too big, too small or it is the secret number
# 5.      The program ends if the player guesses the secret number correctly
# ------------------------------------------------------------

import random

print(random.randrange(1,20))