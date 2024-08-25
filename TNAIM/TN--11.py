age:float = 0
height:float = 0
number:int = 0
while True:
    try:
        age = float(input("please enter your age"))
        height = float(input("please enter your height in centimeters"))
        print("you can enter" if 8 <= age <= 18 and height > 115 or age > 18 and height > 100 else "you can not enter")
        break
    except Exception as e:
        print(f"the number you entered is wrong, {e}, please try again")
        continue