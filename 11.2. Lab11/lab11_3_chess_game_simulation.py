"""
3. Napisz skrypt symulujący rozgrywkę gry w szachy, w tym celu:
• stwórz wirtualną szachownicę,
• na wirtualnej szachownicy rozmieść losowo 2. dowolne figury szachowe i 3. piony,
• zaprezentuj użytkownikowi stan wirtualnej szachownicy.
"""

import random

print(""
"Symboliczne oznaczenie figur i kolorów w symulacji rozgrywki szachowej: \n"
"1. Kolory: \n"
"• W = WHITE (biały) \n"
"• B = BLACK (czarny) \n"
"\n"   
"2. Figury: \n"
"• P = PAWN   (pionek) \n"
"• H = HORSE  (konik/ skoczek) \n"
"• B = BISHOP (goniec/ laufer) \n"
"• R = ROOK   (wieża) \n"
"• Q = QUEEN  (królowa/ hetman) \n"
"• K = KING   (król) \n")

print(
"Wszystkie dostępne figury dla dwóch graczy: "
"\n ", "WR", "WH", "WB", "WQ", "WK", "WB", "WH", "WR",
"\n ", "WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP",
"\n ", "BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP",
"\n ", "BR", "BH", "BB", "BQ", "BK", "BB", "BH", "BR",
"\n" * 2)



# Stworzenie wirtualnej szachownicy
chessboard = [["--" for i in range(8)] for i in range(8)]
# print(chessboard)



# Listy pionków i figur szachowych
chess_pawns = [
"WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP",
"BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"]

chess_figures = [
"WR", "WH", "WB", "WQ", "WK", "WB", "WH", "WR",
"BR", "BH", "BB", "BQ", "BK", "BB", "BH", "BR"]


# Losowanie 3 pionów i 2 figur
drawn_chess_pawn = random.sample(chess_pawns, 3)
drawn_chess_figures = random.sample(chess_figures, 2)

# Tworzenie listy łączonej
drawn_chess_pieces = drawn_chess_pawn + drawn_chess_figures



# Ustawianie w losowy sposób wylosowanych pionków i figur szachowych
piece = 0

while piece < len(drawn_chess_pieces):
    row = random.randint(0, 7)
    column = random.randint(0, 7)
    if chessboard[row][column] == "--":  # sprawdzanie, czy na planszy jest puste pole, tj. "--".
        chessboard[row][column] = drawn_chess_pieces[piece] # jeśli puste pole, postaw figurę szachową
        piece += 1



# Prezentacja stanu wirtualnej szachownicy
print("Symulacja rozgrywki szachowej. \n"
      "Stan szachownicy: \n")

for row in range(len(chessboard)):
    if row == 0:
        print(" ", "A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ")
    print(row + 1, end=" ")
    for column in range(len(chessboard)):
        print(chessboard[row][column], end=" ")
        if column == 7:
            print(row + 1, end=" ")
    print()
print(" ", "A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ")