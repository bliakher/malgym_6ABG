# 15.hodina - 7. 1. 2022

## Text na obrazovce

**1) inicializace konkrétního fontu:**
- objekt `Font`
``` python
font = pygame.font.SysFont(name, size) -> Font
```

- na různých systémech jsou dostupné různé fonty
- které fonty jsou dostupné:
``` python
available_fonts = pygame.font.get_fonts()
```

- pokud nespecifikujeme - vybere se defaultní font
``` python
font = pygame.font.SysFont(None, 24) # default font, velikost 24
```

- můžeme také dát pole fontů - vybere se první dostupný

``` python
font = pygame.font.SysFont(['freesans', 'dejavusans'], 24)
```

- další parametry - `italics` a `bold`

``` python
SysFont(name, size, bold=False, italic=False)
```

**2) vyrenderování textu do fontu:**
- zkombinujeme písmena a font a vytvoříme "obrázek", který můžeme nakreslit na obrazovku
- použijeme funkci `render`, která vytvoří "obrázek" - něco, na co můžeme použít `screen.blit()`
``` python
image = render(text, antialias, color, background=None)
```
- ale zavoláme ji na objektu fontu - vyrenderujeme text v daném fontu:
``` python
black = pygame.Color(0, 0, 0)
img = font.render('hello', True, black) # černé písmo na bílém pozadí
```

- můžeme přidat barevné pozadí pomocí parametru `background`

**3) vykreslíme vyenderovaný font**
- vyrenderovaný font můžeme nyní nakreslit stejně jako jiné obrázky
``` python
screen.blit(img, (20, 20))
```

``` python

```







