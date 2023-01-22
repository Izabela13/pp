"""
Napisz program, który rozszyfruje poniższą wiadomość: Xq|`gf(bm{|(nibfq)
Dla każdego znaku zmieniono 4 bit na przeciwny.
4-ty bit - bit liczymy od najmniej znaczącego (to jest indeks 3)
"""

#print("c") # znaki w ASCI reprezentowane są przez ciągi bitowe
#print(ord("c")) # wartość w tabeli ASCI to 99. Ta liczba na pewno jest zapisana bitowo
#print(bin(ord("c"))) # 0b1100011

#print(chr(99)) # c
#reprezentacja bitowa:
#print("{:08b}".format(ord("c"))) #01100011

#01100011 - to mamy
#01101011 - zmieniony jest czwarty znak
# sama alternatywa rozłączna nie pomoże. Trzeba go wyizolować


# 01100011 - nasza liczba
# 00001000 - nasza maska
# 01101011 - to chcemy dostać - potrzebujemy alternatywy rozłącznej - XOR, aby dojść do zamiany obiektów

# jak wygenerować maskę? Wziąć 1 i przesunąć o wartość, która nas interesuje
# print("{:08b}".format(1 << 3)) #00001000
# print("{:08b}".format(ord("c") ^ (1 << 3))) # 01101011
# print(chr(ord("c") ^ (1 << 3))) # k

msg = "Xq|`gf(bm{|(nibfq)"

for c in msg:
    print(chr(ord(c) ^ (1 << 3)), end = "")
# rozwiązanie: Python jest fajny!
