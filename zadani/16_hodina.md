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

### Úkol 1

*Nejdřív zkuste zobrazit nějaký text v defaultním fontu. Pak zaexperimentujte s fonty. 
Nechte si vypsat, jaké fonty jsou podporované a vyzkoušejte je.
Zkuste změnit barvu a barvu pozadí. Zkuste kurzívu a tučné písmo.*

### Úkol 2

*K první hře z minula - míček se pohne zleva doprava, když zmáčkneme šipku, dokud nedorazí na druhý konec - přidejte zobrazování vzdálenosti od levého okraje.*

### Úkol 3

*Ke stejné hře přidejte měření času - jak dlouho trvalo, než se povedlo dostat míček na druhou stranu.
Můžete využít funkce z [pygame.time](https://www.pygame.org/docs/ref/time.html).*

### Úkol 4

*Udělejte jednoduchý časovač.
Po spuštění aplikace nechte uživatele zadat čas do konzole - např. počet minut a vteřin.
Opět využijte pygame.time - zobrazujte, jak čas plynule ubývá.
Když čas dojde, zastavte odpočítávání a signalizujte konec. Můžete například změnit barvu pozadí.*










