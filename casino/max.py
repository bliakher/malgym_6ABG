
import random
import time

print("")

print(r""" /$$      /$$                     /$$               /$$$$$$                      /$$                    
| $$$    /$$$                    | $/              /$$__  $$                    |__/                    
| $$$$  /$$$$  /$$$$$$  /$$   /$$|_//$$$$$$$      | $$  \__/  /$$$$$$   /$$$$$$$ /$$ /$$$$$$$   /$$$$$$ 
| $$ $$/$$ $$ |____  $$|  $$ /$$/  /$$_____/      | $$       |____  $$ /$$_____/| $$| $$__  $$ /$$__  $$
| $$  $$$| $$  /$$$$$$$ \  $$$$/  |  $$$$$$       | $$        /$$$$$$$|  $$$$$$ | $$| $$  \ $$| $$  \ $$
| $$\  $ | $$ /$$__  $$  >$$  $$   \____  $$      | $$    $$ /$$__  $$ \____  $$| $$| $$  | $$| $$  | $$
| $$ \/  | $$|  $$$$$$$ /$$/\  $$  /$$$$$$$/      |  $$$$$$/|  $$$$$$$ /$$$$$$$/| $$| $$  | $$|  $$$$$$/
|__/     |__/ \_______/|__/  \__/ |_______/        \______/  \_______/|_______/ |__/|__/  |__/ \______/""")

print("")

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  ")

print("")

print("WELCOME TO MAX'S CASINO, THE FINEST EXAMPLE OF ANARCHO-CAPITALISM ON GOD'S GREEN EARTH!")




dealer_cards = []
global running
running = True
player_cards = []
global playing
playing = True

player_coins = 500
player_coins = int(player_coins)


def bet(): 
    global players_bet
    global player_coins
    good_credit = True

    print(f"You have {player_coins} coins")

    while good_credit == True:

        players_bet = input("how much do you want to bet? ")

        players_bet = int(players_bet)

        if players_bet > player_coins:
            print("oops! You don't have enough coins for that bet!")
        else:
            break

    print(f"You bet: {players_bet}")

    player_coins = player_coins - players_bet

    print(f"You now have {player_coins} coins.")
    time.sleep(1)


def blackjack_game():
    print(r"""     ________  ___       ________  ________  ___  __          ___  ________  ________  ___  __           
    |\   __  \|\  \     |\   __  \|\   ____\|\  \|\  \       |\  \|\   __  \|\   ____\|\  \|\  \         
    \ \  \|\ /\ \  \    \ \  \|\  \ \  \___|\ \  \/  /|_     \ \  \ \  \|\  \ \  \___|\ \  \/  /|_       
     \ \   __  \ \  \    \ \   __  \ \  \    \ \   ___  \  __ \ \  \ \   __  \ \  \    \ \   ___  \      
      \ \  \|\  \ \  \____\ \  \ \  \ \  \____\ \  \\ \  \|\  \\_\  \ \  \ \  \ \  \____\ \  \\ \  \     
       \ \_______\ \_______\ \__\ \__\ \_______\ \__\\ \__\ \________\ \__\ \__\ \_______\ \__\\ \__\    
        \|_______|\|_______|\|__|\|__|\|_______|\|__| \|__|\|________|\|__|\|__|\|_______|\|__| \|__|    
                                                                                                         """)


    print("")
    
    global player_win
    player_win = False

    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 11))
        if len(dealer_cards) == 2:
            print("Dealer has X &", dealer_cards[1])

    while len(player_cards) != 2:
        player_cards.append(random.randint(1, 11))
        if len(player_cards) == 2:
            print("You have ", player_cards)
 
    if sum(dealer_cards) == 21:
        print("Dealer has 21 and wins!")
    elif sum(dealer_cards) > 21:
        print("Dealer has busted!")
        player_win = True

    while sum(player_cards) < 21:
        action_taken = str(input("Do you want to stay or hit?  "))
        if action_taken == "hit":
            player_cards.append(random.randint(1, 11))
            print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
        else:
            print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
            print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
            if sum(dealer_cards) > sum(player_cards):
                print("Dealer wins!")
                break
            else:
                print("You win!")
                player_win = True
                break

    if sum(player_cards) > 21:
        print("You BUSTED! Dealer wins.")
    elif sum(player_cards) == 21:
        print("You have BLACKJACK! You Win!! 21")
        player_win = True


def coin_flip():
    global player_win
    player_win = False
    print("")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
    print(r"""                ______________
    __,.,---'''''              '''''---..._
 ,-'             .....:::''::.:            '`-.
'           ...:::.....       '
            ''':::'''''       .               ,
|'-.._           ''''':::..::':          __,,-
 '-.._''`---.....______________.....---''__,,-
      ''`---.....______________.....---''""")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("")
    selected_face = input("On which coin face would you like to bet? [Heads, Tails]: " )
    faces = ['Tails', 'Heads']
    top_face = random.choice(faces)

    if top_face == selected_face:
        print(f"You won! {top_face}!")
        player_win = True
    else:
        print(f"{top_face}! Better luck next time!")


def award():
    global player_coins
    if player_win == True:
        player_coins = player_coins + players_bet*2
        print(f"You now have {player_coins} coins.")
    else:
        print(f"You have {player_coins} coins.")

def again_choice():
    global playing
    player_choice = input("Do you want to play again?(y/n): ")
    if player_choice == "n":
        playing = False
    elif player_choice == "y":
        print("OK. Enjoy!")

def play_bj():
    global playing
    playing = True
    global dealer_cards
    global player_cards
    while playing == True:
        bet()
        blackjack_game()
        award()
        again_choice()
        dealer_cards = []
        player_cards = []

def play_coinflip():
    global playing
    playing = True
    while playing == True:
        bet()
        coin_flip()
        award()
        again_choice()

def choice_of_game():

    game_choice = input("What game would you like to play? [A] = Blackjack [B] = Coinflip [C] = Exit: ")

    if game_choice == "A":
        time.sleep(1)
        print("Alright! You are now playing Blackjack, may the odds be ever in your favor!")
        play_bj()
    elif game_choice == "B":
        time.sleep(1)
        print("Alright! You're playing coinflip, enjoy!")
        play_coinflip()
    elif game_choice == "C":
        exit()

while running == True:
    choice_of_game()




