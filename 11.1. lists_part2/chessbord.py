# szachy - plansza 8 x 8

#       A  B  C  D  E  F  G  H
#   1   #  #  #  #  #  #  #  #
#   2   #  #  #  #  #  #  #  #
#   3   #  #  #  #  #  #  #  #
#   4   #  #  #  #  #  #  #  #
#   5   #  #  #  #  #  #  #  #
#   6   #  #  #  #  #  #  #  #
#   7   #  #  #  #  #  #  #  #
#   8   #  #  #  #  #  #  #  #

# chess_row = ["--" for i in range(8)] # szachowy wiersz, który będzie zawierał 8 elementów
# chessboard = [chess_row[:] for i in range(8)] # weź wycinek z chess_row, utwórz kopię --> wszystkie listy będą oddzielnymi listami

# definiowanie pionów:
WHITE_POWN = "WP"
BLACK_POWN = "BP"

chessboard = [["--" for i in range(8)] for i in range(8)] # to wyrażenie zostanie za każdym razem wywołane

chessboard[0][0] = WHITE_POWN
chessboard[3][5] = BLACK_POWN

for chess_row in chessboard:
    for chess_square in chess_row:
        print(chess_square, end=" ") # odseparowanie znaków od siebie
    print() # enter na zakończenie wyświetlania