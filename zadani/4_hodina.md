# 3. hodina - 25. 2. 2022

## Magické metody

- speciální metody označené 2 podtržítky kolem názvu
- konstruktor - `__init__` - je magická metoda
```python
class Cat:
  def __init__(self, name):
    self.name = name
```

- nikdy je nevoláme přímo pomocí názvu
```python
cat = Cat("Udo")
# zavola se Cat.__new__()
# pak Cat.__init__("Udo")
```
### __str__()
- vytisknutí objektu pomocí `print()`
- zkuste - co se stane?
```python
class Cat:
  def __init__(self, name):
    self.name = name
    
cat = Cat("Udo")
print(cat)
```

- jak vyřešit?
  - při volání funkcí `str()` a `print()` na objektu se zavolá magická metoda `__str__()`
  - metodu můžeme v definici třídy. předefinovat na reprezentaci, kterou chceme

```python
class Cat:
  def __init__(self, name):
    self.name = name
    
  def __str__(self):
    return "cat: " + self.name
    
cat = Cat("Udo")
print(cat)
```
- teď už bude fungovat

### Úkol 1
*Přidejte do svojí třídy Zlomek magickou metodu `__str__()` a vyzkoušejte, že jde zlomek vytisknout pomocí printu.*

### Předefinování operátoru
- magické metody také slouží k předefinování operátorů
- při použití jakéhokoliv matematického operátoru (+, -, \*, /, <, ... ) se volá odpovídající magická metoda
```python
a = 10
b = a + 5
c = a.__add__(5)
print(b)
print(c)
```
- můžeme použít na svojí vlastní třídě, aby na ní fungovaly matematické operátory

### Úkol 2
*Přidejte do svojí třídy Zlomek magickou metodu `__add__()`, tak aby následující kód fungoval.*
```python
a = Zlomek(1, 2)
b = Zlomek(1, 3)
c = a + b
print(c)
```

### Konverzní metody
- už známe konverzní metody pro převádění mezi datovými typy:
  - int()
  - str()
  - float()

- někdy může dávat smysl převést objekt na číslo
```python
a = Zlomek(1, 2)
b = 0.5
c = a + b
print(c)
```
- nebude fungovat - vyhodí error - nemůžu sčítat float a Zlomek
- můžu použít metodu `hodnota()`
```python
a = Zlomek(1, 2)
a = a.hodnota()
b = 0.5
c = a + b
print(c)
```

- místo hodnoty, bych mohla použít konverzní funkci `float()`
```python
a = Zlomek(1, 2)
a = float(a)
b = 0.5
c = a + b
print(c)
```
- samo o sobě nebude fungovat, `float()` je globální funkce, ne metoda třídy Zlomek a nebere Zlomek jako argument
- umožníme předefinováním magické metody `__float__()`

### Úkol 2
*Přidejte do svojí třídy Zlomek magickou metodu `__float__()`, tak aby předchozí kód fungoval.*
 
