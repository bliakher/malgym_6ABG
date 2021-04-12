import math

"""
def mojefunkce(param1, param2):
    a = param1 + param2
    return a

# v nazvech nemuzou byt mezery

mojefunkce(3, 5)

# return - navratova hodnota

vysledek = mojefunkce(4, 2)
print(vysledek)
vys2 = mojefunkce(vysledek, 3)

jmeno = input("Jmeno")

def bez_navratu(p1, p2):
    a = p1 + p 332
    print(a)

bez_navratu(4, 2)
"""
"""
# globalni x lokalni promenna

x = 5 # globalni

def fce():
    l = 0 # lokalni
    # vidime ji jen zevnitr funkce fce
    l += 1
    print("l:", l)
    # vidim vsechny globalni promenne
    print("x:", x)
    # ale nemuzu prepisovat jejich hodnotu
    # x = 6, x += 1
    
    
def fce2():
    x = 7  # definice lokalniho x
    print("x:", x)

def fce3():
    global x # reknu ze se jedna o globalni a ne lokalni
    print("fce3 x ", x)
    x = 6 # ted se priradi do globalniho x
    print("x:", x)

# print(l) error - nevidime dovnitr funkce

fce()
print("x:", x)
fce2()
fce3()


def a():
    p = 8 # lokalni

def b():
    global p # definuje novou globalni p
    # print(p) - error - v p neni zadna hodnota - nemuzeme cist
    p = 1
    print(p)
    

b()
print("p", p) # p def uvnitr fce, ale jako globalni

"""
"""

def main():
    print("menu")
    global money
    money = 500
    print(money)

def coin():
    # sazka, hod minci
    # vyhra / prohra -> upravit mnozstvi penez
    global money
    money += 10


def rozsireni1():
    global money
    money = 1000000 # bank casina
    #.....

def rozsireni2():
    money -= 100 # upravuju bank banky
    
"""   

# globalni promenne jsou osklive!

# zasada - hlidat si data -
# aby do promenne slo zapsat jen tam, kde si ji definujeme

# jak to delat bez globalnich?
# chceme - vsechny promenne jenom uvnitr funkci

"""
def main():
    money = 500
    print(money)
    print("menu")
    money = coin(money)
    print(money)
    money = dice(money)
    

def coin(money):
    # sazka, hod minci
    # vyhra / prohra -> upravit mnozstvi penez
    money += 10
    return money

def dice(money)
    money -= 50
    return money

main()


# funkce muze vracet vic veci

def fce_vraci_2():
    a = 8
    b = 7
    return a, b

a, b = fce_vraci2()

"""

# funkce, ktera pocita objem koule
# nacte od uzivatele polomer
# spocita objem koule
# vypise vysledek
# objem = 4/3 pi r^3
# math.pi 

print(math.pi)

def sphere_volume():
    r = int(input("R= "))
    volume = 4/3 * math.pi * r * r * r
    print(volume)

sphere_volume()

# funkcni dekompozice

# 1. kdyz se mi opakuje kod

# 2. oddeleni vstupu a vystupu od vypoctu


def sphere_volume(r):
    volume = 4/3 * math.pi * r * r * r
    return volume

def sphere_volume_interactive():
    R = int(input("R= "))
    volume = sphere_volume(R)
    print(volume)






















    











