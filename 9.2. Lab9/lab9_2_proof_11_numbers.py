"""
Udowodnij, że w zbiorze liczb z zakresu 1-100, jest 11 liczb, które są
parzyste i jednocześnie większe od 90, a gdy są nieparzyste, to
przynajmniej dzielą się przez 9.
"""

print("Twierdzenie: \n"
      "w zbiorze z zakresu od 1 do 100 jest w sumie 11 liczb, które: \n"
      "- są parzyste i jednocześnie większe od 90 lub \n"
      "- są nieparzyste, ale dzielą się przez 9. \n")

summing = 0 # zmienna sumująca wszystkie wystąpienia

print("Oto liczby spełniające któryś z wymienionych warunków:")
for x in range(1, 101):
    if (x % 2 == 0 and x > 90) or (x % 2 != 0 and x % 9 == 0):
        print(x, end="; ")
        summing += 1

print("\n")
print("Twierdzenie jest PRAWDZIWE.")
print("Wszystkich liczb spełniających któryś z wymienionych warunków jest w sumie " + str(summing) + ".")
