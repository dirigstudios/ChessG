import sys

#move = input(">>Next move: ")
move = "d3 d4"

#movements must have 5 characters -> "d5 d6"
if len(move)!=5:
    sys.exit("invalid syntax")

#string slything methods

#1
# former = move[0:2] #this string slything method does not include the last character
# latter = move[3:5]
# print (former, latter)

#2
slice = move.split(" ")
mfrom = slice[0]
mto = slice[1]

print(mfrom, mto)

#function that extracts the coordinates for operative work
#HAS TO BE IN LOWERCASE
def extractX(c):
    x = c[0:1] #x axis value
    hexX = ord(x) #ASCII value in hex for the x xAxis
    #if (hexX > 0x60): #making sure its syntax is correct (ISSUE)
    return int(hex(hexX),base=16) - 96 - 1 #-1 to fit array numeration

def extractY(c):
    return int(c[1:2]) - 1 #-1 to fit array numeration

print(isinstance(extractX(mfrom),int)) #they are ints
print(extractX(mfrom))
print(extractY(mfrom))
