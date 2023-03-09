"""
3. Napisz skrypt symulujący rozgrywkę gry w szachy, w tym celu:
• stwórz wirtualną szachownicę,
• na wirtualnej szachownicy rozmieść losowo 2. dowolne figury szachowe i 3. piony,
• zaprezentuj użytkownikowi stan wirtualnej szachownicy.
"""
import random

# figury szachowe
WHITE_FIG = "WF"
BLACK_FIG = "BF"

# piony
WHITE_POWN_1 = "WP"
WHITE_POWN_2 = "WP"
BLACK_POWN_1 = "BP"


chessboard = [["--" for i in range(8)] for i in range(8)]
# print(chessboard)


# losowanie pozycji "i" oraz "j"
i = random.randint(1, 7)
j = random.randint(1, 7)
chessboard[i][j] = WHITE_FIG

i = random.randint(1, 7)
j = random.randint(1, 7)
chessboard[i][j] = BLACK_FIG

i = random.randint(1, 7)
j = random.randint(1, 7)
chessboard[i][j] = WHITE_POWN_1

i = random.randint(1, 7)
j = random.randint(1, 7)
chessboard[i][j] = WHITE_POWN_2

i = random.randint(1, 7)
j = random.randint(1, 7)
chessboard[i][j] = BLACK_POWN_1


for chess_row in chessboard:
    for chess_square in chess_row:
        print(chess_square, end=" ") # odseparowanie znaków od siebie
    print() # enter na zakończenie wyświetlania
