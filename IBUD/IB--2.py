import functions.funds
num:int = None
lowest:int = 9999999
biggest:int = 0
lastNum:int = 0
num = functions.funds.enterInteger("please type an integer")
##lastNum = num
num = None  if num <= 0 else num
lastNum = num
while num:
    biggest = num if num >= lastNum else  biggest
    lowest = num  if num <= lastNum else lowest
    lastNum = num
    num = functions.funds.enterInteger("please type an integer")
    if not num:
        num = lastNum
        break
if num:
    print(f"biggest {biggest} lowest {lowest}")
else:
    print("None")
