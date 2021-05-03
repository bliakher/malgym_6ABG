import random as rnd
import time
coin_status = 500
print("Welcome to Giorgi's Grand Casino. The place where dreams are becoming true.")
print()
print(f"You currently have {coin_status} $")
print()

def try_again_to_spin(coin_status):
    while True:
        choice = input("Do you want to play roulette again? [yes/no]    ")
        if choice == "yes":
            roulette(coin_status)
        else:
            main(coin_status)
            break

def spinning():
    for i in range(10):
        time.sleep(0.5)
        print(".", end="")
    print()


def try_again_to_toss(coin_status):
        continue_tossing = True
        choice = input("Do you want to continou? [yes/no]    ")
        if choice == "yes":
            continue_tossing = True
            toss_a_coin(coin_status)
        else:
            continue_tossing = False
            main(coin_status)
        return continue_tossing

def bet_check(bet):
    is_all_ok = True

    if bet <= coin_status and bet > 0:
        is_all_ok = True
        print("your bet is counted")
        print()
    else:
        print("sorry, but you can't afford that much money, you'll be returned and maybe bet acceptable amount of money :)")
        is_all_ok = False

    return is_all_ok

def colour_bet(coin_status):
    print(f"you currently have {coin_status} $")
    print()
    choice = input("Which one are you bettin on? [red/black]    ")
    bet = int(input("How much do you want to bet? You can bet only as much as you have.     "))
    print()    
    if bet_check(bet) == False:
        return coin_status
    num = rnd.randint(1,36)
    if num % 2 == 1:
        colour = "red"
    else:
        colour = "black"
    print("roulette spinning", end="") 
    spinning()
    print(f"Spinned colour is: {colour}.")
    if colour == choice:
        win = bet * 2
        print("You won!")
        print()
    else:
        win = - bet
        print("Damn it, not today. Maybe you should try again.")
        print()
    coin_status = coin_status + win
    print(f"you currently have {coin_status} $")
    print()
    try_again_to_spin(coin_status)

def number_bet(coin_status):
    print(f"You currently have {coin_status} $")
    print()
    num = rnd.randint(1,36)
    choice = int(input("Which number are you betting on? 1-36     "))
    bet = int(input("How much do you want to bet? You can bet only as much as you have.     "))
    if bet_check(bet) == False:
        return coin_status
    print("roulette spinning", end="") 
    spinning()
    print(f"Spinned number is: {num}")


    if choice == num:
        win = bet * 36
        print("You won!")
        print()
    else:
        win = -bet
        print("Damn it, not today. Maybe you should try again.")
        print()
    coin_status = coin_status + win
    print(f"you currently have {coin_status} $")
    print()
    try_again_to_spin(coin_status)

def roulette(coin_status):
    choice = input("Which one do you want to bet on to [number/colour]?   ")
    if choice == "colour":
        colour_bet(coin_status)
    elif choice == "number":
        number_bet(coin_status)
    else:
        return coin_status

def toss_a_coin(coin_status):
    print(f"You currently have {coin_status} $")
    print()
    bet = int(input("How much do you want to bet? You can bet only as much as you have.    "))
    if bet_check(bet) == False:
        return coin_status

    answer = input("What is going to be your choice? [heads/tails]    ")
    print()
    coin = ["tails", "heads"]
    number = rnd.choice(coin)
    print(f"Actual coin toss: {number}")
    print()
    if answer == number:
        win = + bet
        print("You Won!")
        print()
    else:
        win = - bet
        print("Damn it, not today. Maybe you should try it next time.")
        print()
    coin_status = coin_status + win
    print(f"you currently have {coin_status} $")
    print()
    try_again_to_toss(coin_status)


def main(coin_status):
    answer = input(
        "Which one do you want to play [roulette/toss a coin] or [end]    ")
    if answer == "toss a coin":
        coin_status = toss_a_coin(coin_status)
    elif answer == "roulette":
        roulette(coin_status)
    else:
        print("Thanks for visiting our casino, please feel free to come back as soon as possible")
        quit()
    return coin_status


while True:
    coin_status = main(coin_status)
