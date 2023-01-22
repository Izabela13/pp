# Liczba produkcji monet półdolarowych dla lat 2012, 2013 i 2014 w Denver i w Philadelphi

denver = [1_700_000, 4_600_000, 2_100_000]
philadelphia = []

philadelphia.append(1_800_000)
philadelphia.append(5_000_000)
philadelphia.append(2_500_000)

total = [0, 0, 0] # trzy elementy ustawione na razie na zera
total[0] = denver[0] + philadelphia[0]
total[1] = denver[1] + philadelphia[1]
total[2] = denver[2] + philadelphia[2]

average = (total[0] + total[1] + total[2]) / len(total)

print("{:,d}".format(total[0]).replace(",", " "))

print("Produkcja w roku 2012 wyniosła", "{:,d}".format(total[0]).replace(",", " "), "sztuk.")
print("Produkcja w roku 2013 wyniosła", "{:,d}".format(total[1]).replace(",", " "), "sztuk.")
print("Produkcja w roku 2014 wyniosła", "{:,d}".format(total[2]).replace(",", " "), "sztuk.")


