# # pętla for iteruje po sekwencjach

# # Polecenie: Wyświetl wszystkie cyfry od 1 do 10.

# i = 1 # zmienna i tworzona jest na zewnątrz pętli. Zmienna nie tyczy się tylko pętli, ale całego skryptu.
# while i < 10: # pętla while będzie wyświetlała wszystkie cyfry do momentu, gdy i będzie mniejsze niż 10
#     print(i, end=" ") # program ma wyświetlić cyfry w jednej linii (bez end = " " cyfry wyświętlą się jedna pod drugą)
#     i += 1 #zwiększanie o jeden (inkrementacja)
# # Wynik: 1, 2, 3, 4, 5, 6, 7, 8, 9
#
# # Jeżeli powyższa pętla nie będzie uwględniać inkrementacji, wówczas dopóki proces nie zostanie ręcznie przerwany,
# # dopóty będą się wyświetlać same jedynki (ponieważ początkowe i = 1).


# # Dokładnie ten sam przykład zostanie zrealizowany za pomocą pętli for
# for i in range(0, 10): #zakres od 0 do 10, po kolei będą pojawiać sie wartości #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#     print(i, end=" ") # za każdym razem jest sprawdzany warunek, czy i jest mniejsze od 10

# # W przypadku pętli for nie trzeba dbać o zdefiniowanie zmiennej "i". Zmienna "i" zostaje automatycznie zdefiniowana.
# # W przypadku pętli for zmienna "i" to zmienna "lokalna". Zmienna "i" będzie miała po kolei przypisywane wartości z pętli.
# # range(0, 10) oznacza wartości od 0 do 10-1, bo wartość końcowa nie wchodzi do zakresu.
# # Pętla będzie wykonywana do momentu, dopóki zmienna "i" będzie mniejsza od 10. Przy i = 10 pętla się nie wykona.



# # funkcja range

# # funkcję range() można użyć z jednym argumentem
# for i in range(10): #będzie to to samo co range(0, 10, 1)
#     print(i)

# for i in range(3, 10, 3): # generator zaczyna od 3, kończy na 10 i skacze co 3
#     print(i)
# # początek to 3
# # dopóki i mniejsze od 10
# # skaczemy co 3


# for i in range(9, -1, -1):
#     print(i) # zamiast incrementować, będą ją dekrementować

for i in range(9, -10, -1):
    print(i)
# start i = 9
# dekrementacja - skok o -1 --> czy i > -10? Jeśli tak, to leć dalej