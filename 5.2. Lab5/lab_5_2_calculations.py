"""
Napisz skrypt obliczający:
- pole powierzchni,
- obwód
- długość przekątnej
dla kwadratów o następujących długościach boku: 2, 7, 11 oraz 19.
"""


print("\n",
"Informacje o sposobie obliczania:\n",
"- pole powierzchni --> P = a * a, lub P = a ** 2 \n",
"- obwód --> 4 * a \n",
"- długość przekątnej --> d = a√2 \n",
"\n")

import math
math.sqrt(2)

side_of_square1 = 2
side_of_square2 = 7
side_of_square3 = 11
side_of_square4 = 19


print("Kwadrat o długości boku równej", side_of_square1, "- informacje: \n",
"- pole powierzchni =", str(side_of_square1 ** 2), "\n",
"- obwód =", str(4 * side_of_square1), "\n",
"- długość przekątnej =", str(round(side_of_square1 * math.sqrt(2),1)),
"\n")

print("Kwadrat o długości boku równej", side_of_square2, "- informacje: \n",
"- pole powierzchni =", str(side_of_square2 ** 2), "\n",
"- obwód =", str(4 * side_of_square2), "\n",
"- długość przekątnej =", str(round(side_of_square2 * math.sqrt(2),1)),
"\n")

print("Kwadrat o długości boku równej", side_of_square3, "- informacje: \n",
"- pole powierzchni =", str(side_of_square3 ** 2), "\n",
"- obwód =", str(4 * side_of_square3), "\n",
"- długość przekątnej =", str(round(side_of_square3 * math.sqrt(2),1)),
"\n")

print("Kwadrat o długości boku równej", side_of_square4, "- informacje: \n",
"- pole powierzchni =", str(side_of_square4 ** 2), "\n",
"- obwód =", str(4 * side_of_square4), "\n",
"- długość przekątnej =", str(round(side_of_square4 * math.sqrt(2),1)),
"\n")