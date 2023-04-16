# # Zadane 1: student

# class Student:
#     pass

# student1 = Student()  # student1 = obiekt klasy "Student()"
# student2 = Student()  # student2 = obiekt klasy "Student()"
# student3 = Student()  # student3 = obiekt klasy "Student()"

# print(student1, student2, student3)  # Takie obiekty istnieją już gdzieś w pamięci komputera.
# # Moje rozwiązanie jest OK



# # Zadanie 2: three stacks

# class Stack:
#     def __init__(self):
#         self.__stack_list = [] # pusta lista

#     def push(self, val):
#         self.__stack_list.append(val)

#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val

#     def show_val(self):
#         print(self.__stack_list)

# s1 = Stack()
# s2 = Stack()
# s3 = Stack()

# print(s1, s2, s3)

# for i in range(1, 101):
#     s1.push(i)

# s1.show_val()

# for i in range(100):
#     s2.push(s1.pop()) # Do stosu 2 wrzucam wszystkie elementy ze stosu 1

# s2.show_val()

# for i in range(100):
#     s3.push(s2.pop()) # Do stosu 3 wrzucam wszystko to, co ściągam ze stosu 1

# s3.show_val()

# for i in range(100):
#     print(s3.pop(), end=" ")



# Zadanie 3

class Stack:
    def __init__(self):
        self.__stack_list = [] # pusta lista

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def show_val(self):
        print(self.__stack_list)

    def empty(self):
        return len(self.__stack_list) == 0  # Zbadaj ilość elementów na naszym stosie

    def size(self):
        return len(self.__stack_list)

    def top(self):
        if not self.empty():
            return self.__stack_list[-1]
        return None


stack = Stack()  # obiekt "stack" klasy "Stack"
print("Czy stos jest pusty?", stack.empty())
# Czy stos jest pusty? True

stack.push("Ala")
stack.push("Tomek")
stack.push("Agata")

print("\nCzy stos jest pusty?", stack.empty())
print("\nIle elementów jest na stosie?", stack.size())
print("\nNa górze stosu znajduje się:", stack.top())
print("\nIle elementów jest na stosie?", stack.size())
