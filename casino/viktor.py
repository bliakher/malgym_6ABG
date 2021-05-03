import random
doge_coins = 50
bet = 0
what = 0
def main_menu():
    print("CASINO")
    print("What would you like to play?")
    print("Roulette: 1")
    print("Coin_flip: 2")
    game = int(input())
    if game == 2:
        coin_flip()
    if game == 1:
        roulete_menu()

def coin_flip():
    global doge_coins
    print("what side?")
    print("heads: 1")
    print("tails: 2")
    side = int(input())
    print("how much?")
    bet = int(input())
    if bet > doge_coins:
        print("insuficient funds")
        coin_flip()
    doge_coins = doge_coins - bet
    coin = random.randint(1,2)
    if side == coin:
        print("you win!!")
        bet = bet + bet
        doge_coins = doge_coins + bet
        bet = 0
        print("balance:", doge_coins)
        print("Want to play again?")
        print("Yes: 1")
        print("No: 2")
        want_to_play = int(input())
        if want_to_play == 1:
            coin_flip()
        else:
            main_menu()
    else:
        print("you lose")
        bet = 0
        print("balance:", doge_coins)
        print("Want to play again?")
        print("Yes: 1")
        print("No: 2")
        want_to_play = int(input())
        if want_to_play == 1:
            coin_flip()
        else:
            main_menu()

def roulete_color():
    print("red:1")
    print("black:2")
    color = int(input())
    print("how much do you want to bet?")
    global doge_coins
    print("balance:",  doge_coins)
    bet = int(input())
    if bet > doge_coins:
        print("insuficient funds")
        roulete_color()
    doge_coins = doge_coins - bet
    winning_number = random.randint(1,36)
    if winning_number < 19 and color == 1 or winning_number > 18 and color == 2:
        print("YOU WIN!")
        bet = bet + bet
        doge_coins = doge_coins + bet
        bet = 0
        print("balance:",doge_coins)
        print("want to play again?")
        print("yes: 1")
        print("no: 2")
        want_to_play = int(input())
        if want_to_play == 1:
            roulete_color()
        else:
            main_menu()
    else:
        print("YOU LOSE!")
        bet = 0
        print("balance:",doge_coins)
        print("want to play again?")
        print("yes: 1")
        print("no: 2")
        want_to_play = int(input())
        if want_to_play == 1:
            roulete_color()
        else:
            main_menu()

def number_guess():
    print("What number?")
    number = int(input())
    print("how much do you want to bet?")
    global doge_coins
    print("balance:", doge_coins)
    bet = int(input())
    if bet > doge_coins:
        print("insuficient funds")
        number_guess()
    doge_coins = doge_coins - bet
    winning_number = random.randint(1,36)
    if winning_number == number:
        print("YOU WIN")
        bet = bet*36
        doge_coins = doge_coins + bet
        bet = 0
        print("balance:",doge_coins)
        print("want to play again?")
        print("yes: 1")
        print("no: 2")
        want_to_play = int(input())
        if want_to_play == 1:
            number_guess()
        else:
            main_menu()
    else:
        print("YOU LOSE!")
        bet = 0
        print("balance:",doge_coins)
        print("want to play again?")
        print("yes: 1")
        print("no: 2")
        want_to_play = int(input())
        if want_to_play == 1:
            number_guess()
        else:
            main_menu()

def even_uneven():
    print("even:1")
    print("uneven:2")
    even_uneven_variable = int(input())
    print("how much do you want to bet?")
    global doge_coins
    print("balance:", doge_coins)
    bet = int(input())
    if bet > doge_coins:
        print("insuficient funds")
        even_uneven()
    doge_coins = doge_coins - bet
    winning_number = random.randint(1,36)
    if even_uneven_variable == 1 and (winning_number % 2) == 0 or even_uneven_variable == 2 and (winning_number % 2) != 0:
        print("YOU WIN")
        doge_coins = doge_coins + bet + bet
        bet = 0
        print("balance:",doge_coins)
        print("want to play again?")
        print("yes: 1")
        print("no: 2")
        want_to_play = int(input())
        if want_to_play == 1:
            even_uneven()
        else:
            main_menu()
    else:
        print("YOU LOSE!")
        bet = 0
        print("balance:",doge_coins)
        print("want to play again?")
        print("yes: 1")
        print("no: 2")
        want_to_play = int(input())
        if want_to_play == 1:
            even_uneven()
        else:
            main_menu()



def roulete_menu():
    print("What do you want to bet on?")
    print("color:1")
    print("number:2")
    print("even/uneven:3")
    what = int(input())
    if what == 1:
        roulete_color()
    if what == 2:
        number_guess()
    if what == 3:
        even_uneven()
    

main_menu()       

            

