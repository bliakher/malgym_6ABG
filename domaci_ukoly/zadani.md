# Domácí úkoly

*Na úkolech můžete spolupracovat v menších skupinkách, ale řešení sepisujte samostatně. Pouze vyzrazení řešení není spolupráce. Pokud jste s někým spolupracovali, napište mi s kým.*

#### 1. Počet vět - 6 bodů
- Ze standardního vstupu načtěte jméno souboru. Spočítejte počet vět v danném souboru a vypište výsledek na standardní výstup.
- Můžete předpokládat, že soubor ze vstupu existuje a jde otevřít.
- Věta je úsek textu složený ze slov oddělených mezerami, zakončená tečkou ".", otazníkem "?" nebo vykřičníkem "!".
- Příklad vstupního souboru:
```
Věta na jednom řádku!
Věta na
dvou řádcích.
Věta?
..?
```
- Výstupem bude 3
- **Deadline** 20. 2. 2021 23:59

#### 2. Casino - 1.část - 8 bodů
- Cílem je vytvořit hru, která bude simulovat jednoduché sázecí hry. 
- Úkol bude rozložený do několika částí.
- Jak bude hra vypadat - uživatel přijde do kasina a dostane přidělenou nějakou částku (bank), ze které může sázet.
- Uživateli budou dále nabídnuty hry, které může hrát. Vybere si hru, kterou začne hrát, z ní se může vrátit zpět do hlavní části kasina a vybrat jinou hru. 
- V první části vytvoříte hlavní herní smyčku a jednu sázecí hru. Hru si můžete vymyslet jakoukoliv.
- V každé hře bude nějaký element náhody, uživatel si na něco vsadí, může peníze vyhrát nebo prohrát.
- Je potřeba kontrolovat, aby nemohl vsadit víc, než má peněz v banku (nemůže se dostat do minusu).
- Nápady na jednoduché hry:
  - hod mincí
  - hod kostkou
  - hod 2 kostkami - součet
- Složitější hry:
  - ruleta
  - vyšší karta
  - blackjack
- **Deadline** 4. 4. 2021 23:59

#### 3. Casino - 2.část - 8 bodů
- Ve druhé části zapracujte do svého casina moje připomínky k první části a vytvořte druhou hru.
- Dodržte prosím strukturu hry - hlavní menu - vybery hru - můžu ji hrát kolikrát chci - odejdu ze hry a vrátím se opět do menu.
- Druhá hra by měla být o něco komplikovanější než ta první - nestačí hod mincí nebo hod kostkou.
- Pokud si nebudete jistí složitostí svého nápadu nebo bude potřebovat pomoct, **nebojte se mi napsat**.
- Nápady na hry:
  - ruleta (s možností sázky na barvu - červené/černá)
  - vyšší karta
  - blackjack
  - ruská ruleta
  - hádání čísla 
    - počítač mi říká, jestli je hádané číslo větší nebo menší než můj tip 
    - můžu sázet např. na počet hádání, které budu potřebovat
  - více hodů mincí
    - uživatel tipuje nějakou posloupnost hodů např. 0100
    - casino hodí mincí tolikrát (v příkladu 4krát) - kontroluje, jestli se shoduje s tipem
    - výhra může být za přesnou shodu, za počet shod, ...
  - vaše vlastní nápady, představivosti se meze nekladou
- **Deadline** 24. 4. 2021 23:59

### 4. Rekurze - součet prvků v poli - 7 bodů
- Napište rekurzivní funkci, která vezme pole čísel a vrátí součet všech prvků pole.
- **Deadline** 30. 5. 2021 23:59

### BONUS: Bakaláři - 6 bodů
- Programujeme zjednodušenou kontrolu docházky pro bakaláře.
- Naše docházka - pole jmen studentů, kteří byli na hodině.
- např. pritomni = ["Michal K", "Max K", "Nikola H"]
- Učitel zadá do našeho programu jméno studenta a my mu odpovíme, jestli tento student byl na hodině.
- např. pokud učitel zadá "Nikola H", odpovíme "Přítomen", pokud zadá "Julie T", odpovíme "Nepřítomen"
- **Deadline** 20. 6. 2021 23:59
