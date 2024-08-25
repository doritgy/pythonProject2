import functions.funds
myList:list[int] = []
power:int = 1

try:
    myList = [functions.funds.enterInteger("please enter an integer") for _ in range(2)]
except Exception as e:
    print("something went wrong please try next time")
    myList = []
if myList:
    for i in range(myList[1]):
        power *= myList[0]
print(f"the power of the numbers is {power}")