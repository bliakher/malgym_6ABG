# 5. hodina - 8. 10. 2021

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
