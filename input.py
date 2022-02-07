import sys

#move = input(">>Next move: ")
move = "d3 d4"

#movements must have 5 characters -> "d5 d6"
if len(move)!=5:
    sys.exit("invalid syntax")

#string slything methods

#1
former = move[0:2] #this string slything method does not include the last character
latter = move[3:5]
print (former, latter)

#2
slice = move.split(" ")
mfrom = slice[0]
mto = slice[1]

print(mfrom, mto)
