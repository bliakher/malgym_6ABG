# 15.hodina - 7. 1. 2022

## Text na obrazovce

1) inicializace konkrétního fontu:
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

- další parametry - italics a bold

``` python
SysFont(name, size, bold=False, italic=False)
```
