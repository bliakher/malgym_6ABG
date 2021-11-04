# 8.hodina - 5. 11. 2021

## Pygame

### Instalace

- VisualStudio - virtuální prostředí - Manage Packages - pygame

### Jednoduchá aplikace
- credits: https://dr0id.bitbucket.io/legacy/pygame_tutorial01.html

```python
# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen_width = 240
    screen_height = 180
    screen = pygame.display.set_mode((screen_width, screen_height))
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

main()
```

### Nakreslení obrázku

- stáhnout obrázek - do složky s kódem
- nahrát obrázek do programu:
```python
image = pygame.image.load("01_image.png")
```

- vykreslení na obrazovku - pozice od levého horního rohu

```python
screen.blit(image, (50,50))
```
- aby se projevila změna obrazovky, musíme provést update obrazovky:
```python
pygame.display.flip()
```

- barva pozadí pomocí RGB kódu:
```python
screen.fill((r,g,b))
```

### *1. úkol*
*Vykreslit dva obrázky u sebe - napozicovat do kompozice - a vybarvit pozadí. Např. pes s kloboukem na hlavě, člověk s koštětem v ruce..*
*Obrázky se postupně vrství na sebe podle pořadí v kó
du. Zkuste najít obrázky v png s půhledným pozadím a menší velikosti.*

![cat with ball](https://user-images.githubusercontent.com/44325210/140406028-54dcd1b0-060b-4754-a19c-69eb79ff6ccb.png)



