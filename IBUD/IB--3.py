import functions.funds
myList:list[int] = []
count:int = 0
biggest:int = 0
place:int = 0

while count < 5:
    try:
        myList.append(functions.funds.enterInteger("please print an integer"))
        count += 1
    except Exception as e:
        print("something went wrong please try again")
        continue
biggest = max(myList)
print(f"the biggest number is in place {myList.index(biggest) + 1}")

