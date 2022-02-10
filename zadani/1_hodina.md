# 1. hodina - 11. 2. 2022

# Třídy a objekty

## Referenční vs. hodnotové typy

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
