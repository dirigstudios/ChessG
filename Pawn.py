from Piece import Piece


class Pawn(Piece):

    def __init__(self, posx, posy):
        super().__init__(posx, posy)
        self.firstmove = True

    def move(self):
        if self.firstmove:
            self.firstmove = False
            self.posy = self.posy + 2
        else:
            self.posy = self.posy + 1

    def type(self):
        return "pawn"
