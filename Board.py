from PieceProv import Pawn, Rook, Bishop, Queen, King, Knight


class Board:
    def __init__(self):
        self.board = [None] * 8
        for i in range(8):
            self.board[i] = [None] * 8
        x = 0
        y = 0
        self.board[x][y] = Rook(x, y, "W")
        self.board[x][7 - y] = Rook(x, y, "W")
        self.board[7][y] = Rook(x, y, "B")
        self.board[7][7 - y] = Rook(x, y, "B")
        y = y + 1
        self.board[x][y] = Knight(x, y, "W")
        self.board[x][7 - y] = Knight(x, y, "W")
        self.board[7][y] = Knight(x, y, "B")
        self.board[7][7 - y] = Knight(x, y, "B")
        y = y + 1
        self.board[x][y] = Bishop(x, y, "W")
        self.board[x][7 - y] = Bishop(x, y, "W")
        self.board[7][y] = Bishop(x, y, "B")
        self.board[7][7 - y] = Bishop(x, y, "B")
        y = y + 1
        self.board[x][y] = Queen(x, y, "W")
        self.board[7][3] = Queen(x, y, "B")
        y = y + 1
        self.board[x][y] = King(x, y, "W")
        self.board[7][4] = King(x, y, "B")
        y = 0
        x = 1
        while y != 8:
            self.board[x][y] = Pawn(x, y, "W")
            self.board[7 - 1][y] = Pawn(x, y, "B")
            y = y + 1

    def show(self):
        for i in self.board:
            print("\n")
            for j in i:
                if j is None:
                    print("[   ]", end=" ")
                else:
                    j.name()
        print("\n")

    def play(self, OrigX, OrigY, DestX, DestY):
        if self.board[OrigX][OrigY] is None:
            return print("La casilla de origen esta vacia, selecciones otra casilla")
        PieceAux = self.board[OrigX][OrigY]
        if self.board[DestX][DestY] is not None:
            PieceAux2 = self.board[DestX][DestY]
            if PieceAux.color == PieceAux2.color:
                return print("No se puede realizar este movimiento, Hay una pieza de tu color en la casilla destino")
        if not PieceAux.canMove(DestX,DestY):
            return print("El movimiento no es valido para una pieza del tipo:", {PieceAux.getType()})
        self.board[DestX][DestY] = PieceAux
        self.board[OrigX][OrigY] = None
        PieceAux.setPos(DestX, DestY)
        print("----------------JUGADA------------")


tablero = Board()
tablero.show()
tablero.play(1, 1, 1, 3)
tablero.show()
