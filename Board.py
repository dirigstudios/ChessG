from Pieces import Piece
from Pieces import Pawn,Rook,Bishop,Queen,King,Knight
class Board():
    def __init__(self):
        self.board = [None] * 8
        for i in range(8):
            self.board[i] = [None] * 8
        x=0
        y=0
        self.board[x][y] = Rook(x,y,"W","R")
        self.board[x][7-y] = Rook(x,y,"W","R")
        self.board[7][y] = Rook(x,y,"B","R")
        self.board[7][7-y] = Rook(x,y,"B","R")
        y=y+1
        self.board[x][y] = Knight(x,y,"W","K")
        self.board[x][7-y] = Knight(x,y,"W","K")
        self.board[7][y] = Knight(x,y,"B","K")
        self.board[7][7-y] = Knight(x,y,"B","K")
        y=y+1
        self.board[x][y] = Bishop(x,y,"W","B")
        self.board[x][7-y] = Bishop(x,y,"W","B")
        self.board[7][y] = Bishop(x,y,"B","B")
        self.board[7][7-y] = Bishop(x,y,"B","B")
        y=y+1
        self.board[x][y] = Queen(x,y,"W","Q")
        self.board[7][3] = Queen(x,y,"B","Q")
        y=y+1
        self.board[x][y] = King(x,y,"W","K")
        self.board[7][4] = King(x,y,"B","K")
        y=0
        x=1
        while(y!=8):
            self.board[x][y] = Pawn(x,y,"W","P")
            self.board[7-1][y] = Pawn(x,y,"B","P")
            y=y+1

    def show(self):
        for i in self.board:
            print("\n")
            for j in i:
                if(j==None):
                    print("[   ]",end=" ")
                else:
                    j.name()

tablero= Board()
tablero.show()