import functions.funds
myList:list[int] = []
myDens:list[int] = []
den:int = 2
endOfIter:bool = False
biggestDen:int = 1
try:
    myList = [functions.funds.enterInteger("please enter an integer") for _ in range(2)]
except Exception as e:
    print("something went wrong please try next time")
    myList = []
if myList:
    if myList[1] < myList[0]:
        myPop = myList.pop()
        myList.insert(0, myPop)
        print("after swap:", myList)
    biggestDen = myList[0] if myList[1] % myList[0] == 0 else biggestDen
    endOfIter = True if myList[1] % myList[0] == 0 else endOfIter
    while not endOfIter:
        if den == myList[0] or myList[0] == 0:
            endOfIter = True
            break
        if myList[0] % den == 0 and myList[1] % den == 0:
            myList[0] = myList[0] // den
            myList[1] = myList[1] // den
            myDens.append(den)
        else:
            den += 1
    print("myDens:", myDens)
    if myDens:
        for i in range(len(myDens)):
            biggestDen *= myDens[i]
    print("the biggest den is:", biggestDen)










