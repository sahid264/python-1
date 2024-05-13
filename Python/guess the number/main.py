from random import randint
from art import logo
print(logo)

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5



def check_answer(guess,answer,turns):
    if guess > answer:
        print("too high")
        return turns -1
    elif guess < answer:
        print("too low")
        return turns -1
    else:
        print(f"you got it!the answer is {answer}.")


def set_difficituly():
    level = input("choose a difficulty . Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN

def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking a number between 1 to 100.")
    answer = randint(1, 100)
    #print(f"{answer}")

    turns = set_difficituly()
    
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts to guess the number.")

        guess = int(input("make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you have run out of guess, you lose.")
            return
        elif guess != answer:
            print("Guess again.")



game()





