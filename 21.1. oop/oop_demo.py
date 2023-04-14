# TWORZENIE KLAS OBIEKTÓW

class MyClass:  # notacja UpperCamelCase
    pass  # zaślepka

# Tworzenie obiektu dla nowo powtałej klasy. Obiekty tworzymy podobnie jak tworzy się zmienne.
my_obj = MyClass()  # obiekt ma nazwę i jest klasy "MyClass", którą zapisujemy jak funkcję.
# Jest to skrypt w pełni obiektowy.


# W klasie nie uwzględniliśmy żadnych właściwości, ale obiekt może posiadać jakąś właściwość.
# Za pomocą notacji kropkowej możemy nadać obiektowi "my_obj" jakąś właściwość i wprowadzić jakąś wartość.
my_obj.x = 5  # od tej pory obiekt "my_object" ma właściwość "x", do której przypisana jest wartość "5".
print(my_obj.x)      # za pomocą instrukcji print() możemy wyświetlić właściwość obiektu "my_obj".
print(type(my_obj))  # jakiego typu jest obiekt:  <class '__main__.MyClass'>


my_obj2 = MyClass()  # Kolejny obiekt klasy "MyClass".
my_obj2.x = 99       # Przypisanie właściwości "x" do obiektu "my_obj2", ale tym razem wartość właściwości to 99
print(my_obj2.x)


# W skrypcie są dwa obiekty: "my_obj", który ma właściwość 5, i "my_obj2", który ma właściwość 99.
print(my_obj.x, my_obj2.x)  # 5 99
# Mimo że obiekty są tej samej klasy i tego samego typu, mają unikatowe właściwości.