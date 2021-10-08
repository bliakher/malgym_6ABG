# 5. hodina - 8. 10. 2021

Co vytiskne první print? A druhý print?
``` python
x = 5

def funkce():
    x = 3
    
print(x)

funkce()

print(x)

```

Co vypíše následující kód?
``` python
x = 6

def funkce2():
    print(x)
    
funkce2()


```


A tohle?
``` python
def funkce3():
    x = 8
    
print(x)

```

Jaká 2 čísla se vypíšou?
``` python
x = 5

def funkce4(x):
    print(x)
    
print(x)

funkce4(7)

```


Následující program nefunguje tak, jak bylo asi zamýšleno. Co se stane, když ho spustíme? Jak to opravit?
``` python
word = str(input()) 
letter = str(input()) 

count = 0 

def countLetter(word, letter, count): 
    for i in word: 
        if letter == i: 
            count = count + 1 
 
countLetter(word, letter, count) 
print(count)
```
