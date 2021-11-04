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


``` python

array = [1, 2, 3 ]
rev_array = []
x = len(array) - 1

def reverse(array, rev_array, x):
    for i in range(len(array)):
        if x > -1:
            rev_array.append(array[x])
            x = x - 1
            print(rev_array)

reverse(array, rev_array, x)
```

```python
def reverse(array):
    reversed = []
    for i in range(len(array), 0, -1):
        reversed.append(i)
    return reversed

print(reverse([1, 2, 3, 4, 5]))
```
