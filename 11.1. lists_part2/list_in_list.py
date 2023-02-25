numbers = [1, 2, 3]
print(numbers)

matrix = [numbers[:], numbers[:]]

l2 = numbers
print(l2)

# lista w liście
l2 = [numbers] # zagnieżdżenie listy w liście
print(l2) # [[1, 2, 3]]

l2 = [numbers, numbers] # zagnieżdżenie listy w liście
print(l2) # [[1, 2, 3], [1, 2, 3]]

numbers[0] = 99

print(l2) # [[99, 2, 3], [99, 2, 3]]


print(matrix) #[[1, 2, 3], [1, 2, 3]]