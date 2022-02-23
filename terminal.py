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

    copyright = "DiriG © 2022 all rights deserved"
    start = ">>welcome to chessG! type \"play\" to start a new game"
    prompt = ">"
    helpM = ", type \"help\" for further instructions"
    error = "!>>error: "

    def __init__(self):
        self.terminator = True
        self.options = [self.leave, self.help, self.play2p, self.devmode, self.saveGame, self.playAI]
        self.game = Board()
        self.game.__init__()
        print(self.start)
        self.loop(self)

    def loop(self):
        print(self.copyright)
        try:
            while self.terminator:
                selected = input(self.prompt)
                if selected == "DiriG":
                    print("nice")
                elif selected == "clear":
                    self.clear(self)
                elif selected == "help":
                    self.help(self)
                elif selected == "exit": #ERROR???
                    self.leave(self)
                elif selected == "play":
                    self.play2p(self)
                else:
                    print(self.error + "please type a valid option (#else)" + self.helpM)
        except KeyboardInterrupt:
            sys.exit("\n" + self.error + "task killed (Ctrl C)")


    def leave(self):
        self.terminator = False
        # sys.exit(">>bye!")
        sure = input("?>>are you sure you want to leave? [type y/n]: ")
        if sure == 'y':
            sys.exit(">>bye!")
            print(self.copyright)
            #raise KeyboardInterrupt()
        elif sure == "n":
            self.terminator = True
            self.loop(self)
        else:
            print(self.error + "please type a valid option (#leave)" + self.helpM)

    def play2p(self):
        print(">>starting a Player VS Player game! white opens (uppercase pieces)")
        self.terminator = False
        self.game.showW() #starting with white pieces
        while not self.terminator:
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
                self.game.showW() if self.game.getTurn() else game.showB()
            else:
                print(self.error + "invalid move syntax (#play2p)" + self.helpM)
                # self.clear(self)

    def help(self):
        print("wip")
    def devmode(self):
        print("wip")
    def saveGame(self):
        print("wip")
    def playAI(self):
        print("wip")

    def clear(self):
        os.system(CLEAN)
        print(self.copyright)
        print(self.start)

Menu.__init__(Menu)


#old loop
# selected = self.translator(self, input(self.prompt))
#
# if selected >= 1 and selected<len(self.options):
#     print("ole")
#
# elif selected == 0:
#     self.leave()
# elif selected == 6:
#     self.clear()

# def translator(self, typed):
#     if typed == "exit":
#         return 0
#     elif typed == "help":
#         return 1
#     elif typed == "play":
#         return 2
#     elif typed == "$":
#         return 3
#     elif typed == "save":
#         return 4
#     elif typed == "play against AI":
#         return 5
#     elif typed == "clear":
#         return 6

    # def loop(self):
    #     print(self.copyright,self.start)
    #     while self.terminator:
    #         try:
    #             selected = input(self.prompt)
    #             if selected == "DiriG":
    #                 print("nice")
    #             elif selected == "clear":
    #                 self.clear()
    #             elif selected == "help":
    #                 self.help()
    #             elif selected == "exit": #ERROR???
    #                 self.leave()
    #             elif selected == "play":
    #                 self.play2p()
    #             else:
    #                 print(self.error + "please type a valid option (#else)" + self.helpM)
    #
    #         except KeyboardInterrupt:
    #             break
    #         except:
    #             print(self.copyright)
