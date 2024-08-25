import functions.funds
num:int = None
j:int = 0
while True:
    try:
        num = functions.funds.enterInteger("please type a positive integer")
        if num < 0:
            print("the number has to be positive, please tryt agaub")
            continue
        break
    except Exception as e:
        print("something went wrong try again")
        continue
while j <= num:
    print(j if j % 2 == 0 else "", end = "")
    j += 1


