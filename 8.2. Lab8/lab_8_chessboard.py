"""
Załóżmy, że na pierwsze pole szachownicy kładziemy 1 ziarno zboża, na
drugie 2 ziarna, na trzecie 4 ziarna i na każde następne pole dwa razy
więcej ziaren niż na pole poprzednie. Napisz program, który zasymuluje
taką sytuację i zliczy sumę wszystkich ziaren na szachownicy.
"""

#rozmiar pola szachownicy = 64

i = 1

while i >= 64:
    i **= 2
    print(i)
