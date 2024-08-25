import functions.funds
numbers:list[int] = []
for i in range(3):
    try:
        numbers.append(functions.funds.enterInteger("please enter an integer"))
    except Exception as e:
        if numbers:
            numbers.pop()
        print(f"something went wrong, {e}, please try again")
        continue
print(f"the largest number entered is: {max(numbers)}")
