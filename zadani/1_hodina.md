# 1. hodina - 11. 2. 2022

## Třídy a objekty

### Referenční vs. hodnotové typy

Jaká bude hodnota proměnné x po zavolání funkce?
``` python
def plus_two(number):
  number = number + 2
  
x = 5
plus_two(x)
print(x)
```

Jak bude vypadat pole po zavolání funkce?
``` python
def append_two(array):
  array.append(2)
  
x = [1, 2, 3, 4]
append_two(x)
print(x)
```

- mezi hodnotové typy patří všechny typy, které mají jednu konkrétní hodnotu:
  - čísla (int, float)
  - boolean (True, False)
  - (řetezce - string)

- referenční typy - "velké" typy, které se nevyplatí kopírovat:
  - pole
  - slovníky - dictionary
  - objekty

### Strukturování kódu
- metody, které používáme ke strukturování kódu:
  1) větvení, cykly - if, while, for
  2) funkce - ucelené funkcionality uzavřené do balíčků, které můžeme volat z různých míst
  3) objekty - balíčky dat, které spolu souvisí

### Příklad

- chci si uchovávat data o svých studentech
- ke každému několik informací:
  - jméno
  - příjmení
  - ročník
  - počet bodů z DÚ

- jak to udělat s tím, co zatím umíme - proměnné:
```python

jmeno1 = "Matej"
prijmeni1 = "Tlapak"
rocnik1 = 6
body1 = 28

jmeno2 = "Lucie"
prijmeni2 = "Hockova"
rocnik2 = 6
body2 = 30

# atd. pro všechny studenty
```
- nepraktické - hodně proměnných, nemůžu procházet studenty v cyklu

- varianta 2 - pole:
```python
studenti = ["Matej", "Tlapak", 6, 28, "Lucie", "Hockova", 6, 30]
```

- lepší - můžu procházet v cyklu
- ale pořád nepraktické
  - v poli není daná hranice mezi studenty
  - když budu chtít přidat další vlastnost - musím přepsat všechen kód, který pole studentů používá

- nejlepší řešení - objekty



