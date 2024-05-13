import random

from art import logo,vs

from game_data import data
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return  guess == "a"
    else:
        return guess == "b"
    





print(logo)
score = 0
game_continue = True
account_b = random.choice(data)


while game_continue:

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A : {format_data(account_a)}.")

    print(vs)
    print(f"Against B : {format_data(account_b)}.")

    guess = input("who has more followers? Type 'a' or 'b': ").lower()


    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers, b_followers)

    clear_console()
    print(logo)


    if is_correct:
        score += 1
        print(f"you are right. current score is: {score}.")
    else:
        game_continue = False
        print(f"sorry, you are wrong. final score is: {score}.")