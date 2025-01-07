from random import randint

def check_answer (guess, answer):
    if guess>answer:
        print("Too High")
    elif guess<answer:
        print("Too low")
    else:
        print(f"You got it hurray!! \nThe answer was: {answer}")

def game():
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    attempts = 0
    guess = 0
    while guess != answer:
        guess = int(input("Make a guess: "))
        attempts += 1
        check_answer(guess, answer)
        if guess != answer:
            print("Guess again")
    print(f"It took you {attempts} attempts. Good Game")


game()
    