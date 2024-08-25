import functions.funds
top:int = None
count:int = 0
while True:
    try:
        top = functions.funds.enterInteger("please enter a positive integer")
        if top < 0:
            print("the number you entered is not positive")
            continue
        break
    except exception as e:
        print("something went wrong' please try again")
        continue
for i in range(1,top + 1):
    print(i , end=" " )



