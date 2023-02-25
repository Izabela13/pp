# Funkcja, która służy do podliczania

def count_down(whishes = True):
    print("Trzy...")
    print("Dwa... ")
    print("Jeden...")

# w zależności od tego, czy chcemy życzenia czy nie
    if not whishes: # jeżeli nie chcemy życzeń
        return # zostanie zwrócone None.
    print("Szczęśliwego Nowego Roku!")


# count_down()
# count_down(True) # jawnie podajemy parametr
# count_down(whishes=True)
count_down(whishes=False)