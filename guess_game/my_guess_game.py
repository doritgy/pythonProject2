import random
def check_guess(lucky_number:int, user_guess:str)->str:
    if user_guess.isalpha():
        raise ValueError("guess is not numeric")

    if user_guess > 100 or user_guess < 1:
        raise valueError("number out of range")

    if lucky_number == int(user_guess):
        return "bingo"
    elif lucky_number < int(user_guess):
        return "try lower"
    else:
        return "try higher"

def play_guessing_game():
    lucky_number:int = random.randint(1, 100)
    while True:
        try:
            user_guess = input("Guess a number between 1-100:")
            feedback: str = check_guess(lucky_number, user_guess)
            print(feedback)
            if feedback == "bingo":
                print("you win, you guessed the number")
                ans = input("do you want to play again? y/n ")
                if ans == 'y':
                    lucky_number: int = random.randint(1, 100)
                    continue
                else:
                    print("bye bye, thanks for playing the game")
                    break
        except Exception as ex:
            print(ex)





