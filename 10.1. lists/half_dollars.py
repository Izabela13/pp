# Liczba produkcji monet półdolarowych dla lat 2012, 2013 i 2014 w Denver i w Philadelphi

# w poszczególnych latach, które będą odpowiadały za indeks 0, 1 i 2 były takie oto wartości:
denver = [1_700_000, 4_600_000, 2_100_000] # produkcja monet w roku 2012, 2013 i 2014
philadelphia = [] # stowrzenie pustej listy

# za pomocą metody i notacji kropkowej dodajemy produkcję monet za lata 2012, 2013 i 2014
philadelphia.append(1_800_000)
philadelphia.append(5_000_000)
philadelphia.append(2_500_000)

# tworzenie statystyk
total = [0, 0, 0] # pomocnicza lista
# trzy elementy ustawione na razie na zera, ale to będzie suma produkcji z Denver i Filadelfii za poszczególne lata.
total[0] = denver[0] + philadelphia[0] # dla zerowego indeksu - suma zerowego indeksu Denver i zerowego indeksu Filadelfii
total[1] = denver[1] + philadelphia[1]
total[2] = denver[2] + philadelphia[2]

# liczenie średniej za wszystkie lata - dodawanie wartości z indeksów 0, 1, 2 oraz dzielenie przez ilość elementów
average = (total[0] + total[1] + total[2]) / len(total)

# print("{:,d}".format(total[0]).replace(",", " ")) # formatowanie zapisu do odstępów przy dużych liczbach

print("Produkcja w roku 2012 wyniosła", "{:,d}".format(total[0]).replace(",", " "), "sztuk.") # 3 500 000
print("Produkcja w roku 2013 wyniosła", "{:,d}".format(total[1]).replace(",", " "), "sztuk.") # 9 600 000
print("Produkcja w roku 2014 wyniosła", "{:,d}".format(total[2]).replace(",", " "), "sztuk.") # 4 600 000
