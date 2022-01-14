15.hodina - 7. 1. 2022

## Práce s klávesami

### Detekce zmáčknutí klávesy

2 způsoby:

**KEYDOWN event**
- podívám se, jestli nastal event (událost) zmáčknutí klávesy
- jestli ano, podívám se, jestli klávesa, která mě zajímá byla zmáčknutá

```python
# get all events
for event in pygame.event.get():   
    # check for any key down events
    if event.type == pygame.KEYDOWN:
        # check for specific key
        if event.key == pygame.K_LEFT:
          # do something
```

**všechny zmáčknuté klávesy**
- získám všechny zmáčknuté klávesy - nemusí být žádná
- podívám se, jestli je mezi nimi klávesa, která mě zajímá

``` python
# get all keys pressed at the moment
pressed = pygame.key.get_pressed()   
# check for specific key
if pressed[pygame.K_LEFT]:
  # do something
```

#### Úloha 1
*Napište jednoduchou "hru". Postavička začíná na levé straně obrazovky. Pokaždé, když hráč zmáčkne pravou šipku, pohne se o kousek doprava. Když dojede na druhou stranu, hra končí.*

### Detekce puštěné klávesy

**KEYUP event**
- podívám se, jestli nastal event (událost) puštění klávesy
- jestli ano, podívám se, jestli tlačítko, které mě zajímá bylo puštěné

```python
# get all events
for event in pygame.event.get():   
    # check for any key down events
    if event.type == pygame.KEYUP:
        # check for specific key
        if event.key == pygame.K_LEFT:
          # do something
```

**všechny zmáčknuté klávesy**
- pamatuji si, že klávesa byla předtím zmáčknutá
- podívám se na všechny zmáčknuté klávesy
- pokud mezi nimi moje klávesa už není, pak byla puštěna


#### Úloha 2
*Napište jednoduchou "hru". Postavička začíná na levé straně obrazovky. Když hráč zmáčkne pravou šipku, začne se pohybovat doprava a zastaví se, až když hráč pustí šipku. Když dojede na druhou stranu, hra končí.*
*Použijte oba způsoby detekce kláves.*


