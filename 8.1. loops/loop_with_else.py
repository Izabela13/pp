for i in range(5): # pętla będzie sie kręcić, dopóki i będzie mniejsze od 5
    print(i) # pętla wyświetli kolejno: 1, 2, 3, 4,
else:
    print("Koniec pętli...") # na samym końcu pojawi się dopisek "Koniec pętli".

# klauzula "else" wykona się, jeśli nie zostanie przerwana dyrektywą break lub return

for i in range(5):
    print(i)
    if (i == 3):
        break # wychodzimy z pętli i nie wykona się instrukcja else
else:
    print("Koniec pętli...")