"""
Załóżmy, że na pierwsze pole szachownicy kładziemy 1 ziarno zboża, na
drugie 2 ziarna, na trzecie 4 ziarna i na każde następne pole dwa razy
więcej ziaren niż na pole poprzednie. Napisz program, który zasymuluje
taką sytuację i zliczy sumę wszystkich ziaren na szachownicy.
"""

print("Szachownica ma 64 pola. Na pierwsze pole kładziemy 1 ziarno zboża, na drugie 2, na trzecie 4, itd. \n"
      "Każde następne pole obejmuje dwa razy więcej ziaren niż pole poprzednie. \n"
      "Wynik takiego zabiegu prezentuje się następująco: \n")

i = 1 # na pierwszym polu położone jest jedno ziarno. Na każdym kolejnym dwa razy więcej.
counter = 0 # licznik sumujący liczbę ziaren z kolejnych pól.

while i <= 64:
    print("Pole szachownicy: " + str(i) + ";",
          "liczba ziaren: " + str(2 ** (i-1)))
    counter += (2 ** (i-1))
    i += 1
else:
    print("")
    print("Na wszystkich polach szachownicy znajdzie się w sumie " + str(counter) + " ziaren zboża.")
