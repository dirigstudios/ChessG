#script to work on terminal for ChessG
#fkyros - build v1.1

##to-do: developer mode, help mode, if sth typed wrong, keep the program running

import sys
import userInput
from Board import Board

def leave():
    sure = input("?>>are you sure you want to leave? [type y/n]: ")
    if sure == 'y':
        exit = True
        sys.exit(">>bye!")

print("DiriG © 2022 all rights deserved")
print(">>welcome to chessG! type \"play\" to start a new game")
typed = input(">>")

exit = False
while typed != "exit":

    if typed[0] == '$':
        sudo = input(">>sudo:")
        if sudo == "diriG":
            instruction = input("$>>dev mode activated: ")

    elif typed == "help":
        print("?>>help mode activated")
        print("?>>commands available: errorXX, ")
        help = input("?>>")
        #if help == ""

    elif typed == "play":
        game = Board()
        game.__init__()
        game.show()
        move = input(">>type your move:")

        if move == "exit":
            leave()

        if len(move)!=5:
            sys.exit("!>>invalid syntax, type !help for further instructions")

        xFrom = userInput.extractX(userInput.sliceC1(move))
        yFrom = userInput.extractY(userInput.sliceC1(move))
        xTo = userInput.extractX(userInput.sliceC2(move))
        yTo = userInput.extractY(userInput.sliceC2(move))
        newMove = True
        print(xFrom, yFrom, xTo, yTo)
        game.play(xFrom, yFrom, xTo, yTo)
        game.show()

    else:
        print("please type a valid option, type !help for further instructions")

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
