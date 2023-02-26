# słownik

phones = {"Tomek": 345123456,
          "Ada":   123123123,
          "Karol": 999999999,
          "Tomek": 100000000}

print(phones)

# klucz musi być niepowtarzalny, ponieważ jednoznacznie identyfikuje jakąś wartość
# jeżeli jakiś klucz pojawi się jeszcze raz, wówczas zostanie nadpisany
# {'Tomek': 100000000, 'Ada': 123123123, 'Karol': 999999999}


animal_dict = {
    "kot": "cat",
    "pies": "dog",
    "chomik": "hamster"
}

print(animal_dict["kot"])
print(animal_dict.get("kot"))
# z zastosowaniem metody get jest bezpieczniej, bo jak użyjemy wyrazu, którego nie ma,
# zostanie zwrócona wartość None.


# funkcja get ma dodatkowy parameter
print(animal_dict.get("krowa", "Brak takiego słowa")) # metoda zabezpiecza

# do wersji 3.6 słowniki były kolekcjami nieuporządkowanymi.


words = ["kot", "lew", "chomik"] # lista słów, których znaczenie chcę sprawdzić w języku angielskim
for word in words:
    if word in animal_dict:
        print(word, "->", animal_dict[word])
    else:
        print("Nie znaleziono słowa", word,  "w słowniku.")

# Słownik nie jest obiektem sekwencyjnym - nie można po nim iterować, ale można iterować po kluczach

for key in animal_dict.keys(): # nie trzeba zapisywać ".keys" - jest to najczęstsze odwołanie do słowników
    print(key, "->", animal_dict[key])

# metoda values wyciągnie tylko i wyłącznie wartości:
for val in animal_dict.values():
    print(val) # tyle, że nie wyświetlą się klucze

# wyciąganie krotek
for item in animal_dict.items():
    print(item)

for pl, en in animal_dict.items():
    print(pl, "->", en) # działa jak: a, b = (1, 2) ==> a = 1, b = 2


# Chcemy dopisać jakiś element
animal_dict["świnka"] = "pig" # KLUCZ:WARTOŚĆ

print(animal_dict)

# Tak samo zadziała metoda update()
animal_dict.update({"kurczak": "chicken"})
print(animal_dict)

# Modyfikacja
animal_dict.update({"świnka": "piggy"})
# Element nie zmieni swojego położenia, bo klucz już był


# Kopia słownika
dict2 = animal_dict.copy()
print(dict2)


# Usuwanie elementów:
del dict2["świnka"]
print(dict2)

dict2.popitem() # zniknie ostatni element. Za każdym wywołaniem będą usuwane pojedyncze elementy
print(dict2)

dict2.clear() # Wyczyści cały słownik