"""
1. Wyświetl polski alfabet (tylko małe litery, także litery ze znakami diakrytycznymi)
wraz z punktami kodowymi dla każdej litery.
"""

alphabet = ""

for i in range(ord("a"), ord("z") + 1):
      alphabet += chr(i)

print(alphabet)

#polish_signs = ["ą", "ć", "ę", "ł", "ń", "ó", "ś", "ź", "ż"]
polish_signs = "ąćęłńóśźż"

polish_alphabet = alphabet + polish_signs
print(polish_alphabet)

for letter in polish_alphabet:
    print(letter, end= " ")
print()
for letter in polish_alphabet:
    print(ord(letter), end=" ")