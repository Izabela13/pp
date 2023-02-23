"""
Napisz program, który rozszyfruje poniższą wiadomość: Xq|`gf(bm{|(nibfq)
Dla każdego znaku zmieniono 4 bit na przeciwny.
4-ty bit - bit liczymy od najmniej znaczącego (to jest indeks 3)
"""

# print("c") # znaki w ASCI reprezentowane są przez wartości liczbowe.
# print(ord("c")) # funkcja ord pokaże wartość liczbową znaku "c"
## dla znaku "c" wartość w tabeli ASCI to 99. Ta liczba na pewno jest zapisana bitowo.
# print(bin(ord("c"))) # 0b1100011

# print(chr(99)) # 99 w tabeli ASCI to "c". Można to wyświetlić za pomocą funkcji chr (od "character")
# # reprezentacja bitowa:
# print("{:08b}".format(ord("c"))) #01100011

# # 01100011 - to mamy, wiemy, że zmieniony jest czwarty znak
# # 01101011 - to otrzymamy po zmianie czwartego znaku
# # sama alternatywa rozłączna nie pomoże.
# # 00001000
# # Bit, który chcemy zmienić za pomocą alternatywy rozłącznej musimy wyizolować, czyli
# # wskazać, że chcemy operować na jednym bicie. Nie zależy nam zmiana pozosotałych bitów.
# # Chcemy wskazać, że interesuje nas jeden, konkretny bit.


# # 01100011 - nasza liczba
# # 00001000 - nasza maska
# # Nazywa się to "maską" dlatego, że tą jedynką maskujemy te bity, które nas interesują i na których chcemy wykonać daną operację.
# # --------
# # 01101011 - to chcemy dostać - potrzebujemy alternatywy rozłącznej - XOR, aby dojść do zamiany obiektów

# # Zmieniamy na przeciwne tylko te bity, które podamy z zakodowaną maską

# # Jak wygenerować maskę? Wziąć 1 i przesunąć bit operatorem przesunięcia w lewo do pozycji, która nas interesuje
# print("{:08b}".format(1 << 3)) #00001000 # przesunięcie wartości 1 na czwarty bit (na bit o indeksie 3).
# print("{:08b}".format(ord("c") ^ (1 << 3))) # 01101011
# print(chr(ord("c") ^ (1 << 3))) # k

msg = "Xq|`gf(bm{|(nibfq)" # zapisanie jako message

# W pętli nastąpi iteracja. Każdy znak ze zmiennej msg wejdzie do pętli
# Każdy znak zostanie zamieniony na serię bitów, porównany z maską i odczytany jako znak.
for c in msg:
    print(chr(ord(c) ^ (1 << 3)), end = "") #chr - chcemy otrzymywać znaki, ord - chcemy zamienić znak na bit
# rozwiązanie: Python jest fajny!
