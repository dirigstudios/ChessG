class Piece:

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy

    def __str__(self):
        return self.posx + str(self.posy)

    def move(self):  # cada pieza tendra su propia funcion de movimiento
        print("esta pieza no existe")

    def type(self):
        return "no type"
