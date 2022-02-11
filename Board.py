from Pieces import Piece
class Board():
    def __init__(self):
        self.board= [Piece(1,1,"B")]*8

    def show(self):
        for i in self.board:
            (i.name("P"))


tablero= Board()
tablero.show()