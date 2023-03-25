list1 = []

# while True:
#     word = input("Podaj wyraz: ")
#     if word == "":
#         break
#     else:
#         list1.append(word)
#
# print(list1)


animals_dict = {}

words = ["kot", "lew", "chomik"] # lista słów, których znaczenie chcę sprawdzić w języku angielskim
for word in words:  # przechodzenie po liście za pomocą pętli for (wyciąganie słówka z listy słówek)
    if word in animals_dict:  # sprawdzenie: jeżeli "słówko" jest w słowniku, to...
        print(word, "->", animals_dict[word]) # ... wyciągnij słówko (odwołaj się do słownika po kluczu "word")
    else:
        print("Nie znaleziono słowa", word,  "w słowniku.")

print([i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0])