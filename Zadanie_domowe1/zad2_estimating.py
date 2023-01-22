"""
Napisz skrypt pomagający oszacować ile godzin potrzeba na pobranie
danych z sieci o rozmiarze 13 TB, jeżeli wiesz, że plik o rozmiarze 194 MB
udało się pobrać w 5 sekund. Wynik zaokrąglij do pełnych godzin.
"""

from time import sleep


# Elementy zadania
print(
"\n"
"Treść polecenia: \n"
"194 MB pobrało się z sieci w 5 sekund. \n"
"Do pobrania jest plik o rozmiarze 13 TB. \n"
"Pytanie: ile godzin potrzebnych jest na pobranie pliku o wielkości 13 TB? \n",
"\n"), sleep(10)

print("ROZWIĄZANIE:"), sleep(1)



# Przeliczenie 1 TB na 1 MB
print("1 TB = 1 024 × 1 024 × 1 MB = ", str(1_024 * 1_024), "MB \n"), sleep(5)



# Definiowanie funkcji przeliczającej terabajty ma megabajty
# 1. Funkcja przeliczająca liczbę terabajtów na megabajty --> wykorzystywana do dalszych przeliczeń
def plik_TB_ile_to_MB(liczba_TB):
    if(liczba_TB <= 0):
        return print("Wymagane jest wprowadzenie wartości większej niż 0 TB.")
    else:
        return liczba_TB * 1024 ** 2

# 2. Funkcja przedstawiająca słowną informację o przeliczeniu terabajtów na megabajty
def plik_TB_ile_to_MB_slownie(liczba_TB):
    if(liczba_TB <= 0):
        return print(" ")
    else:
        return "Plik liczący " + str(liczba_TB) + " TB mieści " + str(liczba_TB * 1024 ** 2) + " MB."

print(plik_TB_ile_to_MB_slownie(13) + " (" + str(plik_TB_ile_to_MB(1)) + " MB" + " * 13). \n"), sleep(5)



# Tworzenie zmiennej przechowującej ilość MB pobranych na 1 sekundę
mb_na_1sec = 194 / 5 # wyliczenie, ile MB pobiera się na sekundę
print("Jeżeli w ciągu 5 sekund pobrany został plik o wielkości 194 MB, \n"
      "to w ciągu 1 sekundy pobierze się plik o wielkości " + str(mb_na_1sec) + " MB" +
      " (" + str(194) + " MB / " + str(5) + " sekund). \n"), sleep(10)



# Kroki obliczeń:
# 1) ile sekund potrzebne jest na pobranie pliku o wielkości 13 TB wiedząc, że 38.8 MB pobiera się w sekundę.
print("Plik liczący 13 TB, czyli " + str(plik_TB_ile_to_MB(13)) + " MB,"
      + " należy podzieić przez " + str(mb_na_1sec) + " MB, \n"
      + "co pozwoli określić ilość sekund potrzebnych na pobranie pliku: \n"
      + str(plik_TB_ile_to_MB(13)) + " / " + str(mb_na_1sec) + " = "
      + str(round(plik_TB_ile_to_MB(13) / mb_na_1sec, 0)) + "\n"), sleep(10)

# Utworzenie zmiennej przechowującej ilość sekund potrzebną na pobranie pliku o wskazanej liczbie terabajtów
sec_for_downl_TB = round(plik_TB_ile_to_MB(13) / mb_na_1sec, 2)


print("Aby pobrać plik o wielkości 13 TB potrzebne jest "
      + str(round(plik_TB_ile_to_MB(13) / mb_na_1sec, 0)) + " sekund. \n"
      + "Wymagana jest informacja o liczbie godzin potrzebnych na pobranie pliku.\n"), sleep(5)

# 2) zamiana sekund na godziny
print("1 godzina to 60 minut. \n" +
      "1 minuta to 60 sekund. \n" +
      "1 godzina mieści " + str(60 * 60) + " sekund (" + str(60) + " minut * " + str(60) + " sekund). \n"), sleep(5)

sek_w_godz = 60 * 60 #przypisanie wartości do zmiennej okreslającej ilość sekund w godzinie

# 3) wyliczenie ilości godzin potrzebnych na pobranie 13 TB pliku
# funkcja przeliczająca sekundy na godziny
def sek_na_godz(liczba_sek):
    if(liczba_sek <= 0):
        return print("Wymagane jest wprowadzenie wartości większej niż 0.")
    else:
        return liczba_sek * sek_w_godz

print("A więc: \n"
      + str(round(sec_for_downl_TB, 0)) + " sekund pobierania" + " / "
      + str(sek_w_godz) + " sekund (godznię)" + " daje "
      + str(round(sec_for_downl_TB / sek_w_godz, 0)) + " godzin pobierania "
      + "(dokładnie " + str(round(sec_for_downl_TB / sek_w_godz, 2)) + " godzin). \n"
      + "W efekcie daje to " + str(round(sec_for_downl_TB / sek_w_godz / 24, 0)) + " dni. \n"), sleep(10)



# 4. Odpowiedź:
print("Odpowiedź do zadania: \n"
      "Na pobranie danych z sieci danych o rozmiarze 13 TB potrzebne jest "
      + str(round(sec_for_downl_TB / sek_w_godz, 0))
      + " pełnych godzin.")