import functions.funds, statistics
tempList:list[int] = []
ind:int = 0
maxTemp:int = None
minTemp:int = None
avgTemp:int = None
lastTemp:int = -6
while ind < 12:
    try:
        tempList.append(functions.funds.enterInteger("enter the average temprature for the month"))
        if -5 > tempList[ind] > 40:
            print("something went wrong, try again")
            continue
        if tempList[ind - 1] == 0 and tempList[ind] == 0:
            ind -= 1
            print("two zero temps in a row, try again")
            continue
        lastTemp = tempList[ind]
        ind += 1
    except Exception as e:
        print("you entered a wrong number", e, "try again")
        continue

print("templist", tempList)
maxTemp = max(tempList)
minTemp = min(tempList)
avgTemp = statistics.mean(tempList)
print(f"max: {maxTemp} min: {minTemp} avg: {avgTemp}")

