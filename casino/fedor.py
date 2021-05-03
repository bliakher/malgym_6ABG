import random as rnd
import time as tm


def game_lobby(balance):
    check_balance(balance)
    while True:
        choice = input("select a game: die roll or blackjack [1/2] or finish playing [end]: ")
        if choice == "1":
            roll_die(balance)
            break
        elif choice == "2":
            blackjack(balance)
            break
        elif choice == "end":
            if balance > 200:
                results = "made " + str(balance - 200)
            else:
                results = "lost " + str(200 - balance)
            print(f"during your time in the casino you {results} tokens, come again")
            break
        print("incorrect usage (please type in [1] or [2] or [end])")


def check_balance(blnc):
    if blnc <= 0:
        tm.sleep(0.8)
        print("your balance has run out")
        waiting(3, 3)
        print("you've just recieved another 200 tokens, on the house this time")
        blnc = 200
    print(f"your current balance is {blnc}")
    return blnc


def roll_die(balance):
    print("welcome to the die roll")
    guess = input("pick a number from 1 to 6: ")
    num = rnd.randint(1, 6)
    print("rolling die", end='')
    waiting(6, 11)
    bet = check_bet(balance)
    if int(guess) == num:
        print(f"congratulations! the die has rolled a {guess}, you win 3x {bet} token(s)")
        balance += 3*bet
    else:
        print(f"the die has rolled a {num}, you lose {bet} token(s)")
        balance -= bet
    check_balance(balance)
    play_again(1, balance)


def waiting(i, j):
    tm.sleep(0.6)
    for i in range(rnd.randint(i, j)):
        print(".", end='')
        tm.sleep(0.5)
    print("")


def check_bet(blnc):
    while True:
        bet = int(input("place your bet: "))
        if bet > blnc:
            print("not enough credit, enter lower number")
            check_balance(blnc)
        elif bet < 1:
            print("you must bet some amount after you've entered the round")
        else:
            return bet


def play_again(game, blnc):
    while True:
        choice = input("would you like to play again [y/n]? ")
        if choice == "y":
            if game == 1:
                roll_die(blnc)
                break
            else:
                blackjack(blnc)
                break
        if choice == "n":
            game_lobby(blnc)
            break
        print("incorrect usage (please type in [y] or [n])")


def blackjack(balance):
    deck = make_deck()
    print("welcome to the blackjack table")
    bet = check_bet(balance)
    hand = []
    deck, hand = draw_card(deck, hand)
    dhand = []
    deck, dhand = draw_card(deck, dhand)
    waiting(3, 6)
    print(f"you have been dealt a(n) {hand[0]}\nthe dealer dealt themselves a(n) {dhand[0]}")
    choice = "h"
    while choice == "h":
        deck, hand = draw_card(deck, hand)
        waiting(4, 6)
        print(f"you have been dealt a(n) {hand[-1]}: {hand}")
        if sum(hand) > 21:
            print(f"you went bust, you lose {bet} token(s)")
            balance -= bet
            break
        elif 21 == ace_sum(hand) and 10 in hand and 1 in hand:
            print(f"blackjack! you win 2x {bet} token(s)")
            balance += 2 * bet
            break
        while True:
            choice = input("do you hit or stand? [h/s]: ")
            if choice == "s":
                while True:
                    deck, dhand = draw_card(deck, dhand)
                    waiting(3, 4)
                    print(f"the dealer's next card is {dhand[-1]}: {dhand}")
                    tm.sleep(0.6)
                    if sum(dhand) > 21:
                        print(f"the dealer has went bust, you win {bet} token(s)")
                        balance += bet
                        break
                    elif ace_sum(dhand) > ace_sum(hand):
                        print(f"the dealer's hand wins, you lose {bet} token(s)")
                        balance -= bet
                        break
                    elif sum(dhand) > 16:
                        if ace_sum(dhand) == ace_sum(hand):
                            print("draw, you have reclaimed your bet")
                            break
                        print(f"your hand wins, you win {bet} token(s)")
                        balance += bet
                        break
                break
            elif choice == "h":
                break
            print("incorrect usage (please type in [h] or [s])")
    balance = check_balance(balance)
    play_again(2, balance)


def make_deck():
    deck = []
    for i in range(1, 14):
        for j in range(4):
            if i > 10:
                deck.append(10)
            else:
                deck.append(i)
    return deck


def draw_card(dck, plr):
    plr.append(rnd.choice(dck))
    dck.remove(plr[-1])
    return dck, plr


def ace_sum(cards):
    if 1 in cards and sum(cards) + 10 < 22:
        return sum(cards) + 10
    return sum(cards)


print("welcome to your local casino!")
game_lobby(200)
