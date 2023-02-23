# # silnia, np:
# 3! = 1 * 2 * 3 = 6

# number = 5 # 1 * 2 * 3 * 4 * 5
# factorial = 1 # silnia = ang. factorial. Początkowa wartość = 1. Jest to mnożenie, więc nie może pojawić się 0.

# for i in range(1, number + 1): #ten number musi być powiększony do 5
#     factorial *= i
# print(factorial)


# while number:
#     factorial *= number
#     print(number, factorial) # przy takim zapisie pojawi się wszystko, co się dzieje za każdym obrotem pętli.
#     number -= 1 # Zmienna number (czyli 5) za każdym obrotem pętli będzie się zmniejszać do 0.
# # Gdy number dojdzie do 0, wówczas wartością dla pętli while będzie "False" i pętla się zatrzyma.
# # Wynik:
# # 5 5
# # 4 20  (5 * 4)
# # 3 60  (20 * 3)
# # 2 120 (60 * 2)
# # 1 120 (120 * 1
# # na odwrót niż w pętli for - dekrementacja: 5 * 4 * 3 * 2 * 1