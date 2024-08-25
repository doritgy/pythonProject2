import functions.funds
myList:list[int] = []
count:int = 0
mul:int = 0

try:
    myList = [functions.funds.enterInteger("please enter an integer") for _ in range(2)]
    count += 1
except Exception as e:
    print("something went wrong please try next time")
    myList = []
if myList:
    for i in range(myList[1]):
        mul += myList[0]
print(f"the multiplication of the numbers is {mul}")