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




