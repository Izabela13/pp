#pętla for

fruits = ["banan", "jabłko", "czereśnia"]

for i in range(len(fruits)):
    print(fruits[i]) # odwołuję się do każdego owocu za pomocą jego indeksu

print()

for i in range(len(fruits)):
    print(i, fruits[i]) # odwołuję się do każdego owocu za pomocą jego indeksu

print()

# Pętla for bez indeksów:

for f in fruits:
    print(f)