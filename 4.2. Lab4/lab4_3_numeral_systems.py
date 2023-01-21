"""
Wylicz wartości dziesiętne następujących liczb zapisanych w różnych
systemach liczbowych:
• 777 (ósemkowo)
• 1011 (binarnie)
• FFF (szesnastkowo)
• 123 (piątkowo)
"""

#777 (ósemkowo)
print(0o777) #511
print(7 * 8 ** 0   +   7 * 8 ** 1    +    7 * 8 **2)

#1011 (binarnie)
print(0b1011) #11
print(1 * 2 ** 0   +   1 * 2 ** 1   +   0 * 2 ** 2   +   1 * 2 **3)

#FFF (szesnastkowo)
print(0xFFF) #4095
print(15 * 16 ** 0   +   15 * 16 ** 1   +   15 * 16 ** 2)

#123 (piątkowo)
print(3 * 5 ** 0   +   2 * 5 ** 1   +   1 * 5 ** 2) # 38