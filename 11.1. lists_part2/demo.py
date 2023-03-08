# # ZAMIANA WARTOŚCI DWÓCH ZMIENNYCH

# a = 1
# b = 4
#
# print("a =", a, "b =", b)  # ctrl + alt + L ==> formatowanie kodu - wyrównanie odległości między znakami

# # Jeżeli chcielibyśmy przyporządkować wartość zmiennej "a" do zmiennej "b" i wartość zmiennej "b" do zmiennej "a", to...
# a = b # od teraz zmienna "a" ma wartość 4.
# b = a # przypisując zmiennej "b" wartość zmiennej "a" przypisze się jej wartość 4, a nie 1.

# print("a =", a, "b =", b) # a = 4 b = 4
# # ... wartość zmiennej "b" nie zostanie zmieniona na pierwotną wartość zmiennej "a", czyli 1, ponieważ
# # interpreter czyta linijki po kolei. Najpierw została zmieniona wartość zmiennej "a" na wartość zmiennej "b".
# # Przy zamianie wartości zmiennej "b" na wartość zmiennej "a" po prostu zostanie powtórzona wartość zmiennej "b", czyli 4.


# # Problem można obejść wprowadzając zmienną pomocniczą.
# # Tworzenie zmiennej pomocniczej to tworzenie poczekalni, do której na chwilę odłożymy wartość
# tmp = a # odkładamy do poczekalni wartość zmiennej "a"
# a = b # tutaj zamazuje się wartość "a" na wartość przyporządkowaną do zmiennej "b", czyli 4.
# b = tmp # do zmiennej "b" przypisujemy wartość tymczasową, czyli 1.

# print("a =", a, "b =", b)


# # Zamiast rozpisywać zamianę wartości dwóch zmiennych, można to zrobić w jednej linii.
# a, b = b, a # najprostszy sposób zamiany wartości: zmienna "a" ma wynościć tyle, co zmienna "b", a zmienna "b" ma wynościć tyle, co zmienna "a".
# print("a =", a, "b =", b)



# # OPERACJE NA LISTACH

# # Zamiana wartości dwóch elementów w liście:
# numbers = [1, 2, 3]

# # Gdyby chcieć zamienić miejscami elementy 2 i 1:
# numbers[0], numbers[1] = numbers[1], numbers[0] # prosty sposób na zamianę dwóch elementów w liście
# print(numbers) # [2, 1, 3]



# PRZESKOK DO PLIKU bubble_sort.py - SORTOWANIE BĄBELKOWE I WBUDOWANE METODY SORTOWANIA



# SORTOWANIE CIĄGÓW ZNAKÓW
letters = ["A", "C", " ", "B"]
print(letters)
# Lista jest zbiorem uporządkowanym, co oznacza, że w jakiej kolejności ustawiliśmy elementy, w takiej zostaną wyświetlone.

letters.sort()
print(letters)  ## [' ', 'A', 'B', 'C']

letters.sort(reverse=True)
print(letters)  ## ['C', 'B', 'A', ' ']
# Każdy znak jest zakodowany pod jakąś wartością.Te wartości są w tabeli ASCI (dla podstawowego zakresu znaków)

# Za pomocą funkcji ord() możemy podejrzeć, jak komputer koduje dany znak. ("ord" = "ordinal" = "uporządkowanie", "kolejność")
print(ord("A"), ord("C")) # A = 65;  C = 67
print(ord("a"), ord("c")) # a = 97;  c = 99
# Kolejność sortowania bierze się z tablic ASCI
# najpierw występują duże litery, potem uszeregowane są małe litery.