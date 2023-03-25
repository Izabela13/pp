# txt = "Ala ma kota."
#
# print(len(txt)) #12
# print(txt[-1])  #.
#
# print(len(""))        # 0
# print(len("\t\n\\"))  # 3: tabulator + znak nowej linii + backslash
#
#
# txt = "To jest tekst."\
#       "To dalszy ciąg."
# print(txt) # To jest tekst.To dalszy ciąg.
#
#
# txt = """To jest tekst."\
#       "To dalszy ciąg."""
# print(txt) # To jest tekst."      "To dalszy ciąg.
#
#
# text = """a
# b
# c"""
#
# text2 = "a\nb\bc"
#
# print(txt)
# print(text2)
#
#
# # KONKATENACJA I REPLIKACJA
#
# str1 = "a"
# str2 = "b"
#
# print(str1 + str2) #ab
# print(str2 + str1) #ba
# print()
# print(str1 * 3) #aaa
# print(5 * str2) #bbbbb
#
# str1 += str2
# print(str1) # ab
#
#
# str1 *= 10
# print(str1) # abababababababababab


# STRING JAKO ŁAŃCUCH ZNAKÓW:
txt = "Ala ma kota."

# print(txt[2]) # a
# print(txt[-3]) # o

# Indeksy

for i in range(len(txt)):
      print(txt[i], end=" -") # A -l -a -  -m -a -  -k -o -t -a -. -

for c in txt:
      print(c)


# WYCINKI
print(txt[4:6]) # wycinanie "ma"
print(txt[7:]) # wycinanie "kota"
print(txt[-1:]) # .
print(txt[2::3]) #aao


#Drukoanie alfabetu
print(ord("a"))
print(ord("z"))

alphabet = ""

for i in range(ord("a"), ord("z") + 1):
      alphabet += chr(i)
      #print(chr(i), end="") # abcdefghijklmnopqrstuvwxyz
# Alfabet bez polskich znaków

print(alphabet)

print("a" in alphabet) # True
print("abce" in alphabet) # False


# # Niemutowalność
# # del alphabet[0] # TypeError
# # Nie można usuwać pojedynczego znaku

# del alphabet # można usuwać stringi za pomocą metody del
# print(alphabet) # pojawi się NameError - nie można odwołać się do nazwy.

# alphabet.append("asbss") nie wolno używać metody append, ani update


# Do stringów można dodawać pojedyncze znaki - za każdym razem tworzymy nowy obiekt w pamięci
alphabet += "AAAA"
print(alphabet) #abcdefghijklmnopqrstuvwxyzAAAA


# Funkcje MIN i MAX
print(min([1, 2, 3])) # 1
print(max([1, 2, 3])) # 3
print()
print(min("abcABC")) # A - wartość kodowa - duże "A" ma mniejszą wartość niż małe "a"
print(max("abcABC")) # c - wartość kodowa - małe "c" ma największą wartość kodową
print()
print(max("Ala ma kota")) #t - wartość punktu kodowego = 116

print(alphabet.index("w")) # literka "w" ma indeks 22
print("aAbByYzZAa".index("A")) # 1 - funkcja indeks zwraca indeks pierwszego wystąpienia argumentu
print("aAbByYzZAa".index("ZA")) # 7 -
print([1, 2, 3].index(3))
print(list(alphabet))
print(alphabet.count("a"))
print("Ala ma kota.".count("a"))

print([1, 1, 2, 2, 4].count(1))