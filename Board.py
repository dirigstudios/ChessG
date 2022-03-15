from PieceProv import Pawn, Rook, Bishop, Queen, King, Knight
from coordinates import Coordinate


class Board:
    def __init__(self):
        self.turn = True  # if turn==True, White plays, if turn==False, Black plays
        self.blackKing = King(4, 0, False)
        self.whiteKing = King(4, 7, True)

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
        x = 0
        y = 7
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

    def compareCoord(self, Coord1, Coord2):
        return Coord1.getX() == Coord2.getX() and Coord1.getY() == Coord2.getY()

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

    # ------------------------------------------------------------------------------------------------------------------

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
                return print("!>>invalid move: move not allowed for piece #1 ", {PieceAux.getType()})
        elif type(PieceAux) is Pawn and PieceAux2 is None:
            positions = PieceAux.canMove(coordinate_dest.getX(), coordinate_dest.getY(), False)
            if not positions:
                return print("!>>invalid move: move not allowed for piece #2 ", {PieceAux.getType()})
        elif not PieceAux.canMove(coordinate_dest.getX(), coordinate_dest.getY()):
            return print("!>>invalid move: move not allowed for piece #3 ", {PieceAux.getType()})
        else:
            positions = PieceAux.canMove(coordinate_dest.getX(), coordinate_dest.getY())

        # 4º Condition: There is not a Piece blocking your move (Not including Knight)
        if type(PieceAux) is not Knight:
            valid = True
            for j in positions:
                if not self.compareCoord(j, coordinate_dest) and not self.compareCoord(j, coordinate_orig) \
                        and self.getOnCoord(j) is not None:
                    valid = False
                    break
            if valid is False:
                return print("!>>invalid move: There is a piece blocking your move")

        # ?º Condition: Your king is on check (This does not mean you have to move only the king)

        # ?º Condition: The Piece movement isn't leaving your king in checkmate

        # ?º Condition: The king isnt in CheckMate

        # If every condition is fulfilled, the move gets to be done
        pieceRemoved = self.getOnCoord(coordinate_dest)  # Save eaten piece in case the move leaves your king on check
        self.setCoord(coordinate_dest, PieceAux)
        self.setCoord(coordinate_orig, None)
        PieceAux.setPos(coordinate_dest.getX(), coordinate_dest.getY())
        if type(PieceAux) is King:
            if self.turn is True:
                self.whiteKing.setPos(coordinate_dest.getX(), coordinate_dest.getY())
            else:
                self.blackKing.setPos(coordinate_dest.getX(), coordinate_dest.getY())

        # Once the move is done, we need to check if your king is on check

        if self.turn:
            if self.check(self.whiteKing):
                self.setCoord(coordinate_orig, PieceAux)
                self.setCoord(coordinate_dest, pieceRemoved)
                return print("!>>invalid move: Your king is left on check with this movement")
        elif not self.turn and self.check(self.blackKing):
            self.setCoord(coordinate_orig, PieceAux)
            self.setCoord(coordinate_dest, pieceRemoved)
            return print("!>>invalid move: Your king is left on check with this movement")

        self.turn = not self.turn

    # ------------------------------------------------------------------------------------------------------------------

    # Given a King of certain team, returns if it is on Check, our method is going to be check every line from which the
    # king can be threatened,
    def check(self, king):

        #debugging time 10-3-22:
        #no detecta la amenaza del peon
        #condiciones while con los booleanos para salirse antes (y en el if tmb)
        #optimizar lo de la diagonal
        #miramos solo las casillas individuales, pero no tenemos en cuenta que delante puede haber piezas enemigas prohibiendo ese problema

        x = king.getX()
        y = king.getY()
        # loop for checking every piece on King's Y axis
        i = 1
        blockYpos = False
        blockYneg = False
        while i <= 7:
            yplus = y + i
            yminus = y - i
            if 0 <= yplus <= 7 and not blockYpos:  # checking if valid values on board
                piece = self.getOnCoord(Coordinate(x, yplus))
                if piece is not None and piece.getColor() is self.turn:
                    blockYpos = True
                elif type(piece) is Queen or type(piece) is Rook and piece.getColor() is not self.turn:
                    return True
            if 0 <= yminus <= 7 and not blockYneg:
                piece = self.getOnCoord(Coordinate(x, yminus))
                if piece is not None and piece.getColor() is self.turn:
                    blockYneg = True
                elif type(piece) is Queen or type(piece) is Rook and piece.getColor() is not self.turn:
                    return True
            i += 1
        # loop for checking every piece on King's X axis
        i = 1
        blockXpos = False
        blockXneg = False
        while i <= 7:
            xplus = x + i
            xminus = x - i
            if 0 <= xplus <= 7 and not blockXpos:  # checking if valid values on board
                piece = self.getOnCoord(Coordinate(xplus, y))
                if piece is not None and piece.getColor() is self.turn:
                    blockXpos = True
                elif type(piece) is Queen or type(piece) is Rook and piece.getColor() is not self.turn:
                    return True
            if 0 <= xminus <= 7 and not blockXneg:
                piece = self.getOnCoord(Coordinate(xminus, y))
                if piece is not None and piece.getColor() is self.turn:
                    blockXpos = True
                elif type(piece) is Queen or type(piece) is Rook and piece.getColor() is not self.turn:
                    return True
            i += 1
        # loop for checking every king's diagonal
        i = 1
        blockI = False
        blockII = False
        blockIII = False
        blockIV = False
        while i <= 7:
            xplus = x + i
            xminus = x - i
            yplus = y + i
            yminus = y - i
            if 0 <= xplus <= 7 and 0 <= yplus <= 7:
                piece = self.getOnCoord(Coordinate(xplus, yplus))
                if piece is not None and piece.getColor() is self.turn:
                    blockI = True
                else:
                    self.checksDiagonal(piece, xplus, x, yplus, y)

                piece = self.getOnCoord(Coordinate(xplus, yminus))
                if piece is not None and piece.getColor() is self.turn:
                    blockII = True
                else:
                    self.checksDiagonal(piece, xplus, x, yminus, y)

                piece = self.getOnCoord(Coordinate(xminus, yplus))
                if piece is not None and piece.getColor() is self.turn:
                    blockIII = True
                else:
                    self.checksDiagonal(piece, xminus, x, yplus, y)

                piece = self.getOnCoord(Coordinate(xminus, yminus))
                if piece is not None and piece.getColor() is self.turn:
                    blockIV = True
                else:
                    self.checksDiagonal(piece, xminus, x, yminus, y)
            i += 1
        return False

    def checksDiagonal(self, piece, xplus, x, yplus, y ):
        if type(piece) is Bishop or type(piece) is Queen and piece.getColor() is not self.turn:
            return True
        elif type(piece) is Pawn and abs(xplus - x) == 1 and abs(yplus - y) == 1 and piece.getColor() is not self.turn:
            return True

    # def checksNonDiagonal(self,piece):

    # ------------------------------------------------------------------------------------------------------------------

    # Sudo/God Functions, so Gabri is happy ;) :

    def sudoPlay(self, coordinate_orig, coordinate_dest):
        self.setCoord(coordinate_dest, self.getOnCoord(coordinate_orig))
        self.setCoord(coordinate_orig, None)

    def sudoKill(self, coordinateKill):
        self.setCoord(coordinateKill, None)

    def sudoNuke(self):
        self.board = [None] * 8
        for i in range(8):
            self.board[i] = [None] * 8


# Tatakae
