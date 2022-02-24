# 3. hodina - 25. 2. 2022

## Metody tříd

- **metoda** - funkce uvnitř třídy

```python
class Cat:
  def __init__(self, name):
    self.name = name
    
  def meow(self):
    print(self.name + " said: Meow!")
```
- konstruktor je speciální metoda
- první parametr vždycky `self` - odkazuje se na objekt, na kterém je metoda zavolaná
- pomocí `self` přistupuji k položkám objektu
- může se jmenovat jakkoliv - `self` je konvence
- volání metody:

```python
cat = Cat("Udo")
cat.meow() # zkrácená syntaxe
Cat.meow(cat) # ve skutečnosti
```

### 
