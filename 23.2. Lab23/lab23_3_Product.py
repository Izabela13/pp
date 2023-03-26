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
    # def __init__(self, name, category, price, discount_in_percentage):
    #     self.__name = name
    #     self.__category = category
    #     self.__price = price
    #     self.__discount_in_percentage = discount_in_percentage
    def __product_features(self, name, category, price, discount_in_percentage):
        print("To jest metoda prywatna...")

    def my_public_method(self):
        self.__my_private_metod()
        print("To jest metoda publiczna")
