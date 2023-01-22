# działamy na liczbach całkowitych

a = 5
b = 3

# koniunkcja bitowa
print(a, "&", b, "=", a & b) # 5 & 3 = 1
# #print(bin(a)) #0b101
print("{:08b}".format(a))   #00000101
print("{:08b}".format(b))   #00000011
print("-" * 8)
print("{:08b}".format(a & b))#00000001 (sprawdzanie - jeśli 0 * 1 to fałsz

"""
00000101
00000011
--------
00000001
"""
print()


# alternatywa bitowa
print(a, "&", b, "=", a | b) # 5 & 3 = 7
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


# operator rozłączny bitowy - 1 jest tylko wtedy, gdy wartości a i b są różne
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


# przesunięcie bitowe
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


print(a, "<<", 2, "=", a << 2) # 5 << 2 = 20
print("{:08b}".format(a))   #00000101
print("-" * 8)
print("{:08b}".format(a << 2))#00010100

"""
00000101
--------
00010100
"""
print()


#negacja bitowa
print("~" + str(a), "=", ~a) # ~5 = -6
print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(~a))#-0000110

"""
00000101
--------
-0000110
"""
print()


for i in range(5, -6, -1):
    print("{0:08b} => {1:d}".format(i & 255, i))
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