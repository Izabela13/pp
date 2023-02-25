# # Tworzenie pierwszego algorytmu
#
# numbers = [4, 5, 2, 1]
# # przy pierwszym przejściu algorytm będzie brał dwa pierwsze elementy i sprawdzał, czy 4 jest większe od 5
# # czy 5 jest większe od 2, czy 5 jest więszke od 1
# numbers = [4, 2, 1, 5]
# # czy 4 jest większe niż 2, czy 4 jest większe niż 1
# numbers = [2, 1, 4, 5]
# numbers = [1, 2, 4, 5]
# # pętla obraca się do momentu, w którym wszystkie elementy zostają posortowane


# numbers = [4, 5, 2, 1] # w innych językach nazwya się to tablicą
#
# # pętla while, bo nie wiemy, ile razy będziemy iterować po elementach.
#
# swapped = True # zmienna pomocnicza, czy była zamiana
# # pętla będzie się wykonywała dopóki swapped == True.
#
# while swapped: # pętla główna, w której będziemy sprawdzać zmienną swapped
#     swapped = False # ustawienie zmiennej na False
#     for i in range(len(numbers) - 1): # pętla będzie przechodziła przez wszystkie elementy - tyle razy, ile elementów - 1
#         if numbers[i] > numbers[i + 1]:
#             numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#             swapped = True
#
# print(numbers)


# numbers = [4, 5, 2, 1, 3, 3333333, 3, 3, 3, 3, 3, 7, 89, 3, 1, 10]
#
# swapped = True
#
# while swapped: # pętla główna, w której będziemy sprawdzać zmienną swapped
#     swapped = False # ustawienie zmiennej na False
#     for i in range(len(numbers) - 1): # pętla będzie przechodziła przez wszystkie elementy - tyle razy, ile elementów - 1
#         if numbers[i] > numbers[i + 1]:
#             numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#             swapped = True
#         print(numbers)
#
# print(numbers)



# # Sortowanie za pomocą wbudowanych funkcji sort i sort(reverse=True)
# numbers = [4, 5, 2, 1, 3, 3333333, 3, 3, 3, 3, 3, 7, 89, 3, 1, 10, 3333, 567]
#
# numbers.sort()
# print(numbers)
#
# numbers.sort(reverse=True)
# print(numbers)