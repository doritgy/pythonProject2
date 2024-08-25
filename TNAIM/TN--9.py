import functions.funds
number:int = 0
while True:
    try:
        number =  functions.funds.enterInteger("please enter an integer")
        print("the  number is even" if number % 2 == 0 else "the number is odd")
        break
    except Exception as e:
        print(f"the number you entered is wrong, {e}, please try again")
        continue