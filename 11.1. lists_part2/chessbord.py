# # PLANSZA DO GRY W SZACHY

# # szachy - plansza 8 x 8

# #       A  B  C  D  E  F  G  H
# #   1   #  #  #  #  #  #  #  #
# #   2   #  #  #  #  #  #  #  #
# #   3   #  #  #  #  #  #  #  #
# #   4   #  #  #  #  #  #  #  #
# #   5   #  #  #  #  #  #  #  #
# #   6   #  #  #  #  #  #  #  #
# #   7   #  #  #  #  #  #  #  #
# #   8   #  #  #  #  #  #  #  #

# # Nasza plansza będzie zawierała po dwie kreski w każdym polu. W dwóch kreskach zmieszczą się dwie litery, które
# # będą symbolizowały piony lub figury.

# # Listy i wyrażenie listowe zagnieżdżone
# chess_row = ["--" for i in range(8)] # szachowy wiersz, który będzie zawierał 8 elementów "--"
# chessboard = [chess_row[:] for i in range(8)] # weź wycinek z chess_row, utwórz kopię --> wszystkie listy będą oddzielnymi listami
# # Wynik: 8 list, które zawierają 8 ciągów znaków "--"

# # Gdzie tu jest błąd w rozumowaniu przy takim sposobie reprezentowania szachownicy: chessboard = [chess_row for i in range(8)]?
# # Jeżeli postawimy pion/ figurę na jednym polu, to będzie on/ ona w całej kolumnie.
# # Propozycja rozwiązania: użycie kopii listy --> [chess_row[:]


# definiowanie pionów:
WHITE_POWN = "WP"
BLACK_POWN = "BP"

# Wyrażenie listowe w wyrażeniu listowym
chessboard = [["--" for i in range(8)] for i in range(8)] # to wyrażenie zostanie za każdym razem wywołane

#          W  K    liczenie od 0
chessboard[0][0] = WHITE_POWN
chessboard[3][5] = BLACK_POWN

for chess_row in chessboard:            # pierwsza pętla będzie brała wiersze
    for chess_square in chess_row:      # druga pętla będzie brała pole
        print(chess_square, end=" ")    # odseparowanie znaków od siebie
    print() # enter na zakończenie wyświetlania