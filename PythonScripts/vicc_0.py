# ------------------------------------------------------------
# Vicc generátor
# ------------------------------------------------------------
# Ez a program vicceket generál 5 lista segítségével. Az első listában szereplők,
# a másodikban tevékenységek, a harmadikban helyszínek, a negyedikben és az ötödikben egész mondatok vannak.
#
# A program véletlen szerűen választ a listákból elemeket és egy viccé rakja őket össze:
#
# Két SZEREPLŐ TEVÉKENYSÉG HELYSZÍN.
# Így szól az egyik: ELSŐ MONDAT.
# Mire a másik: MÁSODIK MONDAT.
# ------------------------------------------------------------
import random

szereplok = ["rendőr", "hóember", "apáca", "kutya", "madárijesztő"]

szereplo = random.choice(szereplok)

print("Két", szereplo, "...")