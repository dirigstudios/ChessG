#script to work on terminal for ChessG
#fkyros - build v1.1

##to-do: developer mode, help mode, if sth typed wrong, keep the program running

import sys
import userInput

print(">>welcome to chessG! type \"play\" to start a new game")
typed = input(">>")

exit = False
while exit == False:

    if typed[0] == '!':
        print(">>manual")

    if typed[0] == '$':
        sudo = input(">>sudo:")
        if sudo == "diriG":
            instruction = input("$>dev mode activated: ")

    if typed == "exit":
        sure = input(">>are you sure you want to leave? [type y/n]: ")
        if sure == 'y':
            sys.exit(">>bye!")

    if typed == "help":
        print("?>>help mode")

    newMove = False
    if typed == "play":
        print("board.init()")
        move = input(">>type your move:")
        if len(move)!=5:
            sys.exit("!>>invalid syntax, type !help for further instructions")

        xFrom = userInput.extractX(userInput.sliceC1(move))
        yFrom = userInput.extractY(userInput.sliceC1(move))
        xTo = userInput.extractX(userInput.sliceC2(move))
        yTo = userInput.extractY(userInput.sliceC2(move))
        newMove = True
        print(xFrom, yFrom, xTo, yTo)

    exit = True
