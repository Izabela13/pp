# # TWORZENIE PIERWSZEGO ALGORYTMU - IMPLEMENTACJA SORTOWANIA BĄBELKOWEGO

# numbers = [4, 5, 2, 1] # elementy do posortowania

# # I iteracja:
# # przy pierwszym przejściu algorytm będzie brał dwa sąsiadujące obok siebie elementy i sprawdzał po kolei:
# # czy 4 jest większe od 5? 4 nie jest większe od 5, więc dwa pierwsze elementy zostają na swoich pozycjach.
# # czy 5 jest większe od 2? 5 jest większe od 2, więc te dwa elementy trzeba zamienić miejscami: [4, 2, 5, 1].
# # czy 5 jest większe od 1? 5 jest większe od 1, więc te dwa elementy zostaną zamienione miejscami: [4, 2, 1, 5]
# # po pierwszym przejściu (pierwszej iteracji) zbiór zostanie posortowany następująco:
# # numbers = [4, 2, 1, 5]

# # II iteracja:
# # czy 4 jest większe od 2? 4 jest większe od 2, więc te dwie pozycje zostają zamienione: [2, 4, 1, 5]
# # czy 4 jest większe od 1? 4 jest większe od 1, więc następuje zamiana pozycji: [2, 1, 4, 5]
# # czy 2 jest większe od 1? 2 jest większe od 1, więc te pozycje zostaną zamienione: [1, 2, 4, 5]
# # czy 2 jest większe od 4? Nie. 2 nie zostaje zamienione miejscem z 4.
# # numbers = [1, 2, 4, 5]

# # Pętla przechodzi po wszystkich elementach oraz iteruje do momentu, dopóki wszystkie elementy nie zostaną posortowane.



# # Jakich mechanizmów będziemy potrzebować do algorytmu? PĘTLI
numbers = [4, 5, 2, 1] # w innych językach programowania listę nazwya się tablicą

# # Mamy listę i chcemy ja posortować
# # Sortowanie będzie odbywać się w PĘTLI WHILE, bo nie wiemy, ile razy będziemy iterować po elementach.
# # Będziemy chcieli obracać tą pętlą do momentu posortowania całego zbioru.

swapped = True # zmienna pomocnicza "czy była zamiana?"
# # Aby pętla wystartowała, trzeba ustawić zmienną "swapped" na "True".
# # pętla będzie się wykonywała dopóki swapped == True.
# # Jeżeli podczas operacji porównywania dwóch liczb zostanie zrobiona zamiana, to znaczy, że lista nie jest posortowana
  # i trzeba kontynuować operację.

# # I pętla
# while swapped: # pętla główna, w której będziemy sprawdzać zmienną swapped
#     swapped = False # ustawienie zmiennej na False, bo jeżeli nie będzie zamiany, zmienna swapped wyhamuje pętlę.
#     # II pętla
#     for i in range(len(numbers) - 1): # pętla będzie przechodziła przez wszystkie elementy - 1
#         if numbers[i] > numbers[i + 1]: # warunek sprawdzający, czy element[i] jest większy od elementu[i + 1]
#             # jeżeli element[i] jest większy od elementu[i + 1], to trzeba zamienić je miejscami
#             numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i] # zamiana miejsc dwóch elementów
#             swapped = True # jeżeli nastąpiła zamiana, zmienną "swapped" ustawiamy na "True", co oznacza, że zbiór nie jest jeszcze posortowany
# # Jeżeli pętla dojdzie do momentu, gdzie nie nastąpi już żadna zamiana elementów, zmienna pomocnicza "swapped" zostanie na "False".
# # Efektem będzie zwrócenie posortowanej listy.
# print(numbers) # [1, 2, 4, 5]


# Sprawdzanie algorytmu bąbelkowego dla wartości powtarzających się, bardziej zróżnicowanych
numbers = [4, 5, 2, 1, 3, 333333, 3, 3, 3, 3, 7, 89, 3, 1, 1, 0, 3333, 567, 2]

swapped = True
counter = 1

while swapped: # pętla główna, w której będziemy sprawdzać zmienną swapped
    swapped = False # ustawienie zmiennej na False
    for i in range(len(numbers) - 1): # pętla będzie przechodziła przez wszystkie elementy - tyle razy, ile elementów - 1
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True
        counter += 1
        #print(i, numbers) # umieszczenie funkcji print w tym miejscu pokazuje, jak przebiegały operacje sortowania.
                          # żeby posortować cały zbiór trzeba było wykonać 18 x 16 operacji, czyli w sumie 288 przebiegów.

print("Sortowanie bąbelkowe:", counter, numbers)
# Wynik ostateczny 289 [0, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 5, 7, 89, 567, 3333, 333333]



# # Sortowanie za pomocą wbudowanych funkcji sort i sort(reverse=True)
numbers = [4, 5, 2, 1, 3, 333333, 3, 3, 3, 3, 7, 89, 3, 1, 1, 0, 3333, 567, 2]

numbers.sort()
print("Sortowanie metodą sort():", numbers) # sortowanie wydajniejsze niż sortowanie bąbelkowe

numbers.sort(reverse=True)
print("Sortowanie metodą sort(reverse=True):", numbers)