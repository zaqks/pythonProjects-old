from math import pow

mypin ="57949"

"gen nums lst"

pinLength = len(mypin)
maxnum = pow(10, pinLength)- 1

combs = []

i = 0

def addZeros(numStr, nZ):
    tmpStr = ""

    i = 0

    while i != nZ:
        i += 1
        tmpStr += "0"
    tmpStr += numStr
    
    print(tmpStr + " was added")
    return tmpStr

    

while i != maxnum:
    i += 1
    combs.append(addZeros(str(i), pinLength-len(str(i))))
   
    



"test the combs"

a = 0
while combs[a] != mypin:
    print("test number " + str(a+1) + " : " + combs[a])
    a += 1

else:
    print("the pin was " + combs[a])

