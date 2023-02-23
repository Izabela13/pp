# iterowanie po listach

# pętla for - iterowanie po indeksach

fruits = ["banan", "jabłko", "czereśnia"]

for i in range(len(fruits)): # funkcja len() zwróci ilość elementów - tyle razy przejdę przez pętlę, ile mam elementów w liście.
    print(fruits[i]) # odwołuję się do każdego owocu za pomocą jego indeksu

print()

for i in range(len(fruits)):
    print(i, fruits[i]) # odwołuję się do każdego owocu za pomocą jego indeksu, mogę też wyświetlić ten indeks.

print()

# Pętla for bez indeksów:

for f in fruits: # iteracja po liście "tak po prostu"
    print(f) # nie mam tutaj dostępu do indeksów
