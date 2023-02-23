# OPERATORY BITOWE

# działamy na liczbach całkowitych
# liczby w systemie dziesiętnym
a = 5
b = 3


# KONIUNKCJA BITOWA - ILOCZYN BITOWY & (operatorem jest ampersand, tzw. etka)
print(a, "&", b, "=", a & b) # 5 & 3 = 1
# print(bin(a)) # 0b101, czyli 5 w systemie dziesiętnym
# bin (od binary) - funkcja, która zamieni liczbę dziesiętną na liczbę w systemie dwójkowym

print("{:08b}".format(a))   #00000101
print("{:08b}".format(b))   #00000011
print("-" * 8) # postawienie kreski na 8 znaków (tyle, ile jest bitów)
print("{:08b}".format(a & b))#00000001 (sprawdzanie - jeśli 0 * 1 to fałsz

"""
00000101
00000011
--------
00000001
"""
# każdy bit na tej samej pozycji jest jakby mnożony,  np. 1 * 1 daje 1, 0 * 1 daje 0, itd.
print()


# ALTERNATYWA BITOWA - SUMA BITOWA | (pipe)
print(a, "|", b, "=", a | b) # 5 | 3 = 7
print("{:08b}".format(a))   #00000101
print("{:08b}".format(b))   #00000011
print("-" * 8)
print("{:08b}".format(a | b))#00000111 (sprawdzanie - jeśli 0 + 1, to prawda)

"""
00000101
00000011
--------
00000111
"""
print()


# ALTERNATYWA ROZŁĄCZNA BITOWA (BITOWA RÓŻNICA SYMETRYCZNA) - XOR - ^ - 1 jest tylko wtedy, gdy wartości a i b są różne
print(a, "^", b, "=", a ^ b) # 5 ^ 3 = 6
print("{:08b}".format(a))   #00000101
print("{:08b}".format(b))   #00000011
print("-" * 8)
print("{:08b}".format(a ^ b))#00000110 (sprawdzanie - jeśli 0 ^ 1, to prawda, ale 0 i 0 oraz 1 i 1 to fałsz)

"""
00000101
00000011
--------
00000110
"""
print()


# PRZESUNIĘCIE BITOWE W PRAWO >>
print(a, ">>", 2, "=", a >> 2) # 5 >> 2 = 1
print("{:08b}".format(a))   #00000101
print("-" * 8)
print("{:08b}".format(a >> 2))#00000001

"""
00000101
--------
00000001
"""
print()


# PRZESUNIĘCIE BITOWE W LEWO
print(a, "<<", 2, "=", a << 2) # 5 << 2 = 20
print("{:08b}".format(a))   #00000101
print("-" * 8)
print("{:08b}".format(a << 2))#00010100 - wskoczyły dwa zera od końca (ze względu na przesunięcie)

"""
00000101
--------
00010100
"""
print()


# NEGACJA BITOWA ~
print("~" + str(a), "=", ~a) # ~5 = -6 # wynika to z kodu uzupełnień do dwóch (U2 lub ZU2)
print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(~a))#-0000110

"""
00000101
--------
-0000110
"""
print()


# Kod uzupełnień do dwóch
for i in range(5, -6, -1):
    print("{0:08b} => {1:d}".format(i & 255, i))
# {1:d} - wartość dziesiętna - 'd' od decimal
"""
00000101 => 5
00000100 => 4
00000011 => 3
00000010 => 2
00000001 => 1
00000000 => 0
11111111 => -1
11111110 => -2
11111101 => -3
11111100 => -4
11111011 => -5
"""
print()


print(1 == 1 == 1) # True
print(1 == 1 == -1) # False
