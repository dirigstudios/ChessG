class Piece:

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy

    def __str__(self):
        return self.posx + str(self.posy)

    def move(self):
        a = 0


xd = Piece("c", 5)
print(xd.__str__())
