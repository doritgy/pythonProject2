import functions.funds
number:int = 0
while True:
    try:
        number =  functions.funds.enterInteger("please enter a two digin number")
        if number <= 9 or number > 99:
            print("the number you entered is not 2 digit")
            continue
        print(f" the sum of it's digits is {number % 10 + number // 10}")
        break
    except Exception as e:
        print(f"the number you entered is wrong, {e}, please try again")
        continue
