a = 3
b = 4
c = 7


print(a < b < c) #True --> równorzędne z zapisem:
print(a < b and b < c)

print()

# W przypadku tego zapisu ewaluacja "b" będzie liczona tylko raz a < b < c

def get():
    print("!")
    return a

print(a < get(b) < c)
print(a < get(b) and get(b) < c)