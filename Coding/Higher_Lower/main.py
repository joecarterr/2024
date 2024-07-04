from art import logo, vs
import random
from game_data import data
import os

again = True
score = 0

print(logo)

def clear_screen():
    os.system("cls")

def create_person(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"


person_1 = random.choice(data)
person_2 = random.choice(data)
if person_1 == person_2:
    person_2 = random.choice(data)


while again:
    print(f"Compare A: {create_person(person_1)}")
    print(vs)
    print(f"To B: {create_person(person_2)}")

    user_guess = input("Who has more followers, A or B?: ").upper()

    followers_1 = person_1["follower_count"]
    followers_2 = person_2["follower_count"]

    if (user_guess == "A" and followers_1 > followers_2):
        clear_screen()
        score += 1
        print(f"You're correct! Your score is {score}.\n")
        person_2 = random.choice(data)
        

    if (user_guess == "B" and followers_1 < followers_2):
        clear_screen()
        score += 1
        print(f"You're correct! Your score is {score}.\n")
        person_1 = random.choice(data)

    else:
        clear_screen()
        print(f"Sorry you were incorrect... Your final score was {score}.")
        again = False
