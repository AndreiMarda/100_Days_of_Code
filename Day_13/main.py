from art import logo, vs
from game_data import data
from random import choice

def random_registration(data):
    return choice(data)

def game_over(logo, score):
    print("\n" * 20)
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")

def format_data(elem):
    name = elem["name"]
    desc = elem["description"]
    country = elem["country"]
    return f"{name}, a {desc}, from {country}"

def check_answer(guess, elem1, elem2):
    if elem1 > elem2:
        return guess == "a"
    else:
        return guess == "b"

def game(score, elem2):
    if score == 0 or elem2 == 0:
        elem1 = random_registration(data)
        elem2 = random_registration(data)
    else:
        elem1 = elem2
        elem2 = random_registration(data)
    if elem1 == elem2:
        elem2 = random_registration(data)

    print("\n" * 20 + logo, end="")

    if score != 0:
        print(f"You're right! Current score: {score}.")

    print(f"Compare A: {format_data(elem1)}.")
    print(f"hint_A: {elem1["follower_count"]}.")
    print(vs + f"Against B: {format_data(elem2)}.")
    print(f"hint_B: {elem2["follower_count"]}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    is_correct = check_answer(guess, elem1["follower_count"], elem2["follower_count"])

    if is_correct:
        game(score+1, elem2)
    else:
        game_over(logo, score)

score = 0
game(score, 0)
