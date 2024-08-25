import functions.funds
num:int = None
sum:int = 0
num = functions.funds.enterInteger("please type an integer")
num = None if num == -99 else num
while (not num == -99) and num:
    sum += num
    num = functions.funds.enterInteger("please type an integer")

print("num:", num, "sum:", sum)

