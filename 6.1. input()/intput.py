#KONKATENACJA

#print(2 + 2) # wynik w postaci wyświetlenia operacji z ciągu znaków
# Można to ująć inaczej
#print("2" + "2") # nastąpi połączenie tych znaków --> 22
# nie można łączyć różnych typów danych ze sobą
# print("2" + 2) # wystąpi błąd

#print("2" + "3") # etc...


#INPUT

#print("Jak masz na imię?")
# do zmiennej name podamy to, co poda nam użytkownik

#name = input()

#print("Witaj " + name + "!" + " Jak Ci minął dzień?")


# Jeżeli chcemy przekazać liczbę jako ciąg znaków - int()
#number = int("2")
#print(number * 5)

#number = "2"
#print(number * 5)
# błąd semantyczny - znaczeniowy - trudniejszy do wykrycia
# operator plus i gwiazka mają dwie opcje


#temp = float("36.6")
#print(temp)


# Konwrsja z liczby na string
#age = 24
#print(str("Mam " + str(age) + " lat\\a."))


#Testowanie

#string_number = input("Podaj liczbę całkowitą: ") #promptowanie - można zostawić spacje lub wstawić \n (nowa linia)
#multiplier = 9
#result = multiplier * int(string_number)
#print("Gdy liczbę " + string_number + " pomnożymy przez " + str(multiplier) + ", to otrzymamy: " + str(result) + ".")


# twierdzenie Pitagorasa
#a = float(input("Wprowadź długość pierwszego boku: "))
#b = float(input("Wprowadź długość drugiego boku: "))
#result = (a**2 + b**2) ** .5

#print("Długość przeciwprostokątnej wynosi " + str(result) + ".")



#Replikator

# print("Ala" * 3)
# print(3 * "Ala") # nie można replikować z wartpściami cząstkowymi.
# jeżeli przemnożymy string przez wartość ujemną string się nie zreplikuje

#print("Ala" * -4)



# Rysowaine

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|" + "\n") * 5, end="")
print("+" + 10 * "-" + "+")

