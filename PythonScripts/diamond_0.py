# ------------------------------------------------------------
# Diamond Drawer
# ------------------------------------------------------------
# This program draws different sized diamonds with the hashtag # character.
#
# Rules:
# 1. The program asks for the size of the diamond.
# 2. The program prints the diamond to the console.
# 3. If the size is 0 or lower it does nothing.

# 1 sized diamond: #

# 2 sized diamond:  #
                   ###
                    #

# 3 sized diamond:  #
                   ###
                  #####
                   ###
                    #

# 4 sized diamond:  #
                   ###
                  #####
                 #######
                  #####
                   ###
                    #
#
# etc.
#
# ------------------------------------------------------------

for i in range(0, 5):
    print("#" * i)