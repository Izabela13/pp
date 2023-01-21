for i in range(5):
    print(i)
else:
    print("Koniec pętli...")


for i in range(5):
    print(i)
    if (i == 3):
        break # wychodzimy z pętli i nie wykona się instrukcja else
else:
    print("Koniec pętli...")