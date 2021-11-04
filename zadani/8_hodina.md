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
screen.blit(image, (50,50)) # (50, 50) souradnice (x, y)
```
- aby se projevila změna obrazovky, musíme provést update obrazovky:
```python
pygame.display.update()
```

- škálování obrázku
```python

```

- barva pozadí pomocí RGB kódu:
```python
screen.fill((r,g,b))
```

### 1. úkol
*Vykreslit dva obrázky u sebe - napozicovat do kompozice - a vybarvit pozadí. Např. pes s kloboukem na hlavě, člověk s koštětem v ruce..*
*Obrázky se postupně vrství na sebe podle pořadí v kódu. Zkuste najít obrázky v png s půhledným pozadím a menší velikosti.*

![cat with ball](https://user-images.githubusercontent.com/44325210/140406440-5e9cf7f0-8e0c-485f-8a95-abe0debdd779.png)


### Pohyb

- pohyb - mění se pozice obrázku - překreslujeme obrázek na posunuté pozici
- proměnné pro pozici obrázku a o kolik ho chceme posouvat

```python
# define the position of the image
xpos = 50
ypos = 50
# how many pixels we move our image each frame
step_x = 1
step_y = 1
```

- vykreslení obrázku přesuneme dovnitř cyklu
- k poloze přičteme step - posun za jeden frame
- load nám stačí udělat pouze jednou

- **problém** obrázek se posouvá, ale zůstává tam vykreslený i starý obrázek
![Screenshot 2021-11-04 at 20 42 53](https://user-images.githubusercontent.com/44325210/140408918-73f64ffe-658f-4a2c-8b74-98198f8673ff.png)

- **řešení** než obrázek překreslíme na nové poloze, musíme vymazat obrazovku:
```python
# erase by repainting background over everything
screen.fill((200, 255, 200))
```

### 2. úkol
*Udělat jednoduchou animaci, kdy obrázek začne u levého okraje obrazovky a bude se pohybovat doprava, dokud nenarazí na pravý okraj, tam se zastaví*

### 3. úkol
*Upravit animaci tak, aby se obrázek odrážel ze strany na stranu*

