import functions.funds
number:int = 0
while True:
    try:
        number = functions.funds.enterInteger("please enter a found digit number")
        if number <= 999 or number > 9999:
            print("the number you entered is not 4 digit")
            continue
        print(f" the third digit is {number % 100 // 10}")
        break
    except Exception as e:
        print(f"the number you entered is wrong, {e}, please try again")
        continue
