"""
Wyświetl liczby od 1 do 100 z pominięciem liczb podzielnych przez 3.
"""

# for x in range(1, 101):
#     if x % 3 != 0:
#         print(x)


"""
Napisz skrypt wyświetlający na ekranie macierz. Rozmiar macierzy oraz
znak z jakiej będzie zbudowana powinien określić użytkownik
"""

# matrix_size = int(input("Podaj rozmiar macierzy: "))
# matrix_sign = input("Podaj znak dla macierzy: ")
#
# for x in range(matrix_size):
#     for i in range(matrix_size):
#         print(matrix_sign, end = " ")
#     print()



"""
Załóżmy, że na pierwsze pole szachownicy kładziemy 1 ziarno zboża, na
drugie 2 ziarna, na trzecie 4 ziarna i na każde następne pole dwa razy
więcej ziaren niż na pole poprzednie. Napisz program, który zasymuluje
taką sytuację i zliczy sumę wszystkich ziaren na szachownicy.
"""

#rozmiar pola szachownicy = 64

i = 1

for i in range(64):
    print(i)

# na pierwsze pole 1, na drugie 2, na trzecie 4, na czwarte 16, itd...
# 1 2 3 4
# 0 1 2 3

sum = 0

for i in range(64):
    sum += 2**i
    print(sum)
print("Suma wszystkich ziaren zboża na szachownicy to: " + str(sum) + ".")



# 1 ziarenko to 0,4 mg
# 1 ziarno to 0,0004 g
# 1 kg = 1000 g
# 1 t = 1000 kg

tons = int(sum * 0.0004 / 1000 / 1000) # najpierw ile gramów, potem kilo i potem ton
print(tons)

#ile lat trzeba sadzić i zbierać przenicę, żeby osiągnąć ten wynik?
#produkcja przenicy na świecie to około 782_000_000 ton
years = int(tons/782_000_000) # 782e6 (notacja naukowa)

print(years) #9 i pół roku zbierania przenicy całego świata

#jeden pociąg towarowy może przetransportować 2200 t
trains = int(tons/2200)
print(trains)