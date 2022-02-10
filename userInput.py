#script to work with user input moves on terminal for ChessG
#fkyros - build v1.1

import sys

#according to v1, our moves should be type as "xy(from) xy(to)"
#example: "d5 d6"
#internally, this will be translated to our code for working coordinates on our matrix (array indexes)
#example: "d5 d6" -> cFrom = (3,4), cTo(3,5)

#given a proper input move, returns a string with the From coordinate
def sliceC1(move):
    if move[2]!=" ":
        sys.exit("!>invalid syntax, type !help for further instructions")

    slice = move.split(" ")
    return slice[0]

#given a proper input move, returns a string with the To coordinate
def sliceC2(move):
    if move[2]!=" ":
        sys.exit("!>invalid syntax, type !help for further instructions")
    slice = move.split(" ")
    return slice[1]

#returns None if not given a valid character from a-h
def extractX(c):
    x = c[0:1] #x axis value
    try:
        intX = int(hex(ord(x)),base=16) #ASCII value from hex to decimal
        if (intX >= 97 and intX <= 104): #lowercase a-h
            return intX - 96 - 1
        if (intX >= 65 and intX <= 72): #uppercase A-H
            return intX - 64 - 1
        #-1 to fit array numeration
    except:
        return None

#returns None if not given a number in char
def extractY(c):
    try:
        return int(c[1:2]) - 1
    except:
        return None
