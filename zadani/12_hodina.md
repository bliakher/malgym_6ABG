# 12.hodina - 3. 12. 2021

## Pygame - parametrizované kreslení obrázků

- vybrané barvy:
``` python
black = pygame.Color(0,0,0)
yellow = pygame.Color(255, 255, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(101, 67, 33)
red = pygame.Color(255, 0, 0)
beige = pygame.Color(244, 226, 198)
```

### Úloha 1
*Procvičování z minula - nakreslete obrázek domečku.*

![Screenshot 2021-12-02 at 13 23 32](https://user-images.githubusercontent.com/44325210/144421264-bee1a4fc-325a-45e1-9a38-5c6c9ae08b71.png)


### Parametrizované kreslení:
- neříkáme přesně, na kterých souřadnicích se má kreslit
- souřadnice se odvozují ne od počátku, ale od nějakého dodaného bodu
- využijeme, když chceme stejný objekt kreslit opakovaně - např. pohyb

### Úloha 2
*K domečku chceme dokreslit plot. Plot je tvořený stejnými laťkami. Chceme ho nakreslit tak, aniž bychom specifikovali umístění každé konkrétní laťky - parametrizovaně.*

![Screenshot 2021-12-02 at 13 42 51](https://user-images.githubusercontent.com/44325210/144424176-6a19bcae-d812-4de9-be21-6f121456d6f5.png)

- postup:
  1) napsat funkci, která nakreslí lať plotu dané šířky a výšky na nějaké pozici
  2) napsat funkci, která nakreslí plot dané šířky pomocí opakovaného kreslení latí
