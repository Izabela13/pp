# generowanie list za pomocą pętli

numbers = [] # pusta lista

# for i in range(1, 1001):
#     numbers.append(i)
#
# print(numbers)


# za pomocą wyrażeń listowych - tę samą pętlę można wykonać w jednej linijce
numbers = [i for i in range(1, 1001)]

print(numbers)


numbers = [99 for i in range(1, 1001)] # te same elementy 1000 elementów z wartością 99

print(numbers)


# można też wykonać jakieś działania:
numbers = [i ** 2 for i in range(1, 101)]
print(numbers)


# dla tego mechanizmu mamy instrukcje warunkowe, które można postawić na samym końcu
numbers = [i ** 2 for i in range(1, 101) if i % 2 == 0] # np. interesują nas tylko liczby parzyste i
print(numbers) # w tym wypadku dostaniemy 50 elementów


# Chcemy dowiedzieć się, ile liczb w przedziale od 1 do 300 dzieli się przez 3 i 7 (jednocześnie)
# całe obliczenie ma być jedną linijką kodu

numbers_choosen = [i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0]
print(len(numbers_choosen))

print(len([i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0]))