class Piece:

    def __init__(self, posx, posy, color):
        self.posx = posx
        self.posy = posy
        self.color = color

    def getColor(self):
        return self.color

    def setPos(self, posx, posy):
        self.posy = posy
        self.posx = posx

    def __str__(self):
        return f"[   ]"

    def canMove(self, posx, posy):  # cada pieza tendra su propia funcion de movimiento
        return "esta pieza no existe"

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
        self.firstmove = True

    def getColor(self):
        return self.color

    def name(self):
        return print(f"[{self.type},{self.color}]", end=" ")

    def getType(self):
        return "peon"

    def setFirstMoveFalse(self):
        self.firstmove=False

    def canMove(self, posx, posy):  # cada pieza tendra su propia funcion de movimiento
        if (self.firstmove and posy-self.posy==2) or posy-self.posy==1:
            return True
        else:
            return False


class Rook(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if color == "B":
            self.type = "r"
        else:
            self.type = "R"

    def getColor(self):
        return self.color

    def name(self):
        return print(f"[{self.type},{self.color}]", end=" ")

    def getType(self):
        return "torre"

    def canMove(self, posx, posy):  # cada pieza tendra su propia funcion de movimiento
        return True


class Bishop(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if color == "B":
            self.type = "b"
        else:
            self.type = "B"

    def getColor(self):
        return self.color

    def name(self):
        return print(f"[{self.type},{self.color}]", end=" ")

    def getType(self):
        return "alfil"

    def canMove(self, posx, posy):  # cada pieza tendra su propia funcion de movimiento
        return True


class Knight(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if color == "B":
            self.type = "n"
        else:
            self.type = "N"

    def getColor(self):
        return self.color

    def name(self):
        return print(f"[{self.type},{self.color}]", end=" ")

    def getType(self):
        return "caballo"

    def canMove(self, posx, posy):  # cada pieza tendra su propia funcion de movimiento
        return True


class Queen(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if color == "B":
            self.type = "q"
        else:
            self.type = "Q"

    def getColor(self):
        return self.color

    def name(self):
        return print(f"[{self.type},{self.color}]", end=" ")

    def getType(self):
        return "dama"

    def canMove(self, posx, posy):  # cada pieza tendra su propia funcion de movimiento
        return True


class King(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if color == "B":
            self.type = "k"
        else:
            self.type = "K"

    def getColor(self):
        return self.color

    def name(self):
        return print(f"[{self.type},{self.color}]", end=" ")

    def getType(self):
        return "rey"

    def canMove(self, posx, posy):  # cada pieza tendra su propia funcion de movimiento
        return True
