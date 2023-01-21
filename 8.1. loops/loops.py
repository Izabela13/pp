# pętla for iteruje po sekwencjach

#Wyświetl wszystkie cyfry

# i = 1
# while i < 10: # czy kod zostanie wykonany
#     print(i, end=" ")
#     i += 1 #zwiększanie o jeden


# for i in range(0, 10): #zakres od 0 do 10, po kolei będą pojawiać sie wartości #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#     print(i, end=" ") # za każdym razem jest sprawdzany warunek, czy i jest mniejsze od 10


#funkcja range
# for i in range(10): #będzie to to samo co range(0, 10, 1)
#     print(i)

# for i in range(3, 10, 3):
#     print(i)
# początek to 3
# dopóki i mniejsze od 10
# skaczemy co 3


# for i in range(9, -1, -1):
#     print(i) # zamiast incrementować, będą ją dekrementować

for i in range(9, -10, -1):
    print(i)
# start i = 9
# dekrementacja - skok o -1 --> czy i > -10? Jeśli tak, to leć dalej