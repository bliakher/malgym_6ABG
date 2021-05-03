
#THINGS TO WORK ON
#short form for input Tails or Heads

import random as rnd


def coin(bank):
    print("Explanation: In this game a coin will be thrown into the air. You are going to guess which side of the coin will be shown when it lands, in order to choose between two alternatives, heads or tails.\n")
    bet_coin = input("Do you bet on [Heads] or [Tails]? (Be careful - any spelling mistake could cost you a lot of money!)\n")
    bet = bet_and_check(bank)
    print("The coin is flipping", end = " ")
    tension()
    if bet_coin == coin_flip():
        bank = win(bank, bet)
    else:
        bank = lost(bank, bet)
    print("You have now $ %d in your bank" %bank)
    return bank

def coin_flip():
    num = rnd.randint(1,2)
    if num == 2:
        return "Heads"
    else:
        return "Tails"



def roulette(bank):
    print("Explanation: At a casino, the roulette wheel is composed of alternating red and black slots, each slot with its own number. You can bet on a colour or on a number between 0 and 49 that you think will be chosen. If you guess the number correctly you will win FIFTY times your bet!\n")
    while True:
        choosing_r_game = input("Do you want to guess the [colour] or the [number]? You can also press [c] for [colour] or [n] for [number] \n")
        
        if choosing_r_game == "colour" or choosing_r_game == "c":
            bank = guessing_colour(bank)
            break
        elif choosing_r_game == "number" or choosing_r_game == "n":
            bank = guessing_num(bank)
            break
        else:
            print("Oops, something went wrong...")
            continue    
    return bank

    
def guessing_colour(bank):
    bet_colour = input("You decided to guess the colour. Do you bet on [black] or [red]?\n")
    bet = bet_and_check(bank)
    if bet_colour == spin_colour():
        bank = win(bank, bet)
    else:
        bank = lost(bank, bet)
    print("You have now $ %d in your bank" %bank)
    return bank

def guessing_num(bank):
    bet_num = int(input("You decided to guess the number. What number do you bet on?\n"))
    bet = bet_and_check(bank)
    if bet_num == spin_num():
        bank = win(bank, bet)*50
    else:
        bank = lost(bank, bet)
    print("You have now $ %d in your bank" %bank)
    return bank


def win(bank, bet):
    print("Congratulations, you won!")
    bank += bet
    return bank


        
def lost(bank, bet):
    print("You lost, maybe next time?")
    bank -= bet
    return bank



def spin_colour():
    num = rnd.randint(0, 49)
    if num % 2 == 0:
        colour = "black"
    else:
        colour = "red"
    print("The roulette is spinning", end = " ")
    tension()
    print("The colour was: " + colour)
    return colour

def spin_num():
    num = rnd.randint(0, 49)
    print("The roulette is spinning", end = " ")
    tension()
    print("The number was: %d " %num)
    return num

        
def tension():
    import time
    for i in range(5):
        time.sleep(1)
        print(".", end = " ")
    print("\n")



    
def bet_and_check(bank):
    bet = int(input("How much $ do you want to bet?\n"))
    while True:
        if bank >= bet:
            break
        else:
            print("You don't have enough money in your bank")
            bet = int(input("How much $ do you want to bet?\n"))
            continue
    return bet



def casino():
    bank = 500
    print("Welcome to Jana's Casino!")
    print ("We'll give you $ %d to start with." %bank)
    while True:
        game = input("Choose a game that you want to play: [coin/roulette] or [end]\n")
        if game == "end":
            print("Goodbye, see you soon!")
            break
        elif game == "coin":
            bank = coin(bank)
        elif game == "roulette":
            bank = roulette(bank)
        else:
            print("Oops, something went wrong...")
            continue

casino()
