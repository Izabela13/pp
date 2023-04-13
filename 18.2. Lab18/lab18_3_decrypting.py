"""
3. Rozszyfruj poniższą wiadomość wiedząc, że została ona zaszyfrowana szyfrem
cezara z parametrem przesunięcia równym 3.
VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ
"""

"""
Alfabet: ABCDEFGHIJKLMNOPRSTUVWXYZ
  Szyfr: DEFGHIJKLMNOPRSTUVWXYZABC
"""


displacement = 3  # parametr przesunięcia
string = "VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ"  # zaszyfrowana wiadomość

# # Zakres
# print(ord("A"))  # 65
# print(ord("Z"))  # 90


def decoding_single_letter(letter, displacement):

    if ord(letter) < ord("A") or ord(letter) > ord("Z"):
        return letter

    decoded_letter = ord(letter) - displacement
    if decoded_letter < ord("A"):
        decoded_letter += ord("Z") - ord("A") + 1
    return chr(decoded_letter)


# # Testy
# print(decoding_single_letter("-", displacement))  # -
# print(decoding_single_letter("A", displacement))  # X
# print(decoding_single_letter("Z", displacement))  # W
# print(decoding_single_letter("C", displacement))  # Z


def decoding(string, displacement):

    decoded_string = ""

    for char in string:
        decoded_string += decoding_single_letter(char, displacement)

    return  decoded_string


print(decoding(string, displacement))
# STUDIA PODYPLOMOWE - PROGRAMISTA PYTHON
