#zakomentované části jsou věci z minule


"""
 v|sčimport random as rnd
barvy = ["černá","bílá"]

def colors(black,white):
    my_color = input("jakou barvu vybíráte? černá/bílá")
    bet = input("Kolik sázíte?")
    if a<=bet:
        print("nemáte dostatek kreditu")
    else:
        print(barvy)
        
        
    


    
import random as rnd
num = rnd.randint(1,100)

import time
time.sleep(2)

while True:
    answer = input("Vyberte hru : [sázka na barvu/ruleta] or [end]")
    if answer == "sázka na barvu":
        colors("black","white")
    else:
        break
"""
print("Dobrý den, vítáme vás v Juliině Casině!")
a= 500
print("začáteční kredit: $", a)

def nabidka():
    vybrana =input(" Vyberte hru (kostky/ruletta/hádání čísla) nebo (ukončit hru): ")
    print(f" vybrali jste si {vybrana}")
    game_choosing(vybrana)

   
def game_choosing(vybrana):
    if vybrana == "kostky":
        hod_kostkou()
    elif vybrana== "ruletta":
        karta()
       # print("Omlouváme se, ale momentálně je hra mimo provoz")
        #nabidka()
    elif vybrana== "hádání čísla" or vybrana== "hadani čisla" :
        hadaní_čisla()
        
    elif vybrana == "ukončit hru":
        print("Děkujeme, brzy nashledanou")
        
    else:
        print("Omlouváme se, ale někde je chyba. ZKuste to jěště jednou prosím")
        nabidka()

def limit():
    while True:
        sazka = int(input("Kolik sázíte?"))
        if sazka >= a:
            print("Omlouváme se, ale nemáte dostatek peněz na účtu pro sázku.")
        
        else:
            print("Vaše sázka byla přijata...Můžeme začít!")
            break
    return sazka


import time

def waiting():
    for i in range(5):
        time.sleep(0.5)
        print(".", end="")

def hexagon():
    while True:
        maximum = 7
        moje_číslo = int(input("Na jaké číslo sázíte 1-6?"))
        if moje_číslo >= maximum or moje_číslo <=0:
            print("Musíte si vsadit na číslo na kostce...1-6")
        else:
            return
            print("Vaše číslo bylo scháleno.")
            break
    return moje_číslo

def hod_kostkou():
    global a
    import random as rnd
    moje_číslo = hexagon()
    sazka = limit()
    print("Počkejte chvíli, kostky se míchají")
    waiting()
    num = rnd.randint(1,6)
    int(a)
    if moje_číslo == num:
        print("Gratujuleme!!! vyhráli jste")
        a += sazka
    else:
        print("Těsně!!! Omlouváme se, ale vaše číslo se neshoduje...")
        a -= sazka
    print("váš momentální kredit je:", a)
    nabidka()

def karta():
    moje_karta = input("Chcete si vsadit na barvu nebo číslo?")
    print(f"Vybrali jste {moje_karta}")
    výber(moje_karta)
    
def padla_barva():
    moje_barva = str(input("Na jakou barvu sázíte: černá/červená ?"))
    global a
    import random as rnd
    sazka = limit()
    print("Počkejte chvili, ruletta se točí")
    waiting()
    barvy = ["černá","červená"]
    color = rnd.choice(barvy)
    int(a)
    if moje_barva == color:
        print("Gratujuleme!!! vyhráli jste")
        a += sazka
    else:
        print("Těsně!!! Omlouváme se, ale vaše barva se neshoduje...")
        a -= sazka
    print("Váš momentální kredit je:", a)
    nabidka()
        
def padle_číslo():
    moje_number = int(input("Na jaké číslo sázíte od 0-36?"))
    global a
    import random as rnd
    sazka = limit()
    print("Počkejte chvili, ruletta se točí")
    waiting()
    num = rnd.randint(0,36)
    int(a)
    if moje_number == num:
        print("Gratujuleme!!! vyhráli jste")
        a += sazka
    else:
        print("Těsně!!! Omlouváme se, ale vaše barva se neshoduje...")
        a -= sazka
    print("Váš momentální kredit je:", a)
    nabidka()
    
    
def výber(moje_karta):    
    if moje_karta == "barva" or moje_karta == "barvu":
        padla_barva()
    elif moje_karta == "číslo":
        padle_číslo()
    else:
        print("Vaše odpověď neodpovídá výběru. Zkuste to znovu")
        nabidka()
    

def hadaní_čisla():
    global a
    print("Bude vylosováno jedno číslo od 1-20. Váš úkol bude ho uhodnout. V této hře sázite na maximálních počet vašich tipů. Na začátku zvolíte první orientační číslo, které nebude započítáváno do vašich pokusů.   Pokud je vše jasné můžeme začít.")
    počet_tipů = int(input("Kolik si myslíte, že budete potřebovat maximálně možností hádání?( počet tipů)"))
    print(f"Sázíte že budete potřebovat {počet_tipů} pokusů na uhodnutí losovaného čísla.")
    sazka = limit()
    import random as rnd
    vylosovane_čislo = rnd.randint(1,20)
    b=0
    
    while True:
        vas_tip = int(input("Jaké číslo si myslíte, že je vylosované?"))
        if vas_tip ==vylosovane_čislo:
            print("Gratulejeme!!! trefili jste vylosované číslo.")
            a += sazka
            print("Váš momentální kredit je:", a)
            nabidka()
        elif b==počet_tipů:
            print("Omlouváme se, ale vyčerpali jste všechny vámi zvolený pokusy na uhodnutí čísla.Tuto hru jste prohráli.")
            a -= sazka
            print("Váš momentální kredit je:", a)
            nabidka()
        
        elif vas_tip > 21:
            print("Vybrali jste číslo, které není mezi losujícími. Musíte zvolit od 1-20. zkuste to znovu")
            b+=1
        elif vas_tip > vylosovane_čislo:
            print("Vaše číslo je větší než losované číslo. zkuste to znovu")
            b+=1
        elif vas_tip < vylosovane_čislo:
            print("Vaše číslo je menší než losované číslo. Zkuste to znovu")
            b+=1
       
        
      
    



nabidka()

"""    
    

def hadaní_čisla():
    print("Bude vylosováno jedno číslo od 1-20. Váš úkol bude ho uhodnout. V této hře sázite na počet maximálních vašich tipů. POkud je vše jasné můžeme začít.")
    počet_tipů = int(input("Kolik si myslíte, že budete potřebovat maximálně možností hádání?( počet tipů)"))
    print("Sázíte že budete potřebovat {počet_tipů} pokusů na uhodnutí losovaného čísla.")
    sazka = limit()
    import random as rnd
    vylosovane_čislo = rnd.randint(1,20)
    vas_tip = int(input("Jaké číslo si myslíte, že je vylosované?"))
    b=0
    while b != počet_tipů:
        if vas_tip ==vylosovane_čislo:
            print("Gratulejeme!!! trefili jste vylosované číslo.")
           
        elif vas_tip >= vylosovane_čislo:
            print("vaše číslo je větší než losované číslo. zkuste to znovu")
          
        elif vas_tip <= vylosovane_čislo:
            print("vaše číslo je menší než losované číslo. Zkuste to znovu")
          
        elif vas_tip >= 21:
            print("vybrali jste číslo, které není mezi losujícími. Musíte zvolit od 1-20")
        počet_tipů -=1    
        
    
elif b==c:
            elif vas_tip > 21:
                print("vybrali jste číslo, které není mezi losujícími. Musíte zvolit od 1-20. A protože to byl váš poslední pokus. Omlouváme se, ale tuto hru jste prohráli. ")
                a -= sazka
                print("váš momentální kredit je:", a)
                nabídka()
            elif vas_tip > vylosovane_čislo:
                print("vaše číslo je větší než losované číslo.  A protože to byl váš poslední pokus. Omlouváme se, ale tuto hru jste prohráli.")
                a -= sazka
                print("váš momentální kredit je:", a)
                nabídka()
            elif vas_tip < vylosovane_čislo:
                print("vaše číslo je menší než losované číslo.  A protože to byl váš poslední pokus. Omlouváme se, ale tuto hru jste prohráli.")
                a -= sazka
                print("váš momentální kredit je:", a)
                nabídka()
hadaní_čisla()
"""
    







        
