from PieceProv import Pawn, Rook, Bishop, Queen, King, Knight
from coordinates import Coordinate


class Board:
    def __init__(self):
        self.turn = True  # if turn==True, White plays, if turn==False, Black plays
        self.board = [None] * 8  # Init of a 8x8 matrix, filled with "None" values.
        for i in range(8):
            self.board[i] = [None] * 8
        x = 0  # Declare x a y, int values, that makes an easier declaration of the piecec
        y = 0  # on the 8x8 matrix
        self.board[x][y] = Rook(y, x, True)
        self.board[x][7 - y] = Rook(y, x, True)
        self.board[7][y] = Rook(y, x, False)
        self.board[7][7 - y] = Rook(y, x, False)
        y = y + 1
        self.board[x][y] = Knight(y, x, True)
        self.board[x][7 - y] = Knight(y, x, True)
        self.board[7][y] = Knight(y, x, False)
        self.board[7][7 - y] = Knight(y, x, False)
        y = y + 1
        self.board[x][y] = Bishop(y, x, True)
        self.board[x][7 - y] = Bishop(y, x, True)
        self.board[7][y] = Bishop(y, x, False)
        self.board[7][7 - y] = Bishop(y, x, False)
        y = y + 1
        self.board[x][y] = Queen(y, x, True)
        self.board[7][3] = Queen(y, x, False)
        y = y + 1
        self.board[x][y] = King(y, x, True)
        self.board[7][4] = King(y, x, False)
        y = 0
        x = 1
        while y != 8:
            self.board[x][y] = Pawn(y, x, True)
            self.board[7 - 1][y] = Pawn(y, x, False)
            y = y + 1

    def setCoord(self, Coord, Piece):
        self.board[Coord.getY()][Coord.getX()] = Piece

    def getOnCoord(self, Coord):
        return self.board[Coord.getY()][Coord.getX()]

    def showW(self):
        print("")
        n = 8
        for i in reversed(self.board):
            print(n, end=" ")
            for j in reversed(i):
                if j is None:
                    print("[ ]", end=" ")
                else:
                    j.name()
            print("")
            n = n - 1
        print("   A   B   C   D   E   F   G   H ")
        print("")

    def showB(self):
        print("")
        n = 1
        for i in self.board:
            print(n, end=" ")
            for j in i:
                if j is None:
                    print("[ ]", end=" ")
                else:
                    j.name()
            print("")
            n = n + 1
        print("   H   G   F   E   D   C   B   A ")
        print("")

    def play(self, coordinate_orig, coordinate_dest):
        # 0º Condition: there is a piece in the Origin Coordinates
        if self.getOnCoord(coordinate_orig) is None:
            return print("!>>invalid move: there is not a piece in the Origin coordinates given")

        # 1º Condition: The selected Piece is from your team
        PieceAux = self.getOnCoord(coordinate_orig)
        if PieceAux.getColor() != self.turn:
            return print("!>>invalid move: The piece selected it's not from your team")

        # 2º Condition: If there is a piece in the Destiny, its an enemy
        if self.getOnCoord(coordinate_dest) is not None:
            PieceAux2 = self.getOnCoord(coordinate_dest)
            if PieceAux.getColor() == PieceAux2.color:
                return print("!>>invalid move: there is a piece of your team in the destiny coordinates given")

        # 3º Condition: The move is allowed for the piece selected (Also treating pawn's special diagonal move)
        if PieceAux is Pawn and PieceAux2 is not None:
            PieceAux.canMove(2, 3, True)
        elif not PieceAux.canMove(2, 2):
            return print("!>>invalid move: move not allowed for piece ", {PieceAux.getType()})

        # 4º Condition: There is not a Piece blocking your move (Not including Knight)
        # valid = True
        # for j in i:
        #     if self.getOnCoord(j) is not None:
        #         valid = False
        #         break
        # if valid is False:
        #     return print("!>>invalid move: There is a piece blocking your move")

        # ?º Condition: Your king is on check (This does not mean you have to move only the king)

        # ?º Condition: The Piece movement isn't leaving your king in checkmate

        self.setCoord(coordinate_dest, PieceAux)
        self.setCoord(coordinate_orig, None)
        # PieceAux.setPos(coordinate_dest)
        self.turn = not self.turn

# Pruebas:

# tablero = Board()
# tablero.showW()
# tablero.play(Coordinate(4, 0), Coordinate(4, 3))
# tablero.showW()
# tablero.play(Coordinate(4, 6), Coordinate(4, 7))
# tablero.showW()

# ANTIGUO PLAY, POR SI LO NECESITO DESPUES
# def play(self, OrigX, OrigY, DestX, DestY):
#     if self.board[OrigY][OrigX] is None:
#         return print("!>>invalid move: there is not a piece in the Origin coordinates given")
#     PieceAux = self.board[OrigY][OrigX]
#     if self.board[DestY][DestX] is not None:
#         PieceAux2 = self.board[DestY][DestX]
#         if PieceAux.color == PieceAux2.color:
#             return print("!>>invalid move: there is a piece of your team in the destiny coordinates given")
#     if not PieceAux.canMove(DestY, DestX):
#         return print("!>>invalid move: move not allowed for piece ", {PieceAux.getType()})
#
#     self.board[DestY][DestX] = PieceAux
#     self.board[OrigY][OrigX] = None
#     PieceAux.setPos(DestY, DestX)
#     self.turn = not self.turn
