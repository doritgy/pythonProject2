import functions.funds
myNum:int = 0
mySearch:int = 0
newNum:int = 1
try:
    myNum = functions.funds.enterInteger("please enter a number")
    mySearch = functions.funds.enterInteger("please enter the search number")
except Exception as e:
    print("something went wrong please try next time")
if myNum and mySearch:
    newNum = myNum // 10
    search = myNum % 10
    while newNum:
        if search  == mySearch:
            print("match found")
            break
        newNum = newNum // 10
        search = newNum % 10
    else:
        print(f"there was no match")