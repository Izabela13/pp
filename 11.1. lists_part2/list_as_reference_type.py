list_1 = [9] # lista wskazuje na obszar pamięci, w której jest wartość 9
list_2 = list_1 # podstawianie do listy 2 wartości z listy 1 - skopiowanie referencji z listy 1 do listy 2
# lista 1 i lista 2 wskazują na ten sam obszar pamięci, w której znajduje się wartość 9
# są dwie nazwy, ale lista jest jedna

list_2[0] = 13

print(list_2)
print(list_1)
# charakter referencyjny list - zarówno lista_2 jak i lista_1 będą teraz przechowywać wartość 13
# jedna nazwa została użyta do tego, aby zmodyfikować element w liście. Druga nazwa nadal wskazuje na tę samą listę.


