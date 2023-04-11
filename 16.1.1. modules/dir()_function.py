# Wykorzystanie funkcji dir().

import math
import random

print(dir(math)) # Wyświetla wszystkie elementy dostępne w module "math"
# Wyświetlona lista jest mało czytelna.


# Wyświetlenie elementów modułu w czytelniejszy sposób:
for e in dir(math):
    print(e)

print("")

for e in dir(random):
    print(e)