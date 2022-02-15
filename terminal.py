#script to work on terminal for ChessG
#fkyros - build v1.1

##to-do: developer mode, help mode, if sth typed wrong, keep the program running

import sys
import userInput
from Board import Board

print(">>welcome to chessG! type \"play\" to start a new game")
typed = input(">>")

exit = False
while exit == False:

    if typed[0] == '$':
        sudo = input(">>sudo:")
        if sudo == "diriG":
            instruction = input("$>>dev mode activated: ")

    if typed == "exit":
        sure = input("?>>are you sure you want to leave? [type y/n]: ")
        if sure == 'y':
            exit = True
            sys.exit(">>bye!")

    if typed == "help":
        print("?>>help mode activated")
        print("?>>commands available: errorXX, ")
        help = input("?>>")
        #if help == ""

    newMove = False
    if typed == "play":
        Board.__init__(Board)
        Board.show(Board)
        move = input(">>type your move:")
        if len(move)!=5:
            sys.exit("!>>invalid syntax, type !help for further instructions")

        xFrom = userInput.extractX(userInput.sliceC1(move))
        yFrom = userInput.extractY(userInput.sliceC1(move))
        xTo = userInput.extractX(userInput.sliceC2(move))
        yTo = userInput.extractY(userInput.sliceC2(move))
        newMove = True
        print(xFrom, yFrom, xTo, yTo)
        Board.play(Board, xFrom, yFrom, xTo, yTo)
        Board.show(Board)

    exit = True
