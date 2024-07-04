import random

easy_lives = 10
hard_lives = 5

found = False
again = True
random_number = random.randint(1, 100)
print(random_number)
print("Please guess a number between 1 and 100")
difficulty = input("Enter your difficulty: ")


def user_guess(lives_left):
    guess = int(input("Please guess your number: "))
    if guess == random_number:
        global found
        found = True
        print(f"Well done you got the number, the number was {random_number}")
    if guess > random_number:
        print("This guess was too high.")
        return lives_left - 1
    if guess < random_number:
        print("This guess was too low.")
        return lives_left - 1


while again:
    if difficulty == "easy":
        turns_easy = user_guess(lives_left=easy_lives)
        if found == True:
            again = False
        if found == False:
            easy_lives = turns_easy
            print(f"You have {turns_easy} remaining.")
            if turns_easy <= 0:
                print("You ran out of lives")
                print(f"The number was, {random_number}")
                again = False

    if difficulty == "hard":
        turns_hard = user_guess(lives_left=hard_lives)
        hard_lives = turns_hard
        print(f"You have {turns_hard} remaining.")
        if turns_hard <= 0:
            print("You ran out of lives")
            print(f"The number was, {random_number}")
            again = False