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

# A helper function to get a number,
# repeats the prompt if the input is not a number.
def get_num(prompt):
    while True:
        try:
            i = input(prompt)
            return int(i)
        except ValueError:
            print(i, "is not a number.")


print("Welcome to the Mega Ultra Club!")
print("The guard stops you at the entrance...")
print()


# ------------------------------------------------------------
# STEP 1: Ask for VIP card
# ------------------------------------------------------------

# input() always returns text (a string)
vip_card = input("Do you have a VIP card? (yes/no): ")

# We clean up the text:
# - strip() removes extra spaces
# - lower() converts everything to lowercase
# This makes comparison safer (YES, Yes, yes all work)
vip_card = vip_card.strip().lower()


# ------------------------------------------------------------
# If the visitor has a VIP card, let them in immediately
# ------------------------------------------------------------

if vip_card == "yes":
    print()
    print("The guard sees your VIP card.")
    print("Welcome, honored guest! You may enter immediately.")
    
    # exit() stops the program completely
    exit()


# ------------------------------------------------------------
# STEP 2: Ask for age (only if no VIP card)
# ------------------------------------------------------------

print()
print("No VIP card? Then I need to check your age.")

# Ask for age
# use the helper function to get a number
age = get_num("How old are you? ")


# ------------------------------------------------------------
# STEP 3: Check age and decide what happens
# ------------------------------------------------------------

print()

if age >= 18:
    # If age is 18 or more
    print("You are old enough.")
    print("The guard lets you enter the club.")
    
elif age < 15:
    # If age is less than 15
    print("You are too young for this club!")
    print("The guard sends you to the playground.")
    
else:
    # This means age is 15, 16, or 17
    print("You are not old enough for the club.")
    print("The guard throws you out.")


print()
print("End of game.")