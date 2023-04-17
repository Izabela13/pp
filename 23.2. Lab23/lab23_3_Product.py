"""
3. Zaprojektuj klasę produktu sklepu internetowego wg wytycznych:
• stwórz klasę o nazwie Product,
• dodaj (prywatne) właściwości jak nazwa, kategoria, cena, rabat w procentach,
• dodaj metodę obliczającą cenę uwzględniającą rabat,
• dodaj metodę sprawdzającą przynależność produktu do danej kategorii,
• dodaj metodę reprezentującą obiekt klasy jako ciąg znaków.
Dodatkowo stwórz grupę produktów z kilku kategorii, ustaw rabat dla produktów z jednej
kategorii i wyświetl listę produktów.
"""

class Product:
    def __init__(self, name, category, price):
        self.__name = name
        self.__category = category
        self.__price = price
        self.__discount_in_percentage = 0

    def set_discount_in_percentage(self, discount_in_percentage):  # metoda ustawiająca rabat
        self.__discount_in_percentage = discount_in_percentage

    def current_price(self):  # metoda obliczająca cenę uwzględniającą rabat
        return round(self.__price * (1 - (self.__discount_in_percentage / 100)), 2)

    def is_specific_category(self, category):  # metoda sprawdzająca przynależność produktu do danej kategorii
        return self.__category == category

    def __str__(self):  # metoda reprezentująca obiekt klasy jako ciąg znaków
        return "{} {} {} zł".format(self.__category, self.__name, self.current_price())


######################################################################################################################


def gap(n):
    return "\t" * n


def show_products(products):
    for p in products:
        print(p)


def bargain(products, category, discount_in_percentage):
    for p in products:
        if p.is_specific_category(category):
            p.set_discount_in_percentage(discount_in_percentage)


def advert(discount, product_category):
    print("Rabat " + str(discount) + "% na wszystkie produkty z kategorii", (product_category).upper() + "!!!")



products = []

products.append(Product("jazzówki \t\t",    "buty do tańca \t\t",   99.99))
products.append(Product("latino \t\t",      "buty do tańca \t\t",   320.00))
products.append(Product("standard \t\t",    "buty do tańca \t\t",   189.90))
products.append((Product("ćwiczki \t\t",    "buty do tańca \t\t",   129.99)))
products.append(Product("spodenki \t\t",    "odzież taneczna \t",   39.99))
products.append(Product("legginsy \t\t",    "odzież taneczna \t",   49.99))
products.append(Product("saszetka \t\t",    "akcesoria \t\t\t",     29.99))
products.append(Product("drapak \t\t",      "akcesoria \t\t\t",     19.99))


print()
print("PRODUKTY W STANDARDOWEJ CENIE:")
print("-" * 50)
print("KATEGORIA", gap(3), "PRODUKT", gap(2), "CENA")
print("-" * 50)
show_products(products)

print("\n")
advert(15, "akcesoria")
print("PRODUKTY:")
print("-" * 50)
print("KATEGORIA", gap(3), "PRODUKT", gap(2), "CENA")
print("-" * 50)
bargain(products, "akcesoria \t\t\t", 25)
show_products(products)

print("\n")
advert(15, "buty do tańca")
print("PRODUKTY:")
print("-" * 50)
print("KATEGORIA", gap(3), "PRODUKT", gap(2), "CENA")
print("-" * 50)
bargain(products, "buty do tańca \t\t", 50)
show_products(products)