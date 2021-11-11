# 9.hodina - 12. 11. 2021

## Pygame

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

### 4. úkol
*Udělat animaci míčku, který se odráží od všech stěn (samozřejmě tak, aby za sebou nenechával stopu).*

![Screenshot 2021-11-04 at 21 01 00](https://user-images.githubusercontent.com/44325210/140411495-6bebd89f-2d96-4f20-a1f2-9d1ed7fad170.png)

