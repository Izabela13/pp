"""
3. Rozszyfruj poniższą wiadomość wiedząc, że została ona zaszyfrowana szyfrem
cezara z parametrem przesunięcia równym 3.
VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ
"""

code1 = "VWXGLD"
code2 = "SRGBSORPRZH"
code3 = "SURJUDPLVWD"
code4 = "SBWKRQ"

for i in code1:
    if i in ("Y", "Z"):
        print(chr(ord(i) - 25))
    else:
        print((chr(ord(i) + 3)))

print()

for i in code2:
    print(chr(ord(i) + 3), end="")

print()

for i in code3:
    print(chr(ord(i) + 3), end="")

print()

for i in code4:
    print(chr(ord(i) + 3), end="")

