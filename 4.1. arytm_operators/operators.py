#INSTRUKCJE I WYRAŻENIA
print("Mam na imię...") #instrukcja

2 + 2 #to jest wyrażenie
print(2 + 2)

a = 2 ** 3 #instrukcja przypisania
print(a)


#OPERATORY
print(2 + 10 - 1 - 1)
print(2+-3) # -1

print(2 * 3) # 6 - liczba całkowita
print(2 * 3.) # 6.0 - typ zmiennoprzecinkowy


# dzielenie i dzielenie całkowite - wyjątek od zasady
print(4 / 2) # 2.0 - float
print(4//2) # 2 - liczba całkowita
print(4//2.) # 2.0 - float (część ułamkowa zniknie)
print(4//3.) # 1.0 - float, bez części ułamkowej 1.333333....

# // flour divider - zaokrąglenie w dół do najbliższej liczby całkowitej
print(-3//2) #-2
print(-4//3) #-2
# w przypadku liczb dodatnich --> w dół do najbliższej liczby całkowitej
# w przypadku liczb ujemnych --> w dół do najbliższej liczby ujemnej, np. -1.3333... ---> -2


#potęgowanie
print(3 ** 3) # 27


#modulo
print(4 % 3) # 1 --? 3 w 4 mieści się raz. Reszta to 1
print(5 % 3) #2

print(14 % 3) #2
#14/3 = 4,... -->  3*4 = 12; 14 - 12 = 2 --> reszta 2
print(14/3) # 4,6666...

print(14 - 3 * 4) # 2


#czy liczba jest parzysta
print(3 % 2) # 1 - nieparzyta
print(3 % 2 == 0) #False - nieparzysta

print(4 % 2) # 0 - parzysta
print(4 % 2 == 0) # True - parzyste



#OPERATORY JEDNOARGUMENTOWE
print(-1) #operator jednoargumentowy ma najwyższy priorytet


#ŁĄCZENIE OPERATORÓW LEWO- I PRAWOSTRONNE
print(2 + 3 -1) # 2 + 3 = 5; 5 - 1 = 4. Operatoru + i - mają taki sam priorytet
print(2 ** 2 ** 3) # 2 do pot. 3 i 2 do pot. 8 --> (2**3) i następnie (2**(wynik z 2**3) #256
print((2 ** 2) ** 3) # 64, bo narzuciliśmy nawiasy

"""
Hierarchia operatorów
-, + - operatory jednoargumentowe
** - potęgowanie
*, /, //, % 
+ i - (dodawanie i odejmowanie)
"""

print(5 - 2 ** 1 ** 2 / 2) #zminnoprzecinkowe, bo mamy dzielenie /


#SYSTEMY LICZBOWE
"""
sysytem dwójkowy: 0, 1 - przed liczbą prefiks 0b lub 0B
system ósemkowy (okta): 0, 1, 2, 3, 4, 5, 6, 7 - przed liczbą prefiks 0o lub 0O
system szesnastkowy (heksa): 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F (F to 15) - przed liczbą prefiks 0x lub 0X
"""

#system ósemkowy
print (0o47) # 39 - podstawa * 8 do potęgi 0, 1, 2...
print(7 * 8 ** 0 + 4 * 8 ** 1)

#dziesiętnie 47 --> 47 to 7 jedności i 4 dziesiątki
# 7 * 10 ** 1 + 4 * 10 ** 1
# ósemkowo - 7 jedności i 4 ósemki


# system szesnastkowy
print(0x2F)
print(15 * 16 ** 0    +   2 * 16 **1)
# F to 15. 15 podnosimy mnożymy 16 (bo to system szesnastkowy) i podnosimy do potęgi 0, bo to jedności
# 2 mnożymy przez 16 (bo system szesnastkowy) i podnosimy do potęgi 1, bo do dzięsiątki (idziemy od tyłu)


#system binarny:
print(0b101) # 1 jedności (2 ** 0), 0 dwójek (2 ** 1), 1 podwójna dwójka - 1 czwórek (2 ** 2) --- 5
print(1 * 2 ** 0   +   0 * 2 ** 1   +   1 * 2 **2) # 5
