# 13.hodina - 10. 12. 2021

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

## Interakce s uživatelem

### Úloha 2
*Na dolním okraji obrazovky vytoříme Santovy saně. Chceme vytvořit hru, ve které se Santa musí vyhnout padajícím sněhovým koulím. 
Přidáme možnost ovládat saně. Pomocí tlačítek šipek bude možné pohybovat se saněmi doleva a doprava.*

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





