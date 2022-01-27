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
- viz (dokumentace)![https://www.pygame.org/docs/ref/mouse.html]
