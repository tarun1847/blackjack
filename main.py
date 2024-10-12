import random
from os import remove

def get_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calc_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user, computer):
    if user==computer:
        return "It's a DRAW!"
    elif user == 0:
        return "BLACKJACK OBTAINED....You win!"
    elif computer == 0:
        return "Computer Win with a BLACKJACK"
    elif user > 21:
        return "You went over the limit, You Lose!"
    elif computer > 21:
        return "Computer went over the limit, You win!"
    elif user>computer:
        return "You Win!"
    else:
        return "You lose!"

def start_game():
    print("WELCOME TO BLACKJACK!!!")
    user_cards=[]
    user_score=-1
    computer_cards=[]
    computer_score=-1
    game_over= False

    for _ in range(2):
        user_cards.append(get_card())
        computer_cards.append(get_card())

    while not game_over:
        user_score=calc_score(user_cards)
        computer_score=calc_score(computer_cards)
        print(f"Your cards: {user_cards} and Your current score is: {user_score}")
        print(f"Computer's card: {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            game_over=True
        else:
            want_third_card=input("type 'y' if you want third card or 'n' to pass: ")
            if want_third_card=="y":
                user_cards.append(get_card())
                print('\n' * 20)
            else:
                game_over=True

    while computer_score !=0 and computer_score<17:
        computer_cards.append(get_card())
        computer_score = calc_score(computer_cards)

    print(f"Computer's final cards were {computer_cards} and score: {computer_score}")
    print(compare(user_score, computer_score))

while input("type 'y' to play again or 'n' to exit the game: ")=='y':
    print('\n'*20)
    start_game()