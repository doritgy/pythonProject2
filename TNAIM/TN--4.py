import functions.funds

inMin:int = None
while True:
    try:
        inMin = functions.funds.enterInteger("please enter a number of nimutes")
        print(f"the length in hours is {inMin // 60} and the minutes are {inMin % 60}")
        break
    except Exception as e:
        print(f"the number you entered is wrong, {e}, please try again")
        continue
