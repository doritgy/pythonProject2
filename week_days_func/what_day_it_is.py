def what_day(x:int) -> str:
    if str(x).isalpha():
        raise ValueError("day number not numeric")
    if x < 1 or x > 7:
        raise ValueError("number out of range")
    match x:
        case 1:
            return "sunday"
        case 2:
            return "monday"
        case 3:
            return "thursday"
        case 4:
            return "wednsday"
        case 5:
            return "tuesday"
        case 6:
            return "friday"
        case 7:
            return "saturday"

    def get_day():
        while True:
            try:
                x:int = int(input("please type the number of week day"))
                print(what_day(x))
                break
            except Exception as e:
                print("you typed a bad number, try again")
                continue


