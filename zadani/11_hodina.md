# 11.hodina - 26. 11. 2021

## Pygame - kreslení obrázků pomocí kódu

- [Odkaz na dokumentaci](https://www.pygame.org/docs/ref/draw.html)

- všechny funkce jsou v:
``` python
pygame.draw
```
- používá se struktura `pygame.Color`
- má 3 složky - R, G, B

``` python
black = pygame.Color(0,0,0)
```

- **nezapomeňte na update**
```python
pygame.display.update()
```

### Linky

``` python
pygame.draw.line(surface, color, start_pos, end_pos, width=1)
```
- surface - povrch, na který kreslíme - v našem případě `screen`
- color - barva čáry - `pygame.Color`
- start_pos - souřadnice začátku - tuple
- end_pos - souřadnice konce
- width - tloušťka čáry - defaultně 1

použití:
``` python
pygame.draw.line(screen, black, (10, 10), (100, 100))
```

### Čtverec/obdélník

``` python
pygame.draw.rect(surface, color, rect, width=0)
```
- surface a color stejné
- rect - obdélník na nakreslení - struktura `pygame.Rect`
  - `Rect(left, top, width, height)`
  - **pozor** levý horní roh, šířka, výška
- width - defaultně 0
  - width == 0 - vyplněný dannou barvou
  - width > 0 - nevyplněný - width je tloušťka čáry

``` python
pygame.draw.rect(screen, black, pygame.Rect(20, 20, 100, 100)) // vyplneny ctverec
pygame.draw.rect(screen, black, pygame.Rect(20, 20, 100, 100), width=1) // nevyplneny - tloustka 1
```

### Kruh

``` python
pygame.draw.circle(surface, color, center, radius, width=0)
```
- surface a color stejné
- center - střed kruhu - souřadnice - tuple
- radius - poloměr
- width - stějně jako u obdélníku

### 1. úkol

*Nakreslete prsten a půlměsíc*
![Screenshot 2021-11-25 at 19 21 59](https://user-images.githubusercontent.com/44325210/143487609-d4a264af-3bb0-4199-af88-344f999ed25d.png)


### 2. úkol

*Nakreslete nějaký obrázek - domeček, panáček v klobouku atd.*









