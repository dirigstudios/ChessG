from PieceProv import Pawn, Rook, Bishop, Queen, King, Knight


class Board:
    def __init__(self):
        self.board = [None] * 8
        for i in range(8):
            self.board[i] = [None] * 8
        x = 0
        y = 0
        self.board[x][y] = Rook(y, x, "W")
        self.board[x][7 - y] = Rook(y, x, "W")
        self.board[7][y] = Rook(y, x, "B")
        self.board[7][7 - y] = Rook(y, x, "B")
        y = y + 1
        self.board[x][y] = Knight(y, x, "W")
        self.board[x][7 - y] = Knight(y, x, "W")
        self.board[7][y] = Knight(y, x, "B")
        self.board[7][7 - y] = Knight(y, x, "B")
        y = y + 1
        self.board[x][y] = Bishop(y, x, "W")
        self.board[x][7 - y] = Bishop(y, x, "W")
        self.board[7][y] = Bishop(y, x, "B")
        self.board[7][7 - y] = Bishop(y, x, "B")
        y = y + 1
        self.board[x][y] = Queen(y, x, "W")
        self.board[7][3] = Queen(y, x, "B")
        y = y + 1
        self.board[x][y] = King(y, x, "W")
        self.board[7][4] = King(y, x, "B")
        y = 0
        x = 1
        while y != 8:
            self.board[x][y] = Pawn(y, x, "W")
            self.board[7 - 1][y] = Pawn(y, x, "B")
            y = y + 1

    def show(self):
        print("")
        n=1
        for i in self.board:
            print(n, end=" ")
            for j in i:
                if j is None:
                    print("[ ]", end=" ")
                else:
                    j.name()
            print("")
            n=n+1
        print("   A   B   C   D   E   F   G   H ")
        print("")

    def play(self, OrigX, OrigY, DestX, DestY):
        if self.board[OrigY][OrigX] is None:
            return print("!>>invalid move: there is not a piece in the Origin coordinates given")
        PieceAux = self.board[OrigY][OrigX]
        if self.board[DestY][DestX] is not None:
            PieceAux2 = self.board[DestY][DestX]
            if PieceAux.color == PieceAux2.color:
                return print("!>>invalid move: there is a piece of your team in the destiny coordinates given")
        if not PieceAux.canMove(DestY ,DestX):
            return print("!>>invalid move: move not allowed for piece ", {PieceAux.getType()})

        self.board[DestY][DestX] = PieceAux
        self.board[OrigY][OrigX] = None
        PieceAux.setPos(DestY, DestX)




# tablero = Board()
# tablero.show()
# tablero.play(1,1 ,2 ,2 )
# tablero.show()
