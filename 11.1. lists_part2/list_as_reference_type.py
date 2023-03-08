## LISTA JAKO TYP REFERENCYJNY

# nazwa w niektórych językach programowania nazywana jest "referencją".
list_1 = [9]    # lista "list_1" wskazuje na obszar pamięci, w której znajduje się lista z elementem 9.
list_2 = list_1 # podstawianie do listy "list_2" wartości z listy "list_1" - skopiowanie referencji z listy 1 do listy 2
# Lista "list_1" i lista "list_2" wskazują teraz na ten sam obszar pamięci, w której znajduje się wartość 9.
# Jest jedna lista i dwie nazwy, które do niej prowadzą. Niezależnie od tego, ile będzie nazw, lista będzie jedna.

# Referencja to odwołanie do jakiegoś miejsca w pamięci komputera, gdzie mamy np. obiekt "list_1" z wartością [9].
# To, co dzieje się w linii 5 to przypisanie/ skopiowanie referencji z listy "list_1" do nowej nazwy "list_2".
# Dwie nazwy - "list_1" i "list_2" wskazują na ten sam obszar pamięci, gdzie znajduje się tablica.

# W sytuacji przypisania jednej listy do drugiej, itd., jeżeli zmienimy listę poprzez którąś z nazw,
# to właściwie zmienimy jedną listę, bo wszystkie nazwy będą wskazywały na tę samą listę (zmienioną).

# Jedną z nazw odwołujących się do listy używamy do tego, aby zmodyfikować listę z elementem [9]
list_2[0] = 13
# Lista została zmodyfikowana na [13]
# Po modyfikacji wartości w liście, te nazwy, które wskazywały na tą listę, nadal wskazują na tą listę, tyle, że teraz zmienioną.

print(list_2) # 13
print(list_1) # 13
# charakter referencyjny list - zarówno lista_2 jak i lista_1 będą teraz przechowywać wartość 13
# jedna nazwa została użyta do tego, aby zmodyfikować element w liście. Druga nazwa nadal wskazuje na tę samą listę.