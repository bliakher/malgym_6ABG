# 3. hodina - 24. 9. 2021

### Fibonacci

Fibbonaciho posloupnost je posloupnost přirozených čísel, kde každé další číslo je součtem dvou předchozích.
Prvních 10 čísel posloupnosti: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Napiš funkci, která bere číslo X a generuje fibbonacciho čísla menší než X.

### Fibonacci rekurzivně

Vzorec pro n-té fibonacciho číslo jde vyjádřit rekurzivně:
F(1) = 1, F(2) = 2, F(n) = F(n-1) + F(n-2)
Napiš rekurzivní funkci, která vezme číslo N a vypíše N-té fibonacciho číslo.

Zamysli se, jestli je efektivnější počítat n-té fibonacciho číslo rekurzivně, nebo bez rekurze pomocí cyklu?

<details>
<summary>Odpověď:</summary>
  
  Výpočet pomocí rekurze je mnohem pomalejší, protože zbytečně počítá znovu výsledky, které už máme spočítané.
  Chci spočítat 5. fibonacciho číslo a zavolám fib(5).
  Uvnitř fib(5) se zavolá fib(5) = fib(4) + fib(3).
  Když počítáme fib(4): fib(4) = fib(3) + fib(2). 
  Když to máme, tak se vrátíme k rozpočítanému fib(5).
  Teď spočítáme část + fib(3).
  Ale fib(3) už jsme měli spočítané, když jsme počítali fib(4). 
  Je to tedy zbytečná operace, která zpomalí celý program.
  
  Při počítání pomocí cyklu se tohle neděje, protože generujeme čísla odspodu. 
  Začneme s 1 a 2 a spočítáme 3, pak 2 + 3 = 5. 
  Vždy pracujeme pouze se 2 nejnovějšími hodnotami, každou hodnotu používáme jen jednou.
  
  V případě fibonacciho čísel je rekurzivní způsob velmi neefektivní, i když je elegantní.
  
  
</details>
