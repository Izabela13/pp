"""
1. Napisz wyszukiwarkę numerów telefonów:
• zdefiniuj słownik par imię -> numer telefonu,
• zapytaj użytkownika o imię,
• wyświetl użytkownikowi numer telefonu lub informacje o jego braku.
"""

phone_numbers = \
         {"Tomek": 345123456,
          "Ada":   123123123,
          "Karol": 321654978}

phone_search = input("Podaj imię, aby wyświetlić numer telefonu do osoby: ")

if phone_search in phone_numbers:
    print("Numer telefonu:", phone_numbers[phone_search])
else:
    print("Brak numeru telefonu do wyświetlenia.")