import functions.funds
max:int = None
den:int = None
j:int = 0
while True:
    try:
        max = functions.funds.enterInteger("please type a positive integer for max")
        den = functions.funds.enterInteger("please type a positive integer for den")
        if max < 0:
            print("max has to be positive, please try again" )
            continue
        if den < 0:
            print("den has to be positive, please try again")
            continue
        break
    except Exception as e:
        print("something went wrong try again")
        continue
while j <= max:
    print(j if j % den == 0 else "", end = " ")
    j += 1