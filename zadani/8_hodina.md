``` python

def reverse(a):
    b = []
    x = 1
    for i in range(len(a)):
       b.append(a[len(a)-x])
       x = x + 1
    return b

a = [1, 2, 3, 4, 5]
print(reverse(a, b))
```
