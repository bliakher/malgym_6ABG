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
