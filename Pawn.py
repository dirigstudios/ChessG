from Piece import Piece


class Pawn(Piece):

    def move(self):
        if self.firstmove:
            self.firstmove = False
            self.posy = self.posy + 2
        else:
            self.posy = self.posy + 1


xd = Pawn("c", 2)
print(xd)
xd.move()
print(xd)
