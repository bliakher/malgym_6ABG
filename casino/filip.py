from random import randint
from time import sleep


def casino():
    peníze = 500
    print("Vítejte v Casino Filip!!! Vaše peníze: ", peníze, " $")
    while True:
        if peníze == 0:
            print("Nemáš ani vindru, přijď až budeš mít prachy!")
            break
        hra = input("Zvolte si hru - napište kostky pro kostky, blackjack pro blackjack, exit pro odchod.")
        if hra == "kostky":
            peníze = kostky(peníze)
        elif hra == "blackjack":
            peníze = blackjack(peníze) 
        else:
            print("Nashledanou příště!")
            break
        print("Zůstatek na účtě:", peníze, " $")  

def kostky(peníze):
    sázka = input("Zvolte výši sázky.")
    sázka = int(sázka)
    if sázka > peníze:
        print("Nemáte dostatek peněz.")
    else:
        print("Hází se kostky")
        for i in range(5):
            sleep(1)
            print(".")
        hod_hráč = randint(1, 6)
        hod_casino = randint(1, 6)
        hod_casino = hod_casino + 1
        if hod_casino > 6:
            hod_casino = 6
        print("Váš hod:", hod_hráč)
        print("Hod casina:", hod_casino)
        if hod_hráč > hod_casino:
            print("Máte to ale štěstí!")
            peníze = peníze + sázka
        elif hod_hráč == hod_casino:
            print("Remíza!")
        else:
            print("Smůla smůlovatá!")
            peníze = peníze - sázka
    return peníze

def blackjack(peníze):
    sázka = input("Zvolte výši sázky.")
    sázka = int(sázka)
    if sázka > peníze:
        print("Nemáte dostatek peněz.")
    else:
        print("Rozdávají se Vám karty.")
        for i in range(3):
            sleep(1)
            print(".")
        karta_1_hráč = randint (2, 11)
        print("1. karta je:", karta_1_hráč) 
        karta_2_hráč = randint (2, 11)
        print("2. karta je:", karta_2_hráč)
        karty_hráče = karta_1_hráč + karta_2_hráč
        print("Vaše hodnota karet je:", karty_hráče)
        karty_hráče = přidání_karty_f(karty_hráče)
        print("Rozdávají se karty krupiérovi.")
        for i in range(3):
            sleep(1)
            print(".")
        karta_1_krupiér = randint (2, 11)
        karta_2_krupiér = randint (2, 11)
        karty_krupiéra = karta_1_krupiér + karta_2_krupiér
        while karty_krupiéra < 17:
            karty_krupiéra = přidání_karty_f_k(karty_krupiéra)
        print(karty_krupiéra)
        if karty_hráče > 21:
            peníze = peníze - sázka
            print("Překročil jste limit.")
            return peníze
        if karty_krupiéra > 21:
            peníze = peníze + sázka
            print("Krupiér překročil limit.")
            return peníze
        else:
            if karty_hráče > karty_krupiéra:
                peníze = peníze + sázka
                print("Máte to ale štěstí! Máte lepší karty.")
            elif karty_hráče < karty_krupiéra:
                peníze = peníze - sázka
                print("Smůla smůlovatá! Krupiér má lepší karty.")
            else:
                print("Remíza!")
        return peníze
        
        
        

def přidání_karty_f(karty_hráče):
    while True:
        přidání_karty = input("Chcete přidat kartu? [y/n]")
        if přidání_karty == "y":
            přidaná_karta = randint (2, 11)
            karty_hráče = karty_hráče + přidaná_karta
            print("Vaše hodnota karet je:", karty_hráče)
            if karty_hráče > 21:
                return karty_hráče
        else:
            return karty_hráče
    
def přidání_karty_f_k(karty_krupiéra):
    přidaná_karta = randint (2, 11)
    karty_krupiéra = karty_krupiéra + přidaná_karta
    return karty_krupiéra

casino()




    
            








