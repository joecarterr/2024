import random

again = True
card_options = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_cards = [random.choice(card_options), random.choice(card_options)]
user_cards = [random.choice(card_options), random.choice(card_options)]

print(f"The users cards are, {user_cards}")
print(f"The dealers cards are, {dealer_cards}")

user_total = sum(user_cards)
dealer_total = sum(dealer_cards)
    
print(f"\nYour total is, {user_total}")
print(f"\nThe dealers total is, {dealer_total}")

while again:
    
    if user_total == 21:
        print("\nBLACKJACK!")
        quit()
    
    if dealer_total == 21:
        print("\nDealer got blackjack")
        quit()

    if user_total > 21:
        print("\nYour score is greater than 21, you lose")

    if dealer_total > 21:
        dealer_total = sum(dealer_cards)
        print(f"\nYou win, the dealer went bust with a score of {dealer_total}")

    another_card = input("\nWould you like to take another card?: ")

    if another_card == "yes":
        user_cards.append(random.choice(card_options))
        user_total = sum(user_cards)
        print(f"\nYour cards are {user_cards}\nYour new total is {user_total}")
    if another_card == "no":
        if dealer_total < 17:
                dealer_cards.append(random.choice(card_options))
                dealer_total = sum(dealer_cards)
                print(f"\nThe dealer has taken another card, their total is {dealer_total}")
        if dealer_total > 17:
             dealer_total = sum(dealer_cards)
             print(f"\nThe dealer cannot take anymore cards, their final score was {dealer_total}")

             if user_total > dealer_total:
                print(f"\nYou win, your score was greater than the dealers")
             if user_total < dealer_total:
                print(f"\nYou lose, the dealer had a greater score than yours")
             if user_total == dealer_total:
                print("\nYou drew, you and the dealer both had the same score")
            
         

    
    


