import functions.funds
nums:list[int] = []
num:int = None
i:int = 0
j:int = 0
while i < 2:
    try:
        nums.append(functions.funds.enterInteger("please enter an integer"))
        if i != 0 and nums[i] < nums[i - 1]:
            nums.insert(i - 1, nums.pop())
        i += 1
    except Exception as e:
        print("something went wrong", e)
        continue
j = nums[0]
while j <= nums[len(nums) - 1]:
    print(j, end = "")
    j += 1