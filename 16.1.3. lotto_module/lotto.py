""" MODUŁ DO OBSŁUGI GRY W LOTTO """

from random import sample


""" MECHANIZM I: Funkcja losująca 6 liczb z 49. """
def draw_numbers():
    numbers = [i for i in range(1, 50)]
    lucky_numbers = sample(numbers, 6)
    lucky_numbers.sort()
    return lucky_numbers


""" MECHANIZM II: Funkcja pobierająca od użytkownika zestaw jego liczb. """
def get_user_numbers():
    n = 6
    counter = 1
    user_numbers = []

    while counter < n + 1:
        try:
            number = int(input("Podaj " + str(counter) + " liczbę (1-49): "))
            if number in user_numbers:
                print("Powtórzona liczba!")
                continue
            if number < 1 or number > 49:
                print("Należy podać liczbę z przedziału od 1 do 49!")
                continue
        except:
            print("To nie jest liczba. Proszę podać liczbę całkowitą")
            continue

        user_numbers.append(number)
        counter += 1

    user_numbers.sort()
    return user_numbers


""" MECHANIZM III: Funkcja zliczająca trafione przez użytkownika liczby. """
def check_numbers(user_numbers, lucky_numbers):
    counter = 0
    for number in user_numbers:
        if number in lucky_numbers:
            counter += 1
    return counter


if __name__ == "__main__":
    user_numbers = get_user_numbers()
    lucky_numbers = draw_numbers()
    result = check_numbers(user_numbers, lucky_numbers)
    print(user_numbers)
    print(lucky_numbers)
    print(result)