# 4. hodina - 1. 10. 2021

### Slovník lidí
Pracujeme s rodokmenem tak, jak je definovaný v zadání 2. hodiny. 
Chceme načíst ze souboru s rodokmenem všechny členy rodiny do slovníku tak, 
aby klíčem bylo jméno osoby a hodnotou její věk.

Např. {"Eleonor" : 65}

Připomenutí, jak fungují slovníky v Pythonu: https://www.w3schools.com/python/python_dictionaries.asp

### Slovník mužů
Z načteného slovníku lidí chceme vytvořit nový slovník, kde budou pouze muži.
(Mužská jména začínají vždy na M.)

### Mlaďoch II
S pomocí slovníku všech mužů najdeme nejmladšího muže v rodině.

### Substring
Bonusová úloha v testu: chceme spočítat, kolikrát se danný substing vyskytuje ve stingu.
Neboli - máme nějaké slovo a nějaký kratší řetězec (několik písmen), 
chceme spočítat, kolikrát najdeme tuto skupinu písmen v zadaném slově.
- zkuste nejdřív rozmyslet a zformulovat algoritmus
- příprava: napište funkci, která bere slovo, podřetězec a pozici, a rozhodne jestli na této pozici ve slově začíná danný podřetězec
  - např. ve slově "abrakadabra" začíná najdeme podřetězec "ab", když začneme na nulté nebo na sedmé pozici ve slově 
