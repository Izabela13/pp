class MyClass:
    pass # zaślepka

# Tworzenie obiektu dla klasy
my_obj = MyClass() # obiekt ma nazwę i klasę, którą zapisujemy jak funkcję

# W klasie nie uwzględniliśmy właściwości, ale możemy ją nadać
my_obj.x = 5  # od tej pory obiekt my_object ma x
print(my_obj.x)
# jakiego typu jest obiekt
print(type(my_obj)) # <class '__main__.MyClass'>


my_obj2 = MyClass()
my_obj2.x = 99

print(my_obj2.x)


# W skrypcie są dwa obiekty: obj i obj2
print(my_obj.x, my_obj2.x) # 5 99
# Mimo że obiekty są tej samej klasy, mają unikatowe właściwości