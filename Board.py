from PieceProv import Pawn, Rook, Bishop, Queen, King, Knight
from coordinates import Coordinate


class Board:
    def __init__(self):
        self.turn = True  # if turn==True, White plays, if turn==False, Black plays
        whiteKing = King(3, 0, True)
        blackKing = King(3, 7, False)

        self.board = [None] * 8  # Init of a 8x8 matrix, filled with "None" values.
        for i in range(8):
            self.board[i] = [None] * 8
        x = 0  # Declare x a y, int values, that makes an easier declaration of the piecec
        y = 0  # on the 8x8 matrix
        self.board[0][0] = Rook(0, 0, False)  # Initialization of every piece in their ->
        self.board[0][7] = Rook(7, 0, False)  # -> respective position at the start of the game
        self.board[7][7] = Rook(7, 7, True)
        self.board[7][0] = Rook(0, 7, True)

        self.board[0][1] = Knight(1, 0, False)
        self.board[0][6] = Knight(6, 0, False)
        self.board[7][1] = Knight(1, 7, True)
        self.board[7][6] = Knight(6, 7, True)
        y = y + 1
        self.board[0][2] = Bishop(2, 0, False)
        self.board[0][5] = Bishop(5, 0, False)
        self.board[7][2] = Bishop(2, 7, True)
        self.board[7][5] = Bishop(5, 7, True)
        y = y + 1
        self.board[0][3] = Queen(3, 0, False)
        self.board[7][3] = Queen(3, 7, True)
        y = y + 1
        self.board[0][4] = King(4, 0, False)
        self.board[7][4] = King(4, 7, True)
        x=0
        y=7
        # Loop to make easier the initialization of 16 Pawns from both teams, setting their
        # y coordinate still and adding 1 to x in every iteration
        while x != 8:
            self.board[1][x] = Pawn(x, 1, False)
            self.board[6][x] = Pawn(x, 6, True)
            x = x + 1

    def setCoord(self, Coord, Piece):
        if Piece is not None:
            Piece.setPos(Coord.getX(), Coord.getY())
            self.board[Coord.getY()][Coord.getX()] = Piece
        if Piece is None:
            self.board[Coord.getY()][Coord.getX()] = Piece

    def getOnCoord(self, Coord):
        return self.board[Coord.getY()][Coord.getX()]

    def getTurn(self):
        return self.turn

    def showB(self):  # Prints Board in the point of view of the White team
        print("")
        n = 1
        for i in reversed(self.board):
            print(n, end=" ")
            for j in reversed(i):
                if j is None:
                    print("[ ]", end=" ")
                else:
                    j.name()
            print("")
            n = n + 1
        print("   H   G   F   E   D   C   B   A  \n")

    def showW(self):  # Prints Board in the point of view of the Black team
        print("")
        n = 8
        for i in self.board:
            print(n, end=" ")
            for j in i:
                if j is None:
                    print("[ ]", end=" ")
                else:
                    j.name()
            print("")
            n = n - 1
        print("   A   B   C   D   E   F   G   H  \n")

    def play(self, coordinate_orig, coordinate_dest):
        # 0º Condition: there is a piece in the Origin Coordinates
        if self.getOnCoord(coordinate_orig) is None:
            return print("!>>invalid move: there is not a piece in the Origin coordinates given")

        # 1º Condition: The selected Piece is from your team
        PieceAux = self.getOnCoord(coordinate_orig)
        if PieceAux.getColor() != self.turn:
            return print("!>>invalid move: The piece selected it's not from your team")

        # 2º Condition: If there is a piece in the Destiny, its an enemy
        PieceAux2 = self.getOnCoord(coordinate_dest)
        if PieceAux2 is not None:
            if PieceAux.getColor() == PieceAux2.color:
                return print("!>>invalid move: there is a piece of your team in the destiny coordinates given")

        # 3º Condition: The move is allowed for the piece selected (Also treating pawn's special diagonal move)
        if type(PieceAux) is Pawn and PieceAux2 is not None:
            positions = PieceAux.canMove(coordinate_dest.getX(), coordinate_dest.getY(), True)
            if not positions:
                return print("!>>invalid move: move not allowed for piece ", {PieceAux.getType()})
        elif type(PieceAux) is Pawn and PieceAux2 is None:
            positions = PieceAux.canMove(coordinate_dest.getX(), coordinate_dest.getY(), False)
            if not positions:
                return print("!>>invalid move: move not allowed for piece ", {PieceAux.getType()})
        elif not PieceAux.canMove(coordinate_dest.getX(), coordinate_dest.getY()) :
            return print("!>>invalid move: move not allowed for piece ", {PieceAux.getType()})
        else:
            positions = PieceAux.canMove(coordinate_dest.getX(), coordinate_dest.getY())

        # 4º Condition: There is not a Piece blocking your move (Not including Knight) ARREGLOS NECESARIOS!!!!!!!!!!!!
        if type(PieceAux) is not Knight:
            valid = True
            for j in positions:
                if self.getOnCoord(j) is not None:
                    valid = False
                    break
            if valid is False:
                return print("!>>invalid move: There is a piece blocking your move")

        # ?º Condition: Your king is on check (This does not mean you have to move only the king)

        # ?º Condition: The Piece movement isn't leaving your king in checkmate

        # ?º Condition: The king isnt in CheckMate

        # If every condition is fulfilled, the move gets to be done
        self.setCoord(coordinate_dest, PieceAux)
        self.setCoord(coordinate_orig, None)
        # PieceAux.setPos(coordinate_dest)
        # Once the move is done, we need to check if the enemy King is on check

        self.turn = not self.turn

        # Aom CalV0

        def sudoPlay(self, coordinate_orig, coordinate_dest):
            self.setCoord(coordinate_dest, PieceAux)
            self.setCoord(coordinate_orig, None)

# Pruebas:

# Prueba = Pawn(0,0,True)
# print(type(Prueba) is Pawn)

# tablero = Board()
# tablero.showW()
# tablero.play(Coordinate(6, 7), Coordinate(5, 5))
# tablero.showB()
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
