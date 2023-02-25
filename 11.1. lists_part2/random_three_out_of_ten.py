# Wylosuj 3 liczby od 1 do 10, przy czym nie chcemy, aby te liczby się powtarzały.
# Mają być posortowane w kolejności rosnącej.
import random

random_numbers = [] # umieszczanie wylosowanych liczb

# iterowanie tyle razy, ile mamy wylosować liczb
#
# for i in range(3):
#     random_numbers.append(random.randint(1, 10))
# random_numbers.sort()
#
# print(random_numbers)

# randint nie zapewnia unikatowych wartości

# trzeba zmienić pętlę na while - losuj dopóki liczby nie będą sie powtarzać

# counter = 3
#
# while counter: # jeżeli counter będzie 3, wyjdziemy z pętli
#     number = random.randint(1, 10)
#     if number not in random_numbers:
#         random_numbers.append(number)
#         counter -= 1
#
# random_numbers.sort()
# print(random_numbers)
# # problem jest z wydajnością - może się okazać, że program będzie w koło losował tę samą liczbę



# sample - losowanie dowolnej ilości liczb bez powtórzeń
numbers = [i for i in range(1, 11)] # wyrażenie listowe
random_numbers = random.sample(numbers, 3) # zbiór i ile liczb

random_numbers.sort()

print(random_numbers)