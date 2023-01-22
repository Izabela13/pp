"""
Udowodnij, że w zbiorze liczb z zakresu 1-100, jest 11 liczb, które są
parzyste i jednocześnie większe od 90, a gdy są nieparzyste, to
przynajmniej dzielą się przez 9.
"""

print("Twierdzenie:"
      "w zbiorze z zakresu od 1 do 100 jest w sumie 11 liczb, które są:"
      "- parzyste i jednocześnie większe od 90 lub"
      "- są nieparzyste, ale dzielą się przez 9.")

for x in range(1, 101):
    if (x % 2 == 0 and x > 90) or (x % 2 != 0 and x % 9 == 0):
        print(x)
    else:
        print("", end="")