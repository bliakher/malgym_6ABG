# 2. hodina - 17. 9. 2021

### Vnoučata

Máte k dispozici rodokmen vaší rodiny. Ten vypadá následujícím způsobem.
Na 1. řádku je jméno babičky, na dalším je číslo N - počet babiččiných dětí. Dále následuje N záznamů pro každé dítě.
Záznam dítěte: na 1. řádku je jméno dítěte, pak číslo K - počet jeho dětí (vnoučat babičky) a dále K jmen dětí.
V rodině máte zajímavou tradici, jména všech dívek začínají na písmeno E a jména chlapců na písmeno M.
Vzorový rodokmen je v souboru `rodokmen.txt` - babička Eleonor má 3 děti - Matěje, Elišku a Martina.
Napište program, který pro libovolný rodokmen vypíše počet babiččiných vnoučat a kolik z nich je děvčat a kolik chlapců.

### Mlaďoch

Do rodokmenu jste doplnili ke každé osobě i její věk. Vzorový rodokmen je v souboru `rodokmen_vek.txt`
Vypište jméno nejmladšího muže v rodině.

### Páry


### Reklama

Firma na výrobu nafukovacích balónků by ráda zvýšila svoje zisky pomocí propagace vlastních produktů. Jenže ne u všech výrobků se reklama vyplatí. Pomozte firmě vybrat produkty, pro které má objednat reklamu.
Pro každý produkt dostanete:
- zisk s reklamou,
- zisk bez reklamy,
- cenu reklamy.

Pro každý produkt rozhodněte, zda se reklama vyplatí, a vypište buď:
- REKLAMU, pokud ano, nebo
- NE REKLAMU, v opačném případě.
Jedna z možností bude vždy výhodnější.

Na prvním řádku vstupního souboru je číslo T - počet produktů, o kterých musíte rozhodnout.
Následuje T řádků se třemi přirozenými čísly – zisk s reklamou, zisk bez reklamy, cena reklamy, v tomto pořadí.

Ukázkový vstup:
```
2
100 90 60
50 30 10
```
Ukázkový výstup:
```
NE REKLAMU
REKLAMU
```

Testový vstup:
```
10
4090 4003 15
120 100 30
550 550 3
1225 998 105
125 90 40
4376 3875 370
65 25 35
5000 4870 305
3000 4050 50
700 654 33

```

<details>
<summary>Výstup (na zkontrolování):</summary>
REKLAMU
  
NE REKLAMU

NE REKLAMU

REKLAMU

NE REKLAMU

REKLAMU

REKLAMU

NE REKLAMU

NE REKLAMU

REKLAMU

</details>
