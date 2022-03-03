#script to work on terminal for ChessG
#fkyros - build v1.2

##to-do: developer mode, help mode, (if sth typed wrong, keep the program running), show available options,
# show board correspondiente,
# problemas si el input es "bueno" a priori pero en verdad no,
# meter las opciones del menu mientras se esta jugando

#used modules
import os
import sys
import time
import userInput
from Board import Board
from coordinates import Coordinate

#constants
CLEAN = "clear" if sys.platform.startswith("linux") else "cls"

class Menu:

    copyright = "DiriG Studios © 2022 all rights deserved"
    start = ">>welcome to chessG! type \"play\" to start a new game"
    prompt = ">"
    helpM = ", type \"help\" for further instructions"
    error = "!>>error: "

    def __init__(self):
        self.sudo = False
        self.terminal = True
        self.playing = False
        self.options = [self.leave, self.help, self.play2p, self.sudoMode, self.saveGame, self.playAI]
        self.game = Board()
        self.game.__init__()
        print(self.start)
        self.loop(self)

    def loop(self):
        print(self.copyright)
        try:
            while self.terminal:
                selected = input(self.prompt)
                if selected == "DiriG":
                    print("nice")
                elif selected == "clear":
                    self.clear(self)
                elif selected == "help":
                    self.help(self)
                elif selected == "exit":
                    self.leave(self)
                elif selected == "play":
                    self.play2p(self)
                else:
                    print(self.error + "please type a valid option (#else)" + self.helpM)
        except KeyboardInterrupt:
            sys.exit("\n" + self.error + "terminal chessG got killed")

    def clear(self):
        os.system(CLEAN)
        print(self.copyright)
        print(self.start)

    def leave(self):
        self.terminal = False
        # sys.exit(">>bye!")
        sure = input("?>>are you sure you want to leave? [type y/n]: ")
        if sure == 'y':
            sys.exit(">>bye!")
            print(self.copyright)
            #raise KeyboardInterrupt()
        elif sure == "n":
            if self.playing:
                self.play2p(self)
            else:
                self.terminal = True
                self.loop(self)
        else:
            print(self.error + "please type a valid option (#leave)" + self.helpM)

    def showBoard(self):
        return self.game.showW() if self.game.getTurn() else self.game.showB()

    def play2p(self):
        print(">>starting a Player VS Player game! white opens (uppercase pieces)")
        self.terminal = False
        self.playing = True
        self.showBoard(self) #starting with white pieces
        while not self.terminal:
            move = input(">>type your move:")

            if len(move)==5 and move[2]==" ":
                #slicing the coordinates
                xFrom = userInput.extractX(userInput.sliceC1(move))
                yFrom = userInput.extractY(userInput.sliceC1(move))
                xTo = userInput.extractX(userInput.sliceC2(move))
                yTo = userInput.extractY(userInput.sliceC2(move))

                if xFrom == None or yFrom == None or xTo == None or yTo == None:
                    print("illo escribe bien las malditas coordenadas")

                #creating the coordinates
                cFrom = Coordinate(xFrom, yFrom)
                cTo = Coordinate(xTo, yTo)

                self.game.play(cFrom, cTo)
                self.game.showW() if self.game.getTurn() else self.game.showB()
            elif move == "clear":
                self.clear(self)
                self.showBoard(self)
            elif move == "help":
                self.help(self)
            elif move == "exit":
                self.leave(self)
            elif move == "show":
                self.showBoard(self)
            elif move == "$":
                self.sudoMode(self)
            else:
                print(self.error + "invalid move syntax (#play2p)" + self.helpM)
                # self.clear(self)

    def help(self):
        print("wip")

    def sudoMode(self):
        #self.playing = False
        self.sudo = True
        sudot = input("$>")
        if sudot == "dirig22":
            self.clear(self)
            self.showBoard(self)
            print("$>>sudo mode activated")
            sudott = input("$>")

            while self.sudo:
                if len(sudott)==5 and sudott[2]==" ": #moving whatever piece mode
                    xFrom = userInput.extractX(userInput.sliceC1(sudott))
                    yFrom = userInput.extractY(userInput.sliceC1(sudott))
                    xTo = userInput.extractX(userInput.sliceC2(sudott))
                    yTo = userInput.extractY(userInput.sliceC2(sudott))

                    if xFrom == None or yFrom == None or xTo == None or yTo == None:
                        print("illo escribe bien las malditas coordenadas")

                    cFrom = Coordinate(xFrom, yFrom)
                    cTo = Coordinate(xTo, yTo)
                    self.game.sudoPlay(cFrom, cTo)

                    self.clear(self)
                    self.showBoard(self)
                    self.sudo = False           #ERROR: MAKING IT UNTIL LEAVING
                    return

                elif len(sudott)==2: #killing pieces mode
                    xFrom = userInput.extractX(userInput.sliceC1(sudott))
                    yFrom = userInput.extractY(userInput.sliceC1(sudott))
                    if xFrom == None or yFrom == None:
                        print("illo escribe bien las malditas coordenadas")
                    cFrom = Coordinate(xFrom, yFrom)
                    self.game.sudoKill(cFrom)

                    self.clear(self)
                    self.showBoard(self)
                    self.sudo = False           #ERROR: MAKING IT UNTIL LEAVING
                    return

                elif sudott == "leave":
                    self.clear(self)
                    self.showBoard(self)
                    self.sudo = False
                    return
                else:
                    self.clear(self)
                    self.showBoard(self)
                    return
        else:
            self.clear(self)
            self.showBoard(self)
            return

    def saveGame(self):
        print("wip")
    def playAI(self):
        print("wip")
    def options(self):
        print("wip")

Menu.__init__(Menu)
