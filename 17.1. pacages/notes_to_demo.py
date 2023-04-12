"""
Pakiet najprościej stworzyć przez wybranie "Python Package". PyCharm tworzy folder o nazwie "package1", a w nim od razu
plik __init__.py. Ten plik jest pusty.



1. TWORZENIE PAKIETU I DWÓCH MODUŁÓW

W package1 umieszczamy dwa pliki Python file:
- module1
- module2

W obu modułach zamieszczamy te same funkcje o tych samych nazwach. Będzie nam to sugerowało, że przez stworzenie modułów
będzie można poradzić sobie z kolizją nazw.

    def introduce():
        print("Jestem funkcją z modułu " + __name__)

Ta funkcja będzie printować napis, mówiący, z którego pochodzi modułu.



2. PIERWSZA APLIKACJA "app1"

Na początku pakiet package1 ma trzy pliki: dwa moduły i jeden plik inicjalizacyjny.
Przechodzimy piętro wyżej i tworzymy aplikację "app1".

W pliku "app1" dokonujemy stosownego importu.

    from package1 import module1
    from package1 import module2

    module1.introduce()
    module2.introduce()

Takie importy dają możliwość wywołania funkcji "introduce()" z modułu "module1" i funkcji "introduce()" z modułu "module2".
Mimo tego, że funkcje mają te same nazwy, robią co innego. Wyprintowane zostaną dwa wyniki:
    ________________________________________
    Jestem funkcją z modułu package1.module1
    Jestem funkcją z modułu package1.module2
    ________________________________________
W module "module1" i w module "module2" mamy dwie różne funkcje, które mają takie same nazwy, ale są w bezpieczny sposób
odseparowane, ponieważ egzystują w innych modułach.



3. TWORZENIE DRUGIEJ APLIKACJI "app2"

W aplikacji "app2" dokonujemy importu z wykorzystaniem aliasów.

    from package1.module1 import introduce as i1
    from package1.module2 import introduce as i2

    i1()
    i2()

Gdyby nie było aliasów, wówczas pojawiłby się problem, ponieważ nazwy funkcji pokrywają się ("introduce()").
Po uruchomieniu pliku okaże się, że bez użycia aliasów drugi import nadpisze pierwszy import.
W tym momencie nie wiadomo, jak odwołać się do pierwszej funkcji.
Aliasowanie pozwala pozbyć się problemu. Za pomocą aliasu można odwołać się do obu funkcji z obu modułów.
    ________________________________________
    Jestem funkcją z modułu package1.module1
    Jestem funkcją z modułu package1.module2
    ________________________________________
Wyprintowanie tego, co zwróci funkcja dir() wyświetli bieżącą przestrzeń nazw - do czego mamy dostęp w tym pliku.

    print(dir())
    ________________________________________________________________________
    ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
    '__loader__', '__name__', '__package__', '__spec__', 'i1', 'i2']
    ________________________________________________________________________

Nazwy "i1" oraz "i2" zostały udostępnione przez import z odpowiednich modułów, które zostały zaimportowane
z odpowiednich pakietów.



4. ZMIANA LOKALIZACJI NASZEGO PAKIETU

Co by się stało, gdyby pakiet znajdował się w innej lokalizacji, np. nie w naszym projekcie?
Folder może znajdować się w innym miejscu, natomiast potrzebujemy ścieżkę do tego miejsca.

C:\Kursy\Python\packages



5. TWORZENIE TRZECIEJ APLIKACJI "app3" - IMPORTOWANIE PLIKÓW Z ZEWNĄTRZ Z FOLDERU

Aby dokonać importu plików z zewnątrz trzeba dopisać odpowiednią ścieżkę, w której zostanie wskazana lokalizacja plików.
Do tego potrzebny będzie moduł systemowy "sys".

    import sys

    # sys.path.append("\\\\fs1\\FolderRedir-Student\\jajkiewi\\Desktop\\packages")
    # ścieżka dostępu do plików na pulpicie na komputerze uczelnianym

    sys.path.append("C:\\Kursy\\Python\\packages")
    # Poszczególne sekcje oznaczone są backslashem. Przed każdym backslashem trzeba wstawić dodatkowy backslash

    from package2 import module1
    module1.introduce()

Z pakietu 2 "package2" importujemy moduł 1 "module1". Nazwy świecą się na czerwono ze względu na to, że PyCharm nie
jest w stanie zorientować się, że wszystko jest w porządku.

Pakiet może być również archiwum ZIP.



6.TWORZENIE CZWARTEJ APLIKACJI "app4" - IMPORTOWANIE PLIKÓW Z ZEWNĄTRZ Z ZIPU

Znowu importujemy moduł "sys". Dodajemy do listy ścieżek plik zip.
W przypadku wskazywania jako źródła pliku zip trzeba podać dokładnie, o jaki plik zip chodzi.

    import sys

    # Lokalizacja pliku zip na komputerze uczelnianym:
    # sys.path.append("\\\\fs1\\FolderRedir-Student\\jajkiewi\\Desktop\\package2.zip")

    sys.path.append("C:\\Kursy\\Python\\packages\\package2_2.zip")

    from package2 import module1
    module1.introduce()



7.KONFIGURACJA PAKIETÓW

Ścieżkę dostępu do pakietów skonfigurować. Wystarczy utworzyć folder, w którym będą umieszczane wszystkie pakiety.
IDE zaciągnie pakiety ze wskazanej lokalizacji.

W prawym dolnym rogu PyCharma mamy link do naszego interpretera. Interpreter w tym przypadku to Python 3.11.
Poniżej znajduje się "Interpreter Settings". W "Interpreter Settings" --> Show All --> Python 3.11 --> + -->
dodanie ścieżki do folderu.



7.TWORZENIE APLIKACJI "app5"

Importowanie pakietów

    from package2 import module1

    module1.introduce()



8. WYKORZYSANIE PLIKU "demo" DO PRZEPROWADZENIA TESTÓW

Wchodzimy do pliku "__init__.py" i dopisujemy jakiś print().

    print("#" * 21)
    print("# Pakiety są super. #")
    print("#" * 21)

Plik "__init__.py" wywoływany jest za każdym razem, gdy importujemy pakiet albo jakiś element pakietu.
Plik "__init__.py" wywoływany jest tylko raz (jeżeli jakiś pakiet zostanie zaimportowany np. 3 razy,
plik wywoła się tylko raz).
    _____________________
    #####################
    # Pakiety są super. #
    #####################
    _____________________

Po uruchomieniu programu w aplikacji "app1", podczas importu pojawia się napis "Pakiety są super!".
Napis został wygenerowany dlatego, że został umieszczony w pliku "__init__.py" i to podczas importu zostało wykonane.
Napis został wyświetlony tylko raz, mimo że dokonywaliśmy dwóch importów:
- from package1 import module1
- from package1 import module2

W każdej kolejnej aplikacji przy imporcie wygenerowany zostanie ten sam napis.



8. SUBPAKIETY - PAKIET W PAKIECIE - PODPAKIET

W subpakiecie automatycznie wygeneruje się plik "__init__.py", który będzie pusty. Dodajemy do niego print.

    print("To jest inicjalizacja podpakietu.")



9. TWORZENIE APLIKACJI "app6"

    import package1                                 # Pojawi się napis "Pakiety są super!"
    from package1 import module1                    # Mamy dostęp do pakietu 1 "package1"
    from package1.subpackage1 import module1 as m   # Zostanie zainicjalizowany podpakiet
"""