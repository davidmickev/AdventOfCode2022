# [G]                 [D] [R]        
# [W]         [V]     [C] [T] [M]    
# [L]         [P] [Z] [Q] [F] [V]    
# [J]         [S] [D] [J] [M] [T] [V]
# [B]     [M] [H] [L] [Z] [J] [B] [S]
# [R] [C] [T] [C] [T] [R] [D] [R] [D]
# [T] [W] [Z] [T] [P] [B] [B] [H] [P]
# [D] [S] [R] [D] [G] [F] [S] [L] [Q]
#  1   2   3   4   5   6   7   8   9 
import sys

def stackalter(ffrom,to,amt):
    ffrom = getattr(sys.modules[__name__], ffrom)
    to = getattr(sys.modules[__name__], to)
    
    for i in range(int(amt)):
        removed = ffrom.pop()
        to.append(str(removed))

def stackalterpart2(ssffrom,ssto,amt):
    ffrom = getattr(sys.modules[__name__], ssffrom)
    to = getattr(sys.modules[__name__], ssto)
    amt = int(amt)

    # ffrom = ffrom[:-3]
    # ffrom = ffrom[:len(ffrom)-amt or None]
    # to = to+removed

    removed = ffrom[-amt:]

    # need this to update "global" scope array stacks
    setattr(sys.modules[__name__], ssffrom,ffrom[:len(ffrom)-amt or None])
    setattr(sys.modules[__name__], ssto,to+removed)
    

stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9 = ([] for stack in range(9))

#INIT
one = "DTRBJLWG"
for c in one: stack1.append(c)
# orcando
stack2.extend(["S","W","C"])
stack3.extend(["R","Z","T","M"])
stack4.extend(["D","T","C","H","S","P","V"])
stack5.extend(["G","P","T","L","D","Z"])
stack6.extend(["F","B","R","Z","J","Q","C","D"])
stack7.extend(["S","B","D","J","M","F","T","R"])
stack8.extend(["L","H","R","B","T","V","M"])
stack9.extend(["Q","P","D","S","V"])

with open("input5.txt") as input:
    for line in input:
        newline = line.split()
        #print("amt = ", newline[1], " from = ", newline[3], " to = ", newline[5])

        #part1 solution
        #stackalter("stack"+newline[3],"stack"+newline[5],newline[1])

        #part2 solution
        stackalterpart2("stack"+newline[3],"stack"+newline[5],newline[1])

    for i in range(1,10):
        stacknum = getattr(sys.modules[__name__], "stack"+str(i))
        print(stacknum[-1])