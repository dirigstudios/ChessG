from coordinates import Coordinate


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
        return f"[ ]"

    def canMove(self, posy, posx):
        return "esta pieza no existe"

    def name(self):
        pass


class Pawn(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if not color:
            self.type = "p"
        else:
            self.type = "P"
        self.firstmove = True

    def getColor(self):
        return self.color

    def name(self):
        return print(f"[{self.type}]", end=" ")

    def getType(self):
        return "peon"

    def setFirstMoveFalse(self):
        self.firstmove = False

    def canMove(self, posx, posy, pieceAt):
        positions = []
        if not pieceAt:
            # Check if this pawn is black or white
            if not self.color: # If its black the movement is inverted
                if self.firstmove and self.posy - posy == 2:
                    return [Coordinate(posx, posy + 1), Coordinate(posx, posy)]
                elif self.posy - posy == 1:
                    return [Coordinate(posx, posy)]
            if self.color: # If its white the movement is normal
                if self.firstmove and posy - self.posy == 2:
                    return [Coordinate(posx, posy - 1), Coordinate(posx, posy)]
                elif posy - self.posy == 1:
                    return [Coordinate(posx, posy)]
        else: # If the movement is to capture a piece we check if the movement is valid
            if not self.color:
                if ((self.posy - posy) == 1) and (-1 <= (posx - self.posx) <= 1):
                    return [Coordinate(posx, posy)]
            if self.color:
                if ((posy - self.posy) == 1) and (-1 <= (posx - self.posx) <= 1):
                    return [Coordinate(posx, posy)]
        return positions


class Rook(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if not color:
            self.type = "r"
        else:
            self.type = "R"

    def getColor(self):
        return self.color

    def name(self):
        return print(f"[{self.type}]", end=" ")

    def getType(self):
        return "torre"

    def canMove(self, posx, posy):
        position = []
        auxcoord = 0;
        # We have to check if the movement is vertical or horizontal
        if self.posy - posy == 0: # If the Y vertex is the same, the movement is horizontal
            if self.posx - posx > 0:
                auxcoord = posx
                while auxcoord <= self.posx:
                    position.append(Coordinate(auxcoord, posy))
                    auxcoord = auxcoord + 1
            elif self.posx - posx < 0:
                auxcoord = posx
                while auxcoord >= self.posx:
                    position.append(Coordinate(auxcoord, posy))
                    auxcoord = auxcoord - 1
        elif self.posx - posx == 0: # If the vertex X is the same, the movement is vertical
            if self.posy - posy > 0:
                auxcoord = posy
                while auxcoord <= self.posy:
                    position.append(Coordinate(posx, auxcoord))
                    auxcoord = auxcoord + 1
            elif self.posy - posy < 0:
                auxcoord = posy
                while auxcoord >= self.posy:
                    position.append(Coordinate(posx, auxcoord))
                    auxcoord = auxcoord - 1
        return position


class Bishop(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if not color:
            self.type = "b"
        else:
            self.type = "B"

    def getColor(self):
        return self.color

    def name(self):
        return print(f"[{self.type}]", end=" ")

    def getType(self):
        return "alfil"

    def canMove(self, posx, posy):
        positions = []
        # We initialize variables for Y and X vertex in order to check to which quadrant we are trying to move
        cuadrantex = posx - self.posx
        multiplicadorx = 1
        cuadrantey = posy - self.posy
        multiplicadory = 1
        if cuadrantey < 0:
            cuadrantey = -cuadrantey
            multiplicadory = -1
        if cuadrantex < 0:
            cuadrantex = -cuadrantex
            multiplicadorx = -1
        if cuadrantex == cuadrantey:
            i = 0
            # After we see which quadrant we are trying to move to, we use a loop to build the array of positions
            while cuadrantey >= 0:
                positions.append(Coordinate(self.posx + (i * multiplicadorx), self.posy + (i * multiplicadory)))
                cuadrantey = cuadrantey - 1
                i = i + 1
        return positions


class Knight(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if not color:
            self.type = "n"
        else:
            self.type = "N"

    def getColor(self):
        return self.color

    def name(self):
        return print(f"[{self.type}]", end=" ")

    def getType(self):
        return "caballo"

    def canMove(self, posx, posy):
        positions = []
        # As the Knight moves are very different, we have to check which one of the 8 possibilities we are trying to do
        if (self.posx - posx == 2) and (self.posy - posy == 1):
            positions.append(Coordinate(posx, posy))
        elif (self.posx - posy == -2) and (self.posy - posy == -1):
            positions.append(Coordinate(posx, posy))
        elif (self.posx - posx == 2) and (self.posy - posy == -1):
            positions.append(Coordinate(posx, posy))
        elif (self.posx - posx == -2) and (self.posy - posy == 1):
            positions.append(Coordinate(posx, posy))
        elif (self.posy - posy == 2) and (self.posx - posx == 1):
            positions.append(Coordinate(posx, posy))
        elif (self.posy - posy == -2) and (self.posx - posx == -1):
            positions.append(Coordinate(posx, posy))
        elif (self.posy - posy == -2) and (self.posx - posx == 1):
            positions.append(Coordinate(posx, posy))
        elif (self.posy - posy == 2) and (self.posx - posx == -1):
            positions.append(Coordinate(posx, posy))
        return positions


class Queen(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if not color:
            self.type = "q"
        else:
            self.type = "Q"

    def getColor(self):
        return self.color

    def name(self):
        return print(f"[{self.type}]", end=" ")

    def getType(self):
        return "dama"

    def canMove(self, posx, posy):
        # The queen is a fusion of the Rook and the Bishop, so we can merge the code to get the queens one
        position = []
        cuadrantex = posx - self.posx
        multiplicadorx = 1
        cuadrantey = posy - self.posy
        multiplicadory = 1
        if cuadrantey < 0:
            cuadrantey = -cuadrantey
            multiplicadory = -1
        if cuadrantex < 0:
            cuadrantex = -cuadrantex
            multiplicadorx = -1
        if cuadrantex == cuadrantey:
            i = 0
            while cuadrantey >= 0:
                positions.append(Coordinate(self.posx + (i * multiplicadorx), self.posy + (i * multiplicadory)))
                cuadrantey = cuadrantey - 1
                i = i + 1
        auxcoord
        if self.posy - posy == 0:
            if self.posx - posx > 0:
                auxcoord = posx
                while auxcoord <= self.posx:
                    position.append(Coordinate(auxcoord, posy))
                    auxcoord = auxcoord + 1
            elif self.posx - posx < 0:
                auxcoord = posx
                while auxcoord >= self.posx:
                    position.append(Coordinate(auxcoord, posy))
                    auxcoord = auxcoord - 1
        elif self.posx - posx == 0:
            if self.posy - posy > 0:
                auxcoord = posy
                while auxcoord <= self.posy:
                    position.append(Coordinate(posx, auxcoord))
                    auxcoord = auxcoord + 1
            elif self.posy - posy < 0:
                auxcoord = posy
                while auxcoord >= self.posy:
                    position.append(Coordinate(posx, auxcoord))
                    auxcoord = auxcoord - 1
        return position


class King(Piece):
    pass

    def __init__(self, posx, posy, color):
        super().__init__(posx, posy, color)
        if not color:
            self.type = "k"
        else:
            self.type = "K"

    def getColor(self):
        return self.color

    def name(self):
        return print(f"[{self.type}]", end=" ")

    def getType(self):
        return "rey"

    def canMove(self, posx, posy):
        position = []
        # The king only has to check if it moved only one position
        if -1 <= self.posy - posy <= 1 and -1 <= self.posx - posx <= 1:
            position.append(Coordinate(posx, posy))
        return position
