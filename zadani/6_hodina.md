# 6. a 7.hodina - 15. 10. 2021, 22. 10. 2021

### Zanoření

Zkuste krokovat následující kód s breakpointem nastaveným na řádku s voláním funkce. 
Jaký je rozdíl, pokud budu krokovat s přeskočením (F10) nebo s vnořením (F11)?

``` python
def cyklus(pole):
  for prvek in pole:
    print(prvek)
    
cyklus([1, 2, 3, 4]) # breakpoint tady

```

### Podřetězce ve slově

``` python
def count_letter2(word, substring): 
  a = 0 
  b = 2 
  substring_count = 0 
  while b<=len(word): 
    A = word[a:b] 
    if A == substring: 
      substring_count += 1 
    a += 1 
    b += 1 
  return substring_count 

print(count_letter2("bbbb", "bbb")) 

```

V programu je chyba, kterou jsme na minulé hodině hledali. 
Zkuste si teď program krokovat ne VS, podívat se, co se děje s důležitými proměnnými a připomenout si, kde je chyba.

### Uvnitř cyklu

Program by měl sečíst všechna čísla od 1 do 10. Někde je ale chyba. Zkuste krokovat.

``` python
i = 0
while i < 10:
    soucet = 0
    i += 1
    soucet += i

print(soucet)
```

### Nekonečné násobky

Program měl načíst číslo od uživatele a vypsat první až desátý násobek toho čísla.
Tedy pro číslo 5 vypsat : 5, 10, 15, ..., 45, 50.
Zkuste si spustit a podívat se, co to dělá. (Běžící program zastavíte zmáčknutím Ctrl+C )
Najděte chybu a opravte.

``` python
cislo = int(input("Cislo na nasobky: "))

nasobek = 1

while cislo < 10*cislo:
    print(cislo * nasobek)
    nasobek += 1
```

### Globalizace
V tomhle programu se nám zamíchali proměné mezi funkcemi. To, co se vypíše, není ani 256 děleno 8 ani faktoriál 5.
Krokujte s vnořením a opravte.

``` python
vysledek = 1

def faktorial(x):
    global vysledek
    for i in range(1, x + 1):
        vysledek *= i
    print("Faktorial", x, "je", vysledek)

def vypis_vysledek():
    print("Tady je vysledek:")
    print(vysledek)
    

vysledek = 256 // 8
faktorial(5)
vypis_vysledek()
```

### Moje chyba

Zkus vymyslet krátký program, ve kterém je nějaká chyba.
Odevzdej do připraveného zadání v Teams.
Tvůj program pak zveřejním na gitu a ostatní se budou snažit chybu odhalit.

#### Gio
``` python
# Vypise nasobky cisla (1. az 10. nasobek)
def vypsani_nasobku(nasobek, cislo):
    while nasobek <= 10:
        cislo = cislo * nasobek
        nasobek += 1
   
vypsani_nasobku(1, 5)
```
#### Ondra
``` python
def ds (fe ,ba=[] ):
    """
    program ma vzit 'fe' a (pripadne) 'ba'
    pridat prvky obraceneho pole 'fe' do 'ba'
    vratit druhou pulku ba pripojenou na zacatek prvni pulky 'ba'
    """
    gd =len
    ba.extend (reversed(fe ))
    return(ba[gd   (ba) //2:])+ba[: gd(ba) //2]

# ls = [i for i in range(10)]
# print(ds(ls))
# print(ds(ls, [-1,-2,-3]))
# print(ds(ls))
# print(ds(ls))
```
#### Viktor
``` python
"program vypíše počet dvojic stejných čísel v A a B" 

A = [5, 17, 10, 5, 5, 1, 2, 7] 
B = [1, 5, 17, 17, 2, 10, 10] 
couples = 0 
A.sort() 
B.sort() 
while len(A) != 0 and len(B) !=0: 
    if A[0] == B[0]: 
        couples = couples + 1 
        A.pop(0) 
        B.pop(0) 
    if len(A) != 0 and len(B) !=0 and A[0] > B[0]: 
        A.pop(0) 
    if len(A) != 0 and len(B) !=0 and A[0] < B[0]: 
        B.pop(0) 

print(couples)   
```
#### Lucka
``` python
#program ma vypocitat mocninu (cislo umocnene na moc)

def mocnina(x, n):
    vysledek = 1
    for i in range(n):
        vysledek = x*x
    return vysledek

cislo = int(input("cislo: "))
moc = int(input("mocnina: "))
print(mocnina(cislo, moc))
```
#### Julča S.
``` python
# pocet pismen ve slove

pocet_pismen = 0
slovo = input("vlozte slovo: ")
for i in slovo:
    pocet_pismen =+ 1

print(f"Pocet pismen je {pocet_pismen}")
```
#### Max
``` python
###Code checks if a user's password contains a number

password = input("Type password:")
def password_checker(password):
  HasNum = False
  for i in password:
    if i.isdigit():
      HasNum = True


number_check = password_checker(password)

if number_check == True:
  print("password contains a number")
else:
  print("password does not contain a number")
```
#### Michal
``` python
#Vypisuje Fibonacciho posloupnost do cisla limit.

def fibonacci(prvni, druhe, limit):
    print(prvni)
    print(druhe)
    while druhe < limit:
        soucet = prvni + druhe
        print(soucet)
        druhe = soucet
        prvni = druhe

fibonacci(1, 2, 500)
```
#### Filip
``` python
def rekurzefaktorial(num):
    factorial_num = 0
    if num>=0:
        factorial_num = num * rekurzefaktorial(num-1)
        
    return factorial_num
print(rekurzefaktorial(4))
```
#### Matěj
``` python

#program ma brat cisla a rikat jestli jsou delitelna dvema a trema

while True:
    x = int(input("napis sem cislo: "))
    if x % 2 = 0 and x % 3 = 0:
        print(x,"je delitelne dvema i trema")
    elif x % 2 = 0 and x % 3 != 0:
        print(x,"je delitelne dvema ale trema ne")
    elif x % 2 != 0 and x % 3 = 0:
        print(x,"je delitelne trema ale dvema ne")
    else:
        print(x,"neni delitelne ani dvema ani trema")
```
#### Kryštof
``` python
koruny = 0
eura = int(input("zadej počet euro: "))
def prevod(eura):
    koruny = eura * 25,63 
    print(koruny, "czk")
prevod(eura)

"místo desetinné čárky v kurzu eura je normální čárka"
```
#### Teo
``` python
def obratit(pole):
    druhepole = []
    for i in range(len(pole), 0, -1):
        druhepole.append(i)
    return druhepole

print(obratit([1, 2, 3, 4, 3]))
#program ma obratit pole
```
