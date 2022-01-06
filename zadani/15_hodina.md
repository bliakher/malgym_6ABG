# 15.hodina - 7. 1. 2022

## Práce s tlačítky

### Detekce zmáčknutí tlačítka

2 způsoby:

**KEYDOWN event**
- podívám se, jestli nastal event (událost) zmáčknutí tlačítka
- jestli ano, podívám se, jestli tlačítko, které mě zajímá bylo zmáčknuté

```python
# get all events
for event in pygame.event.get():   
    # check for any key down events
    if event.type == pygame.KEYDOWN:
        # check for specific key
        if event.key == pygame.K_LEFT:
          # do something
```

**všechna zmáčknutá tlačítka**
- získám všechna zmáčknutá tlačítka - nemusí být žádná
- podívám se, jestli je mezi nimi tlačítko, které mě zajímá

``` python
# get all keys pressed at the moment
pressed = pygame.key.get_pressed()   
# check for specific key
if pressed[pygame.K_LEFT]:
  # do something
```

