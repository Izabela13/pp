# pop - procedural orientated programming

stack = [] # najlepszy dla przechowywania elementów - lista

def push(val):
    stack.append(val)

def pop(): # przy pop ściągam ostatni podany element
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)

print(stack) # [3, 2, 1]

print(pop()) # 1
print(pop()) # 2
print(pop()) # 3
# zwracanie od końca. Ostatnia dodana była wartość 1. Wyszła też 1.