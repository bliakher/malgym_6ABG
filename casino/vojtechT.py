import time as t
import random as r
def odpocitavani(a):
    sekunda=a+1
    for i in range(a):
        sekunda-=1
        t.sleep(1)
        print(sekunda, end=" ")
    print( '\n')
def sazka(penize):
    vsazeni=int(input("Vsadte castku : "))
    while vsazeni > penize :
        print("Nejde sazet vic nez mate")
        vsazeni=int(input("Vsadte castku : "))
    while vsazeni < 0:
        print("Nejde sazet zaporne castky")
        vsazeni=int(input("Vsadte castku : "))
    return vsazeni
def soucet_hrac(pocet):
    soucet=0
    for i in pocet:
        if i == "Q" or i=="K" or i =="J":
            i=10
        elif i == "A":
            i = int(input("Chcete A pocitat jako 1/11? "))
        soucet+=int(i)
    return soucet
def soucet_pocitac(pocet):
    soucet=0
    a=0
    b=-1
    for i in pocet:
        if i == "Q" or i=="K" or i =="J":
            i=10
        if i=="A":
            i=0
        soucet+=int(i)
    if "A" in pocet:
        for i in range(pocet.count("A")):
            soucet+=11
        if pocet == ["A", "A"]:
            pass
        else:
            while soucet>21:
                if a != pocet.count("A"):
                    a+=1
                    soucet-=10
                elif a == b :
                    break
                b=a
                
    return soucet
def rozdavani(hrac, hrac_pocet, pocitac):
    a=["♠", "♥", "♣", "♦"]
    b=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    for i in range(2):
        hodnota=str(r.choice(b))
        karta=str(hodnota)+str(r.choice(a))
        while karta in hrac or karta in pocitac:
            hodnota=str(r.choice(b))
            karta=str(hodnota)+str(r.choice(a))
        hrac.append(karta)
        hrac_pocet.append(hodnota)
    return hrac, hrac_pocet
def dobirani(hrac, pocet, pocitac):
    a=["♠", "♥", "♣", "♦"]
    b=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    hodnota=str(r.choice(b))
    karta=hodnota+str(r.choice(a))
    while karta in hrac or karta in pocitac:
        hodnota=str(r.choice(b))
        karta=hodnota+str(r.choice(a))
    hrac.append(karta)
    pocet.append(hodnota)
    return hrac, pocet
def blackjack(penize):
    print("Prubeh hry: Dostanete 2 karty a muzete se rozhodnout dobrat dalsi. Musite mit soucet karet bliz ke 21 nez pocitac, ale nesmite presahnout 21. Vyjimka je, kdyz mate 2x A. J, Q, K se pocitaji za 10, A se pocita podle vyberu za 1/11. Pokud prohrajete, prijdete o vsazeni, pokud vyhrajete, dostanete vsazeni.")
    while True:
        a=["♠", "♥", "♣", "♦"]
        b=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        hrac=[]
        hrac_pocet=[]
        pocitac=[]
        pocitac_pocet=[]
        rozdavani(hrac, hrac_pocet, pocitac)
        vsazeni=sazka(penize)
        print("Vase karty : "+str(hrac))
        while soucet_pocitac(hrac_pocet)<22 :
            if input("Chcete dalsi kartu? [ano,ne] ")=="ne":
                break
            dobirani(hrac, hrac_pocet, pocitac)
            print("Vase karty : "+str(hrac))
        hrac_soucet=soucet_hrac(hrac_pocet)
        rozdavani(pocitac, pocitac_pocet, hrac)
        print("Karty pocitace : "+str(pocitac))
        pocitac_soucet=soucet_pocitac(pocitac_pocet)
        while pocitac_soucet < 17:
            print("Pocitac dobira karty")
            odpocitavani(3)
            dobirani(pocitac, pocitac_pocet, hrac)
            pocitac_soucet=soucet_pocitac(pocitac_pocet)
            print("Karty pocitace : "+str(pocitac))
        print("Vase karty : "+str(hrac))
        print("Soucet pocitace : "+str(pocitac_soucet))
        print("Vas soucet : "+str(hrac_soucet))
        while True:
            if (hrac_soucet<22 and hrac_soucet==pocitac_soucet) or (hrac_pocet==["A", "A"] and hrac_soucet==22 and pocitac_pocet==["A", "A"]):
                print("Remiza")
                break
            elif ( hrac_soucet>21 and hrac_pocet != ["A", "A"]) or (hrac_soucet<22 and pocitac_soucet<22 and hrac_soucet<pocitac_soucet) or pocitac_pocet==["A", "A"]:
                 print("Prohra")
                 penize-=vsazeni
                 break
            elif (pocitac_soucet>21) or (pocitac_soucet<22 and hrac_soucet<22 and pocitac_soucet<hrac_soucet) or (hrac_pocet==["A", "A"] and hrac_soucet==22) :
                print("Vyhra")
                penize+=vsazeni
                break
        psani(penize)
        if input("Chcete hrat dal?[ano,ne] ")=="ne":
            break
def casino():
    print("Vítejte")
    penize=100
    print("Dostáváte : "+str(penize))
    while True:
        hra=str(input("Vyberte hru [skorapky/blackjack/konec] : "))
        if hra == "blackjack" :
            penize=blackjack(penize)
        elif hra == "skorapky":
            penize=skorapky(penize)
        else:
            print("Na shledanou")
            break
def skorapky(penize):
    d=0
    print("Prubeh hry : Vsadite castku na skorapku, pokud se trefite, vyhrajete 2x vsazeni, pokud ne, vsazeni prohrajete")
    while d != "ne":
        a=str(r.randint(1,3))
        b=str(input("Vsadte na skorapku :[1,2,3] : "))
        c=sazka(penize)
        print("Míchání")
        odpocitavani(5)
        if b==a:
            print("Vyhra")
            penize+=2*c
        else :
            print("Prohra")
            penize-=c
        print("Skorapka : "+str(a))
        psani(penize)
        d=input("Chcete pokracovat ve hre? [ano/ne] : ")
    return penize
def psani(penize):
    print("Vase penize : "+str(penize))
casino()

