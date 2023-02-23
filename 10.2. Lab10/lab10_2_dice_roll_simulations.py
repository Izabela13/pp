"""
Napisz program, który zasymuluje 16 rzutów kostką do gry a następnie
wyświetli poniższe informacje:
• zestaw wylosowanych wyników,
• wyrzucaną wartość za 8 razem,
• liczbę wyrzuconych szóstek,
• maksymalną liczbę wyrzuconych tych samych wartości pod rząd.
"""

print("Symulacja 16-stu rzutów kostką.")

import random # zaimportowanie modułu "random"

numbers = [] # wylosowane numery będą zapisywane w liście

# zestaw wylosowanych wyników
for i in range(16): # w pętli for będzie losowane w sumie 16 liczb
    number = random.randint(1, 6) # losowanie liczb od 1 do 6
    numbers.append(number) # każda liczba będzie zapisywana do zmiennej number (metodą append)

print("Zestaw wylosowanych wyników:", numbers)


# wyrzucona wartość za 8-mym razem
print("Liczba wyrzucona za 8-mym razem:", numbers[7]) # indeks 0 to pierwszy element z listy --> indeks 7 to ósmy element listy


# liczba wyrzuconych szóstek

count_6 = 0 # licznik szóstek

for six in numbers:
    if six == 6:
        count_6 += 1
else:
    print("Liczba wyrzuconych 6-tek:", count_6)


# maksymalna liczba wyrzuconych tych samych wartości pod rząd

the_same_numbers = 0
count = 0
count_list = []

for element in numbers:
    if the_same_numbers == element:
        count += 1
        count_list.append(count)
    else:
        #count_list.append(count)
        the_same_numbers = element
        count = 0 # zerowanie licznika, jeśli kolejna liczba była inna niż wcześniejsza
else:
    if len(count_list) > 0 and max(count_list) > 0:
        print("Maksymalna liczba wyrzuconych tych samych wartości pod rząd:", max(count_list) + 1)
    else:
        print("Wśród wylosowanych liczb te same wartości nie wystąpiły pod rząd.")

# Jakie liczby wyrzucono n-razy pod rząd, ale największą liczbę razy?
i = 0 # zmienna indeksowa

if len(count_list) == 0: # count_list może być pustą listą
    max_row = 0
else:
    max_row = max(count_list) + 1 # pierwsza wartość w rzędzie nie zapisuje się do listy, bo odwołuje się do poprzedniej

# listy, w których będą zapisywane liczby, które wypadły n-razy pod rząd:
value_list_2r = []
value_list_3r = []
value_list_4r = []
value_list_5r = []
value_list_6r = []
# możliwe, że więcej razy pod rząd nie wypadnie ta sama wartość.
# przy testowaniu maksymalnie pod rząd wypadały 4 liczby.

# uzupełnianie poszczególnych list (z uwzględnieniem zakresu indeksów do indeksu 15)
for element in numbers:

    if max_row == 2 and i + 1 < 16 and numbers[i] == numbers[i + 1]:
        value_list_2r.append(numbers[i])

    if max_row == 3 and i + 2 < 16 and (numbers[i] == numbers[i + 1] == numbers[i + 2]):
        value_list_3r.append(numbers[i])

    if max_row == 4 and i + 3 < 16 and (numbers[i] == numbers[i + 1] == numbers[i + 2] == numbers[i + 3]):
        value_list_4r.append(numbers[i])

    if max_row == 5 and i + 4 < 16 and (numbers[i] == numbers[i + 1] == numbers[i + 2] == numbers[i + 3] == numbers[i + 4]):
        value_list_5r.append(numbers[i])

    if max_row == 6 and i + 5 < 16 and (numbers[i] == numbers[i + 1] == numbers[i + 2] == numbers[i + 3] == numbers[i + 4] == numbers[i + 5]):
        value_list_6r.append(numbers[i])

    i += 1


# tworzenie zmiennej "winners" dla liczb, które wystąpiły największą ilość razy pod rząd
if max_row == 2:
    winners = value_list_2r
if max_row == 3:
    winners = value_list_3r
if max_row == 4:
    winners = value_list_4r
if max_row == 5:
    winners = value_list_5r
if max_row == 6:
    winners = value_list_6r

if max_row in (2, 3, 4, 5, 6):
    print(max_row, "razy pod (nieprzerwany) rząd wyrzucono:", winners)
# Ostatni komunikat nie wyświetli się, jeśli wśród wylosowanych wyników nie pojawiły się obok siebie te same liczby.
