
def enterInteger(message:str):
    integerEntered:int = None
    while True:
        try:
            integerEntered = int(input(message))
            break
        except Exception as e:
            print(f"the number you entered is wrong, {e}, please try again")
            continue
    return integerEntered

if __name__ == '__main__':
    print("the integer entered is:", enterInteger("please enter an integer"))