# OPERATORY LOGICZNE I BITOWE

# Jeżeli temperatura będzie dodatnia i będzie słonecznie, to...
# pójdziemy na spacer.
# jeśli nie - zostaniemy w domu

temperature = 12
is_sun_shining = False # słońce nie świeci --> False - is_sun_shining samo ewaluuje do wartości logicznej

# złożone wyrażenie logiczne z zastosowaniem operatorów logicznych
# zastosowanie operatora 'and'
if temperature > 0 and is_sun_shining: #True and False -> False
    print("Idziemy na spacer.")
else:
    print("Zostaniemy w domu.")
# temperatura jest dodatnia, ale nie świeci słońce. Wykona się blok else.
# Aby cały złożony warunek logiczny był prawdą (ewaluował do True), to oba warunki muszą być spełnione.


# zastosowanie operatora 'or' - sumy logicznej
if temperature > 0 or is_sun_shining: #True or False -> True
    print("Idziemy na spacer.")
else:
    print("Zostaniemy w domu.")
# Jak działa operator 'or' w pythonie:
# python próbuje ewaluować pierwszą część wyrażenia logicznego. Jeżeli pierwsza część warunku jest spełniona, to
# niezależnie od tego, czy druga część warunku 'or' jest spełniona, i tak całe wyrażenie logiczne będzie spełnione.
# Jeżeli pierwsza część warunku jest spełniona, to druga nie jest już wykonywana.


# Jeżeli temperatura będzie ujemna lub będzie pochmurno, to zostaniemy w domu,
# a jeżeli nie, to pójdziemy na spacer.
temperature = 12
cloudy = False

if temperature < 0 or cloudy is True:
    print("Zostaniemy w domu")
else:
    print("Idziemy na spacer")

temperature = 12
is_sun_shining = False

if temperature < 0 or not is_sun_shining:
    print("Zostaniemy w domu")
else:
    print("Idziemy na spacer")



# OPERATORY LOGICZNE
# and - koniunkcja - czytamy jak "i"
# or - alternatywa - czytamy jak "lub"
# not - negacja - czytamy jak "nie"

# operatory przy zastosowaniu pętli

# Zadanie: Wyświetl cyfrę, chyba, że:
# liczba parzysta lub liczba większa od 6, to wyświetl *

for i in range(10):
    if i % 2 == 0 or i > 6: #dla 6 i 8 wykonywana jest pierwsza instrukcja
        print("*")
    else:
        print(i)
