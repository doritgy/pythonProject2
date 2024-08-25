import functions.funds
numbers:list[int] = []
count:int = 0
while count < 2:
    numbers.append(functions.funds.enterInteger("enter an integer"))
    count += 1

print(f"the lowest number entered is: {min(numbers)}")