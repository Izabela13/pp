"""
1. Wyświetl polski alfabet (tylko małe litery, także litery ze znakami diakrytycznymi)
wraz z punktami kodowymi dla każdej litery.
"""


# 1. Utworzenie alfabetu bez znaków diakrytycznych
alphabet = ""

for i in range(ord("a"), ord("z") + 1):
      alphabet += chr(i)

# print(alphabet) # abcdefghijklmnopqrstuvwxyz


# 2. Ręczne dopisanie polskich znaków diakrytycznych ["ą", "ć", "ę", "ł", "ń", "ó", "ś", "ź", "ż"]
polish_alphabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"


# 3. Wyświetlenie polskiego alfabetu wraz z punktami kodowymi dla każdej litery
print("litera", "|", "punkt kodowy")
print("-" * 21)
for c in polish_alphabet:
    print(c, " " * 4, "|", ord(c))