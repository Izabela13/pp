# # Zadanie 1:

import math
import random
import platform

print("Procesor:", platform.processor())
print("Losowanie", random.sample([x for x in range(1, 11)], 3))
print("Sinus 90 stopni:", math.sin(math.radians(90)))