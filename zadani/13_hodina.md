# 13.hodina - 10. 12. 2021

### replit

Lucka - https://replit.com/join/szwwkbcfqb-bliakher

Filip - https://replit.com/join/mkeunqwaqd-bliakher




## Generování objektů

### Úloha 1
*Udělat animaci padajícího sněhu*

![Screenshot 2021-12-09 at 13 31 12](https://user-images.githubusercontent.com/44325210/145397242-a52fa4e9-cabc-4c16-9108-0cd68f0b3efe.png)

- chceme aby se sníh náhodně generoval
  - v každém snímku se s nějakou pravděpodobností objeví vločka 
  - vločka se objeví na horním okraji obrazovky na náhodné souřadnici x
  - postupně padá dolů, dokud nedojde na spodní okraj

- polohu vloček si můžeme uložit do pole
- v každém snímku projdeme pole a updatujeme polohu všech vloček
- poté je nakreslíme - opět projdeme pole a pro každou polohu zavoláme kreslící funkci

``` python
import random

random.randint(min, max)
random.random()
```

## Interakce s uživatelem

### Úloha 2
*Na dolním okraji obrazovky vytoříme Santovy saně. Chceme vytvořit hru, ve které se Santa musí vyhnout padajícím sněhovým koulím. 
Přidáme možnost ovládat saně. Pomocí tlačítek šipek bude možné pohybovat se saněmi doleva a doprava.*

![Screenshot 2021-12-09 at 15 13 35](https://user-images.githubusercontent.com/44325210/145412227-d06ba9de-2dcd-4a81-be42-333cca3963f6.png)

### Detekce zmáčknutí tlačítka

- zmačknutí tlačítka uživatelem vyvolá událost - *event*
- všechny eventy, které se odehrály v jednom snímku zachytíme pomocí:
``` python
pygame.event.get()
```

- projdeme všechny eventy a podíváme se, jestli mezi nimi není nějaký, který nás zajímá
``` python
while running:
    # ...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```
- kromě `QUIT` budeme kontrolovat i zmáčknutí šipek
- při zmáčknutí šipky změníme polohu saní - posun doleva nebo doprava
- uživatel bude moct posouvat saně

- kontrola, jestli není zmáčknutá klávesa"
``` python
for event in pygame.event.get():
           
    # Condition becomes true when keyboard is pressed   
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            # ...
```
- názvy kláves - šipky: `pygame.K_LEFT` a `pygame.K_RIGHT`


## Kolize

### Úloha 3
*Pokud se Santa nezvládne sněhové kouli vyhnout, saně vybuchnou a hra skončí. 
Abychom poznali, že koule do saní narazila, potřebujeme dodělat kolize.*

![Screenshot 2021-12-09 at 15 22 54](https://user-images.githubusercontent.com/44325210/145413968-100ed028-7100-4ed9-ba4c-e620ebc3df14.png)

- pro každou sněhovou kouli potřebujeme zkontrolovat, že se nedostala do obdélníku, uvnitř kterého se nachází saně
- když dojde k nárazu, ukončíme hru




