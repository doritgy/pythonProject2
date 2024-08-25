import functions.funds
noToTest:int = 0
ind:int = 2
rishoni:bool = False
noToTest = functions.funds.enterInteger("enter an integer to test please")
while True:
    if noToTest % ind == 0:
        break
    else:
        ind += 1
        if ind == noToTest:
            rishoni = True
            break
print("not" if not rishoni else "", "rishoni")

