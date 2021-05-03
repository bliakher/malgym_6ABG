import random
import time
pocet_penez = 1000


def hod_minci():
    global pocet_penez
    print("Vitejte v hodu minci!\nTady si vsadite, jestli padne [panna] nebo [orel].")
    print(f"Kdyz se trefite, vyhrajete vsazenou hodnotu, kdyz prohrajete, ztratite vsazenou castku.\nMate {pocet_penez} Kc!")
    while True:
        vsazene_penize = int(input("Kolik vsazite Kc? "))
        if vsazene_penize <= pocet_penez:
            pocet_penez = pocet_penez - vsazene_penize
            vsazim_na = input("[panna] nebo [orel]? ")
            mince = ["panna", "orel"]
            nahodny_hod = random.choice(mince)
            for i in range(3):
                print("*")
                time.sleep(1)

            if vsazim_na == nahodny_hod:
                print("Vyhravate! Mince dopadla na " + nahodny_hod)
                pocet_penez = pocet_penez + (vsazene_penize * 2)
            else:
                print("Prohravate! Mince dopadla na " + nahodny_hod)
            break
        else:
            print("Nemuzete vsadit vice, nez mate.")
    for i in range(3):
        print("*")
        time.sleep(1)

    vyber_co_dal = input("Chcete se vratit do menu [menu]/pokracovat ve hre [pokracovat]? ")
    if vyber_co_dal == "menu":
        uvitaci_menu()
    elif vyber_co_dal == "pokracovat":
        hod_minci()


def uhodni_cislo():
    global pocet_penez
    print("Vitejte v hadani cisla!\nPocitac vybere nahodne cislo od 1 do 20. Vy si tipnete, na kolik "
          "pokusu dane cislo uhodnete a vsadite libovolny pocet penez.\nPocitac vam po kazdem tipu rekne, zda je nahodne cislo vyssi/nizsi nez vas tip.\nKdyz se trefite, vyhrajete dvojnasobek"
          " vsazenych penez, kdyz se netrefite, prohravate vsazenou castku.")
    while True:
        vsazene_penize2 = int(input("Kolik sazite Kc? "))
        if vsazene_penize2 <= pocet_penez:
            pocet_penez = pocet_penez - vsazene_penize2
            vsazim_na_pocet_pokusu = int(input("Kolik pokusu budete potrebovat? "))
            list_nahodne_cislo1 = list(range(1, 20))
            nahodne_cislo = random.choice(list_nahodne_cislo1)
            pokusy = 0
            hracovo_hadane_cislo = 0

            while hracovo_hadane_cislo != nahodne_cislo:
                hracovo_hadane_cislo = int(input("Jake je hadane cislo? "))
                if hracovo_hadane_cislo > nahodne_cislo:
                    print("Nahodne cislo je nizsi nez tento tip.")
                elif hracovo_hadane_cislo < nahodne_cislo:
                    print("Nahodne cislo je vyssi nez tento tip.")
                pokusy = pokusy + 1

            print(f"Uhodli jste, nahodne cislo bylo {nahodne_cislo}!")
            for i in range(3):
                print("*")
                time.sleep(1)
            if pokusy == vsazim_na_pocet_pokusu:
                pocet_penez = pocet_penez + (vsazene_penize2 * 2)
                print("Trefili jste se poctem pokusu! Vyhravate.")
            else:
                print("Bohuzel jste se odhadem poctu pokusu netrefili. Muzete to zkusit znovu!")
            break
        else:
            print("Nemuzete vsadit vice, nez mate.")

    vyber_co_dal = input("Chcete se vratit do menu [menu]/pokracovat ve hre [pokracovat]? ")
    if vyber_co_dal == "menu":
        uvitaci_menu()
    elif vyber_co_dal == "pokracovat":
        uhodni_cislo()


def uvitaci_menu():
    vyber_hry = input(f"Vitejte v menu!\nMate {pocet_penez} Kc!\nVyberte si hru! [hod minci] nebo [uhodni cislo]. ")
    if vyber_hry == "hod minci":
        hod_minci()
    else:
        uhodni_cislo()


vyber_hry = input("Vitame Vas v Kasinu U Senatu!\nJako prvni dostavate 1000 Kc.\nVyberte si hru! [hod minci] nebo ["
      "uhodni cislo]? ")
if vyber_hry == "hod minci":
    hod_minci()
else:
    uhodni_cislo()




