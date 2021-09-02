import random as rnd
import time

def blackjack(money):
    print("You chose Blackjack")
    print("You have", money, "$")
    bet = int(input("How much do you want to bet:"))
    if bet<=money:
        your_first=value_dealing()
        your_second=value_dealing()
        print("Your cards:", your_first, symbol_dealing(), " ", your_second, symbol_dealing())
        dealer_first=value_dealing()
        dealer_second=value_dealing()
        print("Dealers cards:", dealer_first, symbol_dealing(), " ", dealer_second, symbol_dealing())
        i=input("Choose to [Hit] or [Stand] (hit means drawing another card, stand means ending turn it means you are satisfied):")
        your_hand=your_first+your_second
        while i=="Hit":
            your_new=value_dealing()
            print("Your new card:", your_new, symbol_dealing())
            your_hand = your_hand + your_new
            if your_hand > 21:
                break
            n=input("Choose to [Hit] again or [Stand]:")
            if n=="Stand":
                break
        print("Value of your cards is ", your_hand)
        if your_hand > 21:
            print("You lose")
            money = money - bet
            print("You have", money, "$")
        else:
            dealer_hand=dealer_first+dealer_second
            while dealer_hand < 17:
                dealer_new=value_dealing()
                print("Dealers new card:", dealer_new, symbol_dealing())
                dealer_hand = dealer_hand + dealer_new
            print("Value of dealers cards is ", dealer_hand)
            if dealer_hand > 21:
                print("You win")
                money = money + bet
                print("You have", money, "$")
            else:
                if your_hand > dealer_hand:
                    print("You win")
                    money = money + bet
                    print("You have", money, "$")
                else:
                    if your_hand < dealer_hand:
                        print("You lose")
                        money = money - bet
                        print("You have", money, "$")
                    else:
                        print("It´s draw")
                        print("You have", money, "$")       
    else:
        print("You don´t have enough money")
    return money

def value_dealing():
    A = 11
    J = 10
    Q = 10
    K = 10
    card_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A]
    a1=rnd.choice(card_value)
    return a1

def symbol_dealing():
    card_symbol = ["♠", "♥", "♦", "♣"]
    a2=rnd.choice(card_symbol)
    return a2

    
def dice_game(money):
    print("You chose Dice game.")
    print("You have", money, "$")
    bet = int(input("How much do you want to bet:"))
    if bet<=money:
        print("Throwing dices")
        for i in range(5):
            time.sleep(0.5)
            print(".", end=" ")
        a=rnd.randint(1, 6)
        b=rnd.randint(1, 6)
        print("Your dice:", a)
        choose_bet = input("Bet on [Higher/Lower]:")
        print("His dice:", b) 
        if choose_bet == "Higher":
            if a>b:
                print("Victory")
                money = money + bet
                print(money)
            elif a<b:
                print("Defeat")
                money = money - bet
                print(money)
            elif a==b:
                print("Draw")
                print(money)
        elif choose_bet == "Lower":
            if a>b:
                print("Defeat")
                money = money - bet
                print(money)
            elif a<b:
                print("Victory")
                money = money + bet
                print(money)
            elif a==b:
                print("Draw")
                print(money)
    else:
        print("You don´t have enough money")
    return money


def menu():
    money = int(input("Enter amount of money you want to play with:"))
    print("Welcome too our casino")
    print("You will start with", money, "$")
    while True:
        choose_game = input("Choose which game you want to play [Blackjack/Dice game] or if you want to go already you can [leave]:")
        if choose_game == "Dice game":
            money = dice_game(money)
        elif choose_game == "Blackjack":
            money = blackjack(money)
        elif choose_game == "leave":
            break
    print("Bye, come again.")

menu()

