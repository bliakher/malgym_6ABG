import random as rnd
import time

game_bank = 750

print(r"""\
$$\   $$\                               $$\           $$\                  $$$$$$\                      $$\                     
$$ | $$  |                              \__|          $$ |                $$  __$$\                     \__|                    
$$ |$$  /  $$$$$$\   $$$$$$\   $$$$$$\  $$\  $$$$$$$\ $$ |  $$\ $$\   $$\ $$ /  \__| $$$$$$\   $$$$$$$\ $$\ $$$$$$$\   $$$$$$\  
$$$$$  /  $$  __$$\ $$  __$$\ $$  __$$\ $$ |$$  _____|$$ | $$  |$$ |  $$ |$$ |       \____$$\ $$  _____|$$ |$$  __$$\ $$  __$$\ 
$$  $$<   $$ |  \__|$$$$$$$$ |$$ /  $$ |$$ |$$ /      $$$$$$  / $$ |  $$ |$$ |       $$$$$$$ |\$$$$$$\  $$ |$$ |  $$ |$$ /  $$ |
$$ |\$$\  $$ |      $$   ____|$$ |  $$ |$$ |$$ |      $$  _$$<  $$ |  $$ |$$ |  $$\ $$  __$$ | \____$$\ $$ |$$ |  $$ |$$ |  $$ |
$$ | \$$\ $$ |      \$$$$$$$\ $$$$$$$  |$$ |\$$$$$$$\ $$ | \$$\ \$$$$$$$ |\$$$$$$  |\$$$$$$$ |$$$$$$$  |$$ |$$ |  $$ |\$$$$$$  |
\__|  \__|\__|       \_______|$$  ____/ \__| \_______|\__|  \__| \____$$ | \______/  \_______|\_______/ \__|\__|  \__| \______/ 
                              $$ |                              $$\   $$ |                                                      
                              $$ |                              \$$$$$$  |                                                      
                              \__|                               \______/                                                       
""")

print("Vitejte!")
print(f"Na zacatek dostavate {game_bank} Kc.")

def game_choose(bank):
    print("Vyberte hru:")
    print("1 - hod minci \n2 - vrh kostkou \n3 - ruleta \n4 - hraci automat \n0 - konec")
    chosen_game = input()

    while chosen_game != "1" and chosen_game != "2" and chosen_game != "3" and chosen_game != "4" and chosen_game != "0":
        print("Neplatny vstup")
        print("Vyberte hru:")
        print("1 - hod minci \n2 - vrh kostkou \n3 - ruleta \n4 - hraci automat \n0 - konec")
        chosen_game = input()

    if chosen_game == "1":
        coin_flip(bank)
    elif chosen_game == "2":
        dice_roll(bank)
    elif chosen_game == "3":
        roulette(bank)
    elif chosen_game == "4":
        slot_machine(bank)
    elif chosen_game == "0":
        print("Dekujeme za navstevu naseho casina a tesime se, az znovu prijdete. Nashledanou!")
        pass
 
def coin_flip(bank):
    print(".: HOD MINCI :.")
    print_money(bank)
    bet = int(input("Kolik sazite? "))
    while bet > bank:
        print("Nemuzete vsadit vic penez, nez mate!")
        bet = int(input("Zadejte jinou hodnotu: "))
        
    while bet < 0:
        print("Nemuzete vsadit zapornou hodnotu!")
        bet = int(input("Zadejte jinou hodnotu: "))
    
    sides = ["orel", "panna"]
    chosen_side = input("Vyberte stranu (orel / panna): ")

    while chosen_side != "orel" and chosen_side != "panna":
        print("Neplatna hodnota")
        chosen_side = input("Vyberte stranu (orel / panna): ")
        
    print("Hazim minci:")
    print_dots(5)

    actual_side = rnd.choice(sides)
    print(actual_side)

    if chosen_side == actual_side:
        print("Vyhrali jste, gratulujeme!")
        bank += bet
    else:
        print("Prohrali jste.")
        bank -= bet

    new_bank = bank
    if_continue(coin_flip, new_bank)

def dice_roll(bank):
    print(".: VRH KOSTKOU :.")
    print_money(bank)
    bet = int(input("Kolik sazite? "))
    while bet > bank:
        print("Nemuzete vsadit vic penez, nez mate!")
        bet = int(input("Zadejte jinou hodnotu: "))
        
    while bet < 0:
        print("Nemuzete vsadit zapornou hodnotu!")
        bet = int(input("Zadejte jinou hodnotu: "))
        
    chosen_dice = int(input("Vyberte hodnotu kostky (1-6): "))

    while chosen_dice > 6 or chosen_dice < 1:
        print("Neplatna hodnota")
        chosen_dice = int(input("Vyberte hodnotu kostky (1-6): "))

    print("Hazim kostkou:")
    print_dots(5)

    actual_dice = rnd.randint(1, 6)
    print(actual_dice)

    if chosen_dice == actual_dice:
        print("Gratulace, vyhrali jste 6nasobek vsazene hodnoty!")
        bank += bet * 6
    else:
        print("Prohrali jste.")
        bank -= bet

    new_bank = bank
    if_continue(dice_roll, new_bank)

def roulette(bank):
    print(".: RULETA :.")
    print_money(bank)
    bet = int(input("Kolik sazite? "))
    while bet > bank:
        print("Nemuzete vsadit vic penez, nez mate!")
        bet = int(input("Zadejte jinou hodnotu: "))
        
    while bet < 0:
        print("Nemuzete vsadit zapornou hodnotu!")
        bet = int(input("Zadejte jinou hodnotu: "))

    print("Vyberte, na co chcete sazet:")
    print("1 - barva \n2 - velke/male cislo \n3 - sude/liche \n4 - konkretni cislo \n5 - 2 cisla")
    roulette_mode = input()

    while roulette_mode != "1" and roulette_mode != "2" and roulette_mode != "3" and roulette_mode != "4" and roulette_mode != "5":
        print("Neplatna hodnota")
        print("Vyberte, na co chcete sazet:")
        print("1 - barva \n2 - velke/male cislo \n3 - sude/liche \n4 - konkretni cislo \n5 - 2 cisla")
        roulette_mode = input()
    
    if roulette_mode == "1":
        colors = ["cervena", "cerna"]
        color = input("cervena / cerna: ")

        while color != "cervena" and color != "cerna":
            print("Neplatna hodnota")
            color = input("cervena / cerna: ")
        
        print("Hazim:")
        print_dots(5)

        actual_color = rnd.choice(colors)
        print(actual_color)

        if color == actual_color:
            print("Vyhrali jste, gratulujeme!")
            bank += bet
        else:
            print("Prohrali jste.")
            bank -= bet
            
    elif roulette_mode == "2":
        high_low = input("velke / male cislo: ")

        while high_low != "male" and high_low != "velke":
            print("Neplatna hodnota")
            high_low = input("velke / male cislo: ")
        
        print("Hazim:")
        print_dots(5)

        actual_amount = rnd.randint(1, 36)
        print(actual_amount)
        
        if high_low == "male" and actual_amount <= 18 or high_low == "velke" and actual_amount >= 19:
            print("Vyhrali jste, gratulujeme!")
            bank += bet
        else:
            print("Prohrali jste.")
            bank -= bet
            
    elif roulette_mode == "3":
        even_odd = input("sude / liche cislo: ")

        while even_odd != "sude" and even_odd != "liche":
            print("Neplatna hodnota")
            even_odd = input("sude / liche cislo: ")
        
        print("Hazim:")
        print_dots(5)

        actual_amount = rnd.randint(1, 36)
        print(actual_amount)
        
        if even_odd == "sude" and actual_amount % 2 == 0 or even_odd == "liche" and actual_amount % 2 != 0:
            print("Vyhrali jste, gratulujeme!")
            bank += bet
        else:
            print("Prohrali jste.")
            bank -= bet
            
    elif roulette_mode == "4":
        amount = int(input("1-36: "))

        while amount < 1 or amount > 36:
            print("Neplatna hodnota")
            amount = int(input("1-36: "))
        
        print("Hazim:")
        print_dots(5)

        actual_amount = rnd.randint(1, 36)
        print(actual_amount)
        
        if amount == actual_amount:
            print("Trefa! Velka gratulace, vyhrali jste 35nasobek vsazene hodnoty!")
            bank += bet * 35
        else:
            print("Prohrali jste.")
            bank -= bet

    elif roulette_mode == "5":
        amount1 = int(input("1. cislo (1-36): "))

        while amount1 < 1 or amount1 > 36:
            print("Neplatna hodnota")
            amount1 = int(input("1. cislo (1-36): "))
            
        amount2 = int(input("2. cislo (1-36): "))

        while amount2 < 1 or amount2 > 36:
            print("Neplatna hodnota")
            amount2 = int(input("2. cislo (1-36): "))
        
        print("Hazim:")
        print_dots(5)

        actual_amount = rnd.randint(1, 36)
        print(actual_amount)
        
        if amount1 == actual_amount or amount2 == actual_amount:
            print("Gratulace, vyhrali jste 17nasobek vsazene hodnoty!")
            bank += bet * 17
        else:
            print("Prohrali jste.")
            bank -= bet

    new_bank = bank
    if_continue(roulette, new_bank)

def slot_machine(bank):
    print(".: HRACI AUTOMAT :.")
    print_money(bank)
    bet = int(input("Kolik sazite? "))
    while bet > bank:
        print("Nemuzete vsadit vic penez, nez mate!")
        bet = int(input("Zadejte jinou hodnotu: "))
        
    while bet < 0:
        print("Nemuzete vsadit zapornou hodnotu!")
        bet = int(input("Zadejte jinou hodnotu: "))

    slot_1 = rnd.randint(0, 9)
    slot_2 = rnd.randint(0, 9)
    slot_3 = rnd.randint(0, 9)

    print("Tocim: ")
    time.sleep(5)
    print(slot_1, end=" ")
    time.sleep(5)
    print(slot_2, end=" ")
    time.sleep(5)
    print(slot_3)

    if slot_1 == slot_2 == slot_3 == 7:
        print("3 sedmicky! Velka gratulace, vyhrali jste 500nasobek vsazene hodnoty!")
        bank += bet * 500
    elif slot_1 == slot_2 == slot_3 != 7:
        print("Stejna cisla! Gratulace, vyhrali jste 50nasobek vsazene hodnoty!")
        bank += bet * 50
    else:
        print("Prohrali jste.")
        bank -= bet

    new_bank = bank
    if_continue(slot_machine, new_bank)

def if_continue(game, bank):
    
    if bank <= 0:
        print("Nemate uz zadne penize, vase navsteva casina konci...")
        pass
    else:
        print_money(bank)
        
        cont_ques = input("Prejete si pokracovat? (ano / ne) ")

        while cont_ques != "ano" and cont_ques != "ne":
            print("Neplatny vstup")
            cont_ques = input("Prejete si pokracovat? (ano / ne) ")

        if cont_ques == "ano":
            game(bank)
        elif cont_ques == "ne":
            game_choose(bank)


def print_money(bank):
    print(f"Mate {bank} Kc.")

def print_dots(num):
    for i in range(num):
        print(".", end = " ")
        time.sleep(1)


game_choose(game_bank)
