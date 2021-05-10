"""
# funkce - volani
# navrat
def funkce(): # mam funkci - funkce - na radku 3
    print("Ahoj")
    # skoc na radek navrat


print("Zacatek")
funkce() # navrat = 9
# skoc na radek 3
print("Konec")


print("Zacatek2")
funkce() # navrat = 15
# skoc na radek 3
print("Konec2")


# navrat
def funkce2():
    print(5)

def funkce1():
    funkce2() # navrat = 25 # skoc na 21
    print(7)


funkce1() # navrat = 29 # skoc na 24 - kde je definovana funkce1
print(13)

# volaci zasobnik - call stack
"""
"""
# casino
import random

def menu(bank):
    print("Vyber hru")
    print("input")
    game = "kostky"
    play_game(game, bank)
    if game == end:
        exit()


def play_game(game, bank): 
    # if game == "kostky"
    print("hra")
    r = random.randint(1, 6)
    bank += 1
    menu(bank)

print("Welcome")
menu(500)
"""

# rekurze

# ze venitr funkce volam tu stejnou funkci

def funkce():
    funkce()


def rekurze(n):
    if n <= 0:
        return n
    x = rekurze(n - 1)
    return x

x = rekurze(3)
print(x)

# velky problem - umim rozlozit na mensi problemy
# ty uz je jednoduche vyresit


# factorial
# 1! = 1
# 2! = 1 * 2 = 2
# 3! = 1 * 2 * 3 = 6

# 5! = 1 * 2 * 3 * 4 * 5 = 120
# n! = 1 * 2 * ... * (n-1) * n


def factorial(n):
    result = 1
    f = 1
    while f <= n:
        result = result * f
        f += 1
    return result

print(factorial(5))




































