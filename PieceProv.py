class Piece:

    def __init__(self, posx, posy, color):
        self.posx = posx
        self.posy = posy
        self.color = color

    def __str__(self):
        return self.posx + str(self.posy)

    def move(self):  # cada pieza tendra su propia funcion de movimiento
        print("esta pieza no existe")

    def name(self):
        pass


class Pawn(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if color == "B":
            self.type = "p"
        else:
            self.type = "P"

    def name(self):
        return print(f"[{self.type}]", end="")

class Rook(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if color == "B":
            self.type = "r"
        else:
            self.type = "R"

    def name(self):
        return print(f"[{self.type}]", end="")

class Bishop(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if color == "B":
            self.type = "b"
        else:
            self.type = "B"

    def name(self):
        return print(f"[{self.type}]", end="")

class Knight(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if color == "B":
            self.type = "n"
        else:
            self.type = "N"

    def name(self):
        return print(f"[{self.type}]", end="")

class Queen(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if color == "B":
            self.type = "q"
        else:
            self.type = "Q"

    def name(self):
        return print(f"[{self.type}]", end="")

class King(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if color == "B":
            self.type = "k"
        else:
            self.type = "K"

    def name(self):
        return print(f"[{self.type}]", end="")
