import statistics, functions.funds
numbers:list[int] = []
for i in range(2):
    try:
        numbers.append(functions.funds.enterInteger("please enter an integer"))
    except Exception as e:
        if numbers:
            numbers.pop()
        print(f"something went wrong, {e}, please try again")
        continue
print(f"the average of numbers entered is: {statistics.mean(numbers) :.2f}")
