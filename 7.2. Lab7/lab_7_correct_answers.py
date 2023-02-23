# number = int(input("Podaj liczbę: "))
#
# if (number ** .5) % 1 == 0:
#     str1 = "Tak"
#     str2 = ""
# else:
#     str1 = "Nie"


# student_grade

# points = int(input("Podaj liczbę punktów (0-100): "))
# print("Twoja to ", end = " ")
#
# if points > 95:
#     print("bardzo dobry (5.0)")
#
# elif points > 84:
#     print("dobry plus (4.5)")
#
# elif points >= 70:
#     print("dobry (4.0)")
#
# elif points > 60:
#     print("dostateczny plus (3.5)")
#
# elif points > 50:
#     print("dostateczny (3.0)")
#
# else:
#     print("niedostateczny (2.0)")


import random

number = random.randint(1, 10)
msg = "Zgadnij jaką liczbę z przedziału od 1 do 10 mam na myśli!: "
guess = int(input(msg)) # argument funkcji input

if guess == number:
    print("Brawo! Dokładnie taką liczbę miałem na myśli")
else: # Jeśli chcemy zaślepić program, np. nie wykonywać "else", to po "else" należy wstawić "pass".
    msg = "Masz kolejną szansę. Moja liczba jest: " # Zmiana wartości zmiennej "msg" (inny komunikat)
    if number % 2 == 0:
        msg += "parzysta " # zastosowanie operatora +=, co pozwoli na skonkatenowanie drugiej części komunikatu.
    else:
        msg += "nieparzysta "
    guess = int(input(msg))
    if guess == number:
        print("Brawo! Udało się odgadnąć za drugim razem!")
    else:
        msg = "Masz kolejną szansę. Moja liczba jest: "
        if number > 5:
            msg += "większa"
        else:
            msg += "mniejsza lub równa"
        msg += "od liczby 5: "
        guess = int(input(msg))
        if guess == number:
            print("Brawo! A jednak, do trzech razy sztuka!")
        else:
            msg = "Niestety, myślałem o liczbie: " +  str(number) + "."
            print(msg)