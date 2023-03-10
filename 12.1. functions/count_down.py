# Funkcja, która służy do odliczania

def count_down(whishes = True): # Parametr "czy chcesz życzenia". Parametr ustawiony domyślnie na "True".
    print("Trzy...")
    print("Dwa... ")
    print("Jeden...")

# w zależności od tego, czy chcemy życzenia noworoczne, czy nie
    if not whishes: # jeżeli nie chcemy życzeń
        return # zostanie zwrócone None.
    print("Szczęśliwego Nowego Roku!") # jeżeli chcemy życzenia, to program przejdzie dalej i wdrukują się życzenia.


# count_down() # z wartością domyślną - pojawiają się życzenia
# count_down(True)
# count_down(whishes=True) # jawnie podajemy parametr, że chcemy mieć parameter "wishes" ustawiony na "True"
count_down(whishes=False)

# Jeżeli nie chcemy życzeń, to "return", tutaj "nic".
print(count_down(whishes=False)) # Na końcu pojawi się "None"