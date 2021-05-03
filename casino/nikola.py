import random as rnd
import time
global money
money = int(500)

def casino():
    print("welcome to niki's casino! you can play 'hod kostkou' or 'ruleta'.")
    print("you have $" +str(money)+ " to start with.")
    print("good luck playing!")
    while True:
        game = input("type 'kostka' for hod kostkou, 'ruleta' for roulette or 'exit' for exit. ")
        if game == "kostka":
            kostka()
        elif game == "ruleta":
            ruleta()
        elif game == "exit":
            print("bye")
            break
        else: 
            print("...")

def kostka():
    global money
    print("you chose hod kostkou! in this game a dice will be rolled and you can bet on the number it will end up on.")
    number = int(input("you can bet on a number from 1 to 6. which number do you want to bet on? "))
    if number < 1 or number > 6:
        number = int(input("choose a number between 1 and 6 please "))
    print("you chose " + str(number) + ".")
    time.sleep(0.5)
    print("you have $ " + str(money) + ".")
    bet = int(input("how much do you want to bet? "))
    betnotpossible = int(bet) > money or int(bet) < 0
    while betnotpossible:
        print("please bet a defferent amount")
        bet = input("place a new bet -> ")
    roll()
    time.sleep(1)
    if roll == number:
        print("yay you won!")
        money = money + bet
    else:
        print("better luck next time...")
        money = money - bet
    print("you currently have $ " + str(money) + ".")
    again = input("do you want to play again? yes/no ")
    if again == "yes":
        kostka()
    elif again == "no":
        leaving = input("do you want to return to the menu or exit the game? (type 'menu' or 'exit') ")
        if leaving == "menu":
            menu_2()
        elif leaving == "exit":
            print("bye! see you later!")
        else:
            print("...")
    else:
        print("...")

def ruleta():
    global money
    print("you chose roulette! in this game a roulette will be spinned and you can bet on the color and number it will end up on")
    number = int(input("first, choose your number. you can choose any number from 0 to 36 "))
    while number < 0 or number > 36:
        number = int(input("choose a number from 0 to 36 please "))
    color = input("second, choose a color: red or black? ")
    print("you chose " + str(number) + " and " + str(color) + ".")
    time.sleep(0.5)
    print("you have $ " + str(money) + ".")
    bet = int(input("how much do you want to bet? "))
    while bet < 0 or bet > money:
        print("please bet a defferent amount")
        bet = input("place a new bet -> ")
    spinning_num()
    spinning_col()
    time.sleep(1)
    if spinning_num == number and spinning_col == number:
        print("yay you won!")
        money = money + bet
    else:
        print("better luck next time...")
        money = money - bet
    print("you currently have $ " + str(money) + ".")
    again = input("do you want to play again? yes/no ")
    if again == "yes":
        ruleta()
    elif again == "no":
        leaving = input("do you want to return to the menu or exit the game? (type 'menu' or 'exit') ")
        if leaving == "menu":
            menu_2()
        elif leaving == "exit":
            return("bye")
        else:
            print("...")
    else:
        print("...")
        

def roll():
    num = rnd.randint(1,6)
    print("rolling the dice...")
    time.sleep(1)
    print("the dice ended up on")
    for i in range (3):
        time.sleep(0.5)
        print(".", end="")
    print(num)


def spinning_num():
    num = rnd.randint(0,36)
    print("spinning the roulette...")
    time.sleep(1)
    print("the number is")
    for i in range (3):
        time.sleep(0.5)
        print(".", end="")
    print(num)

def spinning_col():
    color = rnd.randint(1,2)
    if color == 1:
        color = "red"
    else:
        color = "black"
    print("and the color is")
    for i in range (5):
        time.sleep(0.5)
        print(".", end="")
    print(color)
          
def menu_2():
    print("hello!")
    print("you currently have $" +str(money)+ "")
    while True:
        game = input("type 'kostka' for hod kostkou, 'ruleta' for roulette or 'exit' for exit. ")
        print("good luck playing!")
        if game == "kostka":
            kostka()
        elif game == "ruleta":
            ruleta()
        elif game == "exit":
            print("bye")
            break
        else: 
            print("...")
def exit():
    print("bye! see you later")

casino()
    

    
                     


        





    
            
        


    
        
        
    
        



