# ------------------------------------------------------------
# Gate Guarding Game
# ------------------------------------------------------------
# This program plays as a security guard at the entrance of a club.
#
# Rules:
# 1. If the visitor has a VIP card, they are allowed in immediately.
# 2. Otherwise, their age is checked:
#       - 18 or older → allowed in
#       - less than 15 → sent to the playground
#       - 15–17 → thrown out
# ------------------------------------------------------------

has_vip = input("Do you have a VIP card? (yes/no): ")

print("The answer was: ", has_vip)