# Zadanie 1. Wyświetl na ekranie wzór

from time import sleep

#############################################################
print("Wyświetlanie wzoru za pomocą pętli for:"), sleep(3)
for x in ["*"]:
    print(x, x, sep = " " * 8), sleep(1)
    print(x * 2, x * 2, sep = " " * 6), sleep(1)
    print(x * 3, x * 3, sep = " " * 4), sleep(1)
    print(x * 4, x * 4, sep = " " * 2), sleep(1)
    print(x * 5, x * 5, sep = " " * 0), sleep(1)
    print(x * 4, x * 4, sep = " " * 2), sleep(1)
    print(x * 3, x * 3, sep = " " * 4), sleep(1)
    print(x * 2, x * 2, sep = " " * 6), sleep(1)
    print(x, x, sep = " " * 8), sleep(1)
#############################################################

print("\n")

#############################################################
print("Wyświetlanie wzoru za pomocą pętli while:"), sleep(3)
x = "*"

i = 1
j = 8

m = 4
n = 2

while i <= 5:
    print((x * i), (x * i), sep = " " * j), sleep(1),
    i += 1;
    j -= 2
else:
    while m >= 1:
        print((x * m), (x * m), sep = " " * n), sleep(1),
        m -= 1;
        n += 2
#############################################################