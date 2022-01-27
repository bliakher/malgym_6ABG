# 18.hodina - 28. 1. 2022

## Detekce myši

- funguje podobně jako detekce kláves
- 2 možnosti:
  - eventy - zmáčnutí a puštění myši
  - získání stavu myši - je tlačítko zmáčknuté nebo ne

**1) eventy**
- `pygame.MOUSEBUTTONDOWN` a `pygame.MOUSEBUTTONUP`
- kontroloju se všemi eventy jako klávesy
- event navíc obsahuje informaci o pozici myši na obrazovce v okamžiku zmáčknutí - od levého horního rohu

``` python
for event in pygame.event.get():
  if event.type == pygame.MOUSEBUTTONDOWN:
    position = event.pos # pozition of the mouse
    # do something 
```

**2) stav myši**
- podobně jako stav kláves
- funkce `pygame.mouse.get_pressed()` získá informace o stavu tlačítek myši
- funkce `pygame.mouse.get_pos()` získání pozice kurzoru
- viz [dokumentace](https://www.pygame.org/docs/ref/mouse.html)

### Úloha 1

*Naprogramujte hru, kde můžeme myší ovládat pohybující se objekt, např. míček. Míček je na začátku ve středu obrazovky a nehýbe se. Když klikneme na nějaké místo na obrazovce, míček se začne pohybovat směrem k místu na které jsme klikli, dokud k němu nedojede, pak se zastaví. Pokud v průběhu pohybu míčku klikneme na jiné místo, míček změní směr. Udělejte nejdřív jednodušší verzi, kdy se míček pohybuje pouze po ose x, tedy vodorovně.*

### Úloha 2

*Upravte hru tak, aby se míč pohyboval po ose x i y a zastavil se přesně na místě, na které jsme klikli. Míček by se měl pohybovat konstantní rychlostí.*

### Úloha 3

*Napište aplikaci, ve které bude možné rozsvícet a zhasínat žárovku kliknutím na tlačítko.*


