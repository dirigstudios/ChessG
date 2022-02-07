class Piece:

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.firstmove = True

    def __str__(self):
        return self.posx + str(self.posy)

    def move(self):  # ejemplo de movimiento para el peon
        print("esta pieza no existe")

