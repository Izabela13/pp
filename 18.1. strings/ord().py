char1 = "a"
char2 = " "

print(ord(char1)) # 97
print(ord(char2)) # 32
print()


print(ord("ę")) # 281 - wychodzi poza 256 możliwości kodowania
# Jaki to jest znak unicode?

# Wartość heksadecymalna
print(hex(ord("ę"))) # 0x119

# Wyświetlanie znaku unicode o kodzie u0119
print("\u0119") # ę
print()


# Jak działą kodowanie UTF8
c = "a"
print(c, ord(c), hex(ord(c)), c.encode())  # a 97 0x61 b'a' - znak "a" jest kodowany w jednym bajcie

print()

c = "\u20AC" # nie ma znaczenia wielkość liter
print(c) # €
print(c, ord(c), hex(ord(c)), c.encode()) # € 8364 0x20ac b'\xe2\x82\xac'

# Żeby zakodować i wyświetlić znak euro potrzebne są 3 bajty (kodowanie za pomocą UTF8)