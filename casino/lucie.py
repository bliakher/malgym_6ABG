import random as rnd
import time
def bet(a):
    bet = int(input(f"How much do you bet? "))
    while bet > a:
        print(f"That's more money than you have?(You can only bet ${a} and less)")
        bet = int(input("How much do you bet? "))
    return bet
def win_or_loose(a, b, c, money_bet):
    if b == c:
        print ("You win!")
        a += money_bet
    else:
        print ("You loose.")
        a -= money_bet
    print(f"You have ${a}...")
    return a
def three_dots():
    for i in range(3):
        time.sleep(1)
        print(".")
    time.sleep(1)
def flip_a_coin(a):
    user_side_coin = input("Choose [heads] or [tails]: ")
    coin_sides = ["heads", "tails"]
    money_bet = bet(a)
    print("The coin is going to flip now.")
    three_dots()
    coin_side = rnd.choice(coin_sides)
    print(f"The coin's landed on {coin_side}.")
    a = win_or_loose(a, coin_side, user_side_coin, money_bet)
    return a
def wheel_spin():
    print("The wheel and the ball are going to spin now.")
    three_dots()
    number = rnd.randint(1, 36)
    colour = pocket_colour(number)
    print(f"The ball's fallen into {colour} pocket number {number}.")
    return number
def pocket_colour(x):
    if x % 2 == 0:
        colour = "red"
    else:
        colour = "black"
    return colour
def roulette(a):
    bet_question = input("Do you want to bet on a [number] or [colour]? ")
    if bet_question == "number":
        number_bet = int(input("Choose a number from 1 to 36: "))
        money_bet = bet(a)
        number = wheel_spin()
        if number == number_bet:
            print ("You win!")
            a += money_bet * 35
            print(f"You have ${a}...")
        else:
            print ("You loose.")
            a -= money_bet
            print(f"You have ${a}...")
    elif bet_question == "colour":
        colour_bet = input("Choose a colour: [black] or [red] ")
        money_bet = bet(a)
        number = wheel_spin()
        colour = pocket_colour(number)
        a = win_or_loose(a, colour, colour_bet, money_bet)
    return a
def game_cycle(b, funkce):
    while True:
            b = funkce(b)
            if b > 0:
                answer = input("Do you want another game? [y/n]: ")
                if answer == "y":
                    True
                else:
                    game_menu(b)
                    break
            else:
                print("You can't play anymore. You've lost all your money.")
                break
def game_menu(b):
    game = input("Choose a game: [flip a coin/roulette] or [end] ")
    if game == "flip a coin":
        game_cycle(b, flip_a_coin)
    elif game == "roulette":
        game_cycle(b, roulette)
    else: print ("Goodbye, come back soon!") 
print("Welcome to Lucie's casino! You have $500 to start with.")
bank = 500
game_menu(bank)

