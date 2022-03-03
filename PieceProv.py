from coordinates import Coordinate


class Piece:

    def __init__(self, posx, posy, color):
        self.coordinate=Coordinate(0,0)
        self.coordinate.setX(posx)
        self.coordinate.setY(posy)
        self.color = color

    def getColor(self):
        return self.color

    def setPos(self, posx, posy):
        self.coordinate.setY(posy)
        self.coordinate.setX(posx)

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
                if self.firstmove and posy - self.coordinate.getY() == 2:
                    return [Coordinate(posx, self.coordinate.getY() + 1), Coordinate(posx, self.coordinate.getY()+2)]
                elif posy - self.coordinate.getY() == 1:
                    return [Coordinate(posx, posy)]
            if self.color: # If its white the movement is normal
                if self.firstmove and self.coordinate.getY() - posy == 2:
                    return [Coordinate(posx, self.coordinate.getY() - 1), Coordinate(posx, self.coordinate.getY()-2)]
                elif self.coordinate.getY() - posy == 1:
                    return [Coordinate(posx, posy)]
        else: # If the movement is to capture a piece we check if the movement is valid
            if not self.color:
                if ((self.coordinate.getY() - posy) == 1) and (-1 <= (posx - self.coordinate.getX()) <= 1):
                    return [Coordinate(posx, posy)]
            if self.color:
                if ((posy - self.coordinate.getY()) == 1) and (-1 <= (posx - self.coordinate.getX()) <= 1):
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
        if self.coordinate.getY() - posy == 0: # If the Y vertex is the same, the movement is horizontal
            if self.coordinate.getX() - posx > 0:
                auxcoord = posx
                while auxcoord <= self.coordinate.getX():
                    position.append(Coordinate(auxcoord, posy))
                    auxcoord = auxcoord + 1
            elif self.coordinate.getX() - posx < 0:
                auxcoord = posx
                while auxcoord >= self.coordinate.getX():
                    position.append(Coordinate(auxcoord, posy))
                    auxcoord = auxcoord - 1
        elif self.coordinate.getX() - posx == 0: # If the vertex X is the same, the movement is vertical
            if self.coordinate.getY() - posy > 0:
                auxcoord = posy
                while auxcoord <= self.coordinate.getY():
                    position.append(Coordinate(posx, auxcoord))
                    auxcoord = auxcoord + 1
            elif self.coordinate.getY() - posy < 0:
                auxcoord = posy
                while auxcoord >= self.coordinate.getY():
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
        cuadrantex = posx - self.coordinate.getX()
        multiplicadorx = 1
        cuadrantey = posy - self.coordinate.getY()
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
                positions.append(Coordinate(self.coordinate.getX() + (i * multiplicadorx), self.coordinate.getY() + (i * multiplicadory)))
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
        if (self.coordinate.getX() - posx == 2) and (self.coordinate.getY() - posy == 1):
            positions.append(Coordinate(posx, posy))
        elif (self.coordinate.getX() - posy == -2) and (self.coordinate.getY() - posy == -1):
            positions.append(Coordinate(posx, posy))
        elif (self.coordinate.getX() - posx == 2) and (self.coordinate.getY() - posy == -1):
            positions.append(Coordinate(posx, posy))
        elif (self.coordinate.getX() - posx == -2) and (self.coordinate.getY() - posy == 1):
            positions.append(Coordinate(posx, posy))
        elif (self.coordinate.getY() - posy == 2) and (self.coordinate.getX() - posx == 1):
            positions.append(Coordinate(posx, posy))
        elif (self.coordinate.getY() - posy == -2) and (self.coordinate.getX() - posx == -1):
            positions.append(Coordinate(posx, posy))
        elif (self.coordinate.getY() - posy == -2) and (self.coordinate.getX() - posx == 1):
            positions.append(Coordinate(posx, posy))
        elif (self.coordinate.getY() - posy == 2) and (self.coordinate.getX() - posx == -1):
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
        cuadrantex = posx - self.coordinate.getX()
        multiplicadorx = 1
        cuadrantey = posy - self.coordinate.getY()
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
                position.append(Coordinate(self.coordinate.getX() + (i * multiplicadorx), self.coordinate.getY() + (i * multiplicadory)))
                cuadrantey = cuadrantey - 1
                i = i + 1
        auxcoord = 0
        if self.coordinate.getY() - posy == 0:
            if self.coordinate.getX() - posx > 0:
                auxcoord = posx
                while auxcoord <= self.coordinate.getX():
                    position.append(Coordinate(auxcoord, posy))
                    auxcoord = auxcoord + 1
            elif self.coordinate.getX() - posx < 0:
                auxcoord = posx
                while auxcoord >= self.coordinate.getX():
                    position.append(Coordinate(auxcoord, posy))
                    auxcoord = auxcoord - 1
        elif self.coordinate.getX() - posx == 0:
            if self.coordinate.getY() - posy > 0:
                auxcoord = posy
                while auxcoord <= self.coordinate.getY():
                    position.append(Coordinate(posx, auxcoord))
                    auxcoord = auxcoord + 1
            elif self.coordinate.getY() - posy < 0:
                auxcoord = posy
                while auxcoord >= self.coordinate.getY():
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
        if -1 <= self.coordinate.getY() - posy <= 1 and -1 <= self.coordinate.getX() - posx <= 1:
            position.append(Coordinate(posx, posy))
        return position
