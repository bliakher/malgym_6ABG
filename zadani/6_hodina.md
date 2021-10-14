# 6. hodina - 15. 10. 2021

### Podřetězce ve slově

``` python
def count_letter2(word, substring): 
  a = 0 
  b = 2 
  substring_count = 0 
  while b<=len(word): 
    A = word[a:b] 
    if A == substring: 
      substring_count += 1 
    a += 1 
    b += 1 
  return substring_count 

print(count_letter("abrakadabraka", "ab")) 

```

V programu je chyba, kterou jsme na minulé hodině hledali. 
Zkuste si teď program krokovat ne VS, podívat se, co se děje s důležitými proměnnými a připomenout si, kde je chyba.

