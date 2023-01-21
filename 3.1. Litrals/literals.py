#print("Hello...") #literał tekstowy
#print(8 + 2) #intiger
#PI = 3.14 #liczba zmienno-przecinkowa

#LICZBY CAŁKOWITE
print(2)
print(1_000_000) #oddzielenie zer (interpreter ignoruje podkreślniki, wyświetli liczbę w całości
print(-2)
print(+2) #dodawanie plusa jest bezsensu
print(type(2)) #class 'int'


#SYSTEMY LICZBOWE
#system dziesiętny to taki system, w którym liczbę zapisujemy, np. 123 --> 1 * 10 ^ 2 + 2 * 10 ^ 1 + 3 * 10 ^ 0
print(0b101) #101 = 1 * 2 ^2 + 0 * 2 ^ 1 + 1 * 2 ^ 0 = 4 + 1 = 5
print(0o1237)

#system ósemkowy -> 0, 1, 2, 3, 4, 5, 6, 7

print(0xFF) #FF - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F (F to 15. Cyfr mamy tylko 9)
# F * 16 ^ 1 +  F * 16 ^ 0 --> 15 * 16 + 15 * 1
print(15 * 16 + 15 * 1)
print(0b11111111)

print(0o12 + 0xA) #w ósemkowym - 10, w szesnastkowym - 10, powinno wyjść 20

print(type(0o127)) #liczba całkowita zapisana w innym systemie liczbowym


#LICZBY ZMIENNOPRZECINKOWE
print(2.0)
print(.123)
print(99.)
print(5e5) #5 * 10 ^ 3 = 500000.0
print(5E-3) #5 * 10 ^ -3 = 0.005
print(1e17)
print(type(1e17)) #class float


#CIĄGI ZNAKÓW
print("") #pusty ciąg znaków
print("I'm Monthy Python")
print('I\'m Monthy Python') #backlash wprowadza się do znaku specjalnego
print("\\\\\\") # 3 \
print("\\" * 3)  # 3 \
print("", "", "", "", sep = "\\")  # 3 \

print('><', '>\t<', '>\t\t\t<', sep = "\n")
print(type("Agata"))



#WARTOŚCI LOGICZNE (BOOLOWSKIE)
print(False) #wartość utożsamiana z 0
print(type(False)) #<class 'bool'>

print((2 > 3)) #False

print(bool(1)) #True
print(bool(13))#True
print(bool(-1))#True