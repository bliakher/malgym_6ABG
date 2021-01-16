# Domácí úkoly

*Na úkolech můžete spolupracovat v menších skupinkách, ale řešení sepisujte samostatně. Pouze vyzrazení řešení není spolupráce. Pokud jste s někým spolupracovali, napište mi s kým.*

### BONUS: Páska a nůžky - 2 body
- Hráči dostanou pásku sudé délky, na které jsou napsaná kladná čísla. Tah: hráč si vybere jeden z okrajů pásky, který ustřihne. Podle toho, kolik je na ústřižku napsáno, tolik má bodů. Vyhrává hráč s nejvíce body.
- Existuje neprohrávající strategie? Pro kterého hráče?
- Řešení sepište a pošlete na mail, **předmět mailu: 5.AG Páska a nůžky**
- **Deadline** 13. 9. 2020 23:59

### 1. Vývojový diagram - 5 bodů
- Na vstupu jsou zadaná **různá** 3 čísla - a, b, c. Úkolem je vymyslet algoritmus, který čísla seřadí podle velikosti (vzestupně).
- Algoritmus zakreslete do **vývojového diagramu**. Doporučuju si ho nejdřív sepsat v bodech.
- Nápověda: zamyslete se, kolik je možných výstupů (seřazení 3 čísel)
- **Deadline** 4. 10. 2020 23:59

### 2. Python (instalace) - 1 bod
- Nainstalujte si Python na svůj domácí počítač podle návodu, který najdete v MS Teams -> Files -> Class Materials.
- Pošlete mi screenshot textového editoru IDLE (měl by se nainstalovat automaticky s Pythonem).
- V případě problémů mi pište.
- **Deadline** 11. 10. 2020 23:59

### 3. Prohození proměnných - 3 body
- Úkol slouží hlavně k tomu, abyste si připomněli, co jsme dělali na poslední hodině
- úkol: Napsat program v pythonu, který načte 2 čísla z uživatelského vstupu, uloží je do proměnných a proměnné vypíše. Poté prohodí obsah proměnných (tak aby v první proměnné bylo uložené to, co bylo ve druhé a obráceně), proměnné znovu vypíše. Nestačí jen vypsat proměnné v opačném pořadí.
- **Deadline** 25. 10. 2020 23:59

### 4. Převrácená hodnota absolutní hodnoty - 5 bodů
- **Absolutní hodnota** čísla a |a|
  - pro a v intervalu (-nek, 0) : |a| = -a
  - pro a v intervalu <0, +nek) : |a| = a
  - př. |-3| = 3, |5| = 5
- **Převrácená hodnota** čísla a je 1/a
  - př. převrácená hodnota 5 je 1/5
- Napište program v pythonu, který načte od uživatele celé číslo x a spočítá převrácenou hodnotu jeho absolutní hodnoty, tj. 1/|x|
- Pozor na dělení 0.
- **Deadline** 31. 10. 2020 23:59

### 5. Násobky čísla - 5 bodů
- Napište program v Pythonu, který načte číslo z uživatelského vstupu, a vypíše všechny násobky toho čísla menší než 100.
- Nápověda: využijte while cyklus a podmínku
- **Deadline** 8.(15.) 11. 2020 23:59


### 6. FizzBuzz - 6 bodů
- Ve hře FizzBuzz se 2 hráči střídají a říkají postupně čísla od 1 dál, dokud se někdo z nich nesplete. Při tom musí dodržet následující pravidla:
  - Pokud je číslo dělitelné 3, hráč místo něj řekne "Fizz".
  - Pokud je dělitelné 5, řekne "Buzz".
  - Pokud je dělitelné 3 i 5 zároveň, řekne "FizzBuzz".
- Vaším úkolem je napsat program, který vygeneruje tahák pro tuhle hru - načte číslo x ze vstupu a vygeneruje odpovědi do hry od 1 do x - 1, 2, Fizz, 4, Buzz, Fizz, 7...
- Můžete předpokládat, že vstup je vždy kladné celé číslo.
- Každé číslo se vytiskne na samostatný řádek výstupu.
- **Deadline** 21. 11. 2020 23:59
  
### 7. Druhý největší prvek - 8 bodů
- Napište program, který načte ze vstupu posloupnost n kladných čísel - posloupnost je ukončena -1, která značí konec vstupu.
- Na výstup vypište 2. největší prvek posloupnosti.
- Např.: pro vstup 1 31 2 5 87 12 34 9 -1 bude výstup 34
- **Deadline** 5. 12. 2020 23:59

### 8. Ježíškův poštovní software - 7 bodů
- Ježíšek dostává každoročně spoustu dopisů od dětí s jejich přáními. Ježíškovi pomocníci je stíhají roztřídit jen taktak před Vánoci. Ježíšek se proto rozhodl pořídit si na dopisy třídící software. Protože se jeho pomocníci budou muset zaškolit v jeho používání, je nejvyšší čas začít programovat.
- Napište program na třídění vánočních přání. Na vstupu dostanete číslo N - počet dopisů. Na následujících řádcích budou vypsány dopisy v předzpracované formě. Pro každý dopis dostanete na zvláštních řádcích jméno dítěte, číslo K (počet dárků, které si přeje) a na následujících K řádcích výčet dárků.
- Vaším úkolem je vypsat pro Ježíška všechny druhy dárků, které se v dopisech vyskytly, aby věděl, které dárky má vyrábět.
- Zamyslete se nad hezkou funkční dekompozicí.
- Příklad vstupu a výstupu je ve zvláštním souboru.
- **Deadline** 24. 1. 2021 23:59

### BONUS: Nemám dost bodů - 7 bodů
**Možnost 1: Stromeček**
- Napiš funkci, která pro zadané číslo N vypíše N-patrový stromeček z hvězdiček. Příklad pro N = 4:

     *
    ***
   *****
  *******

**Možnost 2:**
- Napiš nějaký hezký program, kterým mi ukážeš, že si zasloužíš jedničku :-) Nejlépe by měl obsahovat slovníky nebo množiny a být hezky rozdělený do funkcí. Může to být nějaký jednoduchý algoritmus, nebo může třeba něco hezkého "vykreslovat" (jako stromeček v možnosti 1).

