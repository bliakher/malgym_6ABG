# 2. hodina - 18. 2. 2022

## Třídy a objekty 

### Opakování pojmů

- **třída**
```python
class ClassName:
  pass
```

- **objekt**
```python
object = ClassName()
```
- **datová položka / atribut / vlastnost**
```python
class ClassName:
  data1 = 1
  data2 = 2
  
class MathConsts:
  pi = 3.141592
  e = 2.718281
  sqrt2 = 1.414213
  
constants = MathConsts()
print("pi is", constants.pi)
print("e is", constants.e)
print("Square root of 2 is", constants.sqrt2)
```
- všechny objekty třídy `MathConsts` budou mít stejné hodnoty datových položek
- **statická data** - stejná pro všechny objekty typu
- hodí se mít i nestatická data - data, která se pro každý objekt můžou lišit

- **konstruktor** - naplní nestatické položky daty
```python
class Clovek:
  klasifikace = "Homo Sapiens" # staticka data, spolecna pro vsechny lidi
  
  def __init__(self, jmeno, vek):
    self.jmeno = jmeno
    self.vek = vek

anna = Clovek("Anna", 25)
petr = Clovek("Petr", 20)
```
- Anna a Petr mají odlišná jména a věk, ale mají stejnou klasifikaci
- použitím `self` říkáme, že `jmeno` a `vek` se mají zapamatovat pro každý objekt zvlášť - patří dannému objektu

### Úkol 1
*Zkopírujte si definici třídy `Clovek`. Napište funkci s předpisem `vypis_info(clovek)`, která bere jako parametr objekt člověka a vypíše informace o něm (jak se jmenuje a kolik je mu let).*

### Úkol 2
*Napište další funkci `je_dospely(clovek)`, která bere objekt člověka jako parametr a vrátí `True` nebo `False` podle toho, jestli je člověk starší 18 let.*

- teď obě funkce přepíšeme na **metody** třídy `Clovek`

### Úkol 3
1) *Vytvořte vlastní třídu příšery nebo bojovníka, který bude mít vlastnosti: sílu útoku - jak dobře umí útočit, a počet životů (může mít i další - jméno, barvu, zbraň atd.)*
2) *Přidejte metodu `bojuj(self, utocnik)`, která porovná sílu útoku bojujících - zvítězí ten, kdo má větší. Poražený ztratí jeden život, pokud mu už nezůstanou životy, umírá. Po skončení boje metoda vypíše výsledky do konzole.*
3) *Vytořte několik objektů bojovníků a nechte je spolu bojovat.*

**příklad řešení:**
``` python
class Monster:
    def __init__(self, name, power, lives):
        self.name = name
        self.power = power
        self.lives = lives

    def print_status(self):
        if self.is_dead():
            print(self.name + ": dead")
        else:
            print(self.name + ": " + str(self.lives) + " lives")

    def is_dead(self):
        return self.lives <= 0

    def fight(self, attacker):
        if self.is_dead() or attacker.is_dead():
            dead_name = self.name if self.is_dead() else attacker.name
            print("Cannot fight, " + dead_name + " is dead.")
            return
        if self.power == attacker.power:
            print("It's a draw")
        elif self.power > attacker.power:
            attacker.lives -= 1
            print(self.name , "won")
        else:
            self.lives -= 1
            print(attacker.name, "won")

        print("Current status:")
        self.print_status()
        attacker.print_status()


ghost = Monster("Casper", 100, 5)
mummy = Monster("Tutanchamon", 75, 5)

ghost.fight(mummy)
```

