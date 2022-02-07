class Board():
    def __init__(self,state):
        self.board = [1]*8
        for i in range(8):
            self.board[i] =[1]*8
        self.state = state

    def start (self,elem):
        for i in self.board:
            for j in i:
                j=j+1

    def show(self):
        for i in self.board:
            for j in range(len(i)):
                print("[",i[j],"]", end=" ")
                if j==7:
                    print("\n")

tablero= Board("Iniciado")
tablero.start(1)
tablero.show()
