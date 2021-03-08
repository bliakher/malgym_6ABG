## Basic Python syntax

### Cycles
- while
``` python
# while condition:
#    body of cycle
 
i = 0
while i < 4:
  print(i)
  i += 1

# -> 0, 1, 2, 3
```

- for
``` python
# for variable in range(number):
#     body of cycle

for i in range(4):
  print(i)

# -> 0, 1, 2, 3

# for variable in range(min, max, step):
#     body of cycle
  
for i in range(2, 9, 2):
  print(i)
  
# -> 2, 4, 6, 8

# for element in someting_iterable:
#     body of cycle

# strings or arrays are iterable

s = "abc"
for letter in s:
  print(letter)

# -> a, b, c
```

### Arrays
- data structure that can hold multiple elements
- ordered - the order of elements matters
- in python - elements can be of different types

``` python
array = [1, "abc", True, 1.4]
```
- index of element 
  - order of an element in array
  - we count from 0
  - first element in array has index 0, second has index 1..
- accessing element by index:
``` python 
numbers = [1, 2, 3, 4]
first = numbers[0]  # 1
second = numbers[1] # 2

idx = 2
element_at_idx = numbers[idx] # 3
```
- change element at index:
``` python
numbers = [1, 2, 3, 4]
numbers[2] = 42 
# -> numbers = [1, 2, 42, 4]
```
- append - add new element at the end:
``` python 
numbers = [1, 2, 3, 4]
a = 5
numbers.append(a)
# -> numbers = [1, 2, 3, 4, 5]
```
- length of array = number of elements
``` python
numbers = [1, 2, 3, 4]
length = len(numbers) # 4
```

### Arrays and cycles

- we often need to access elements of array one by one
- we can use cycles to do it
- we use index to access elements - index is changed in cycle -> different elements
``` python
numbers = [1, 2, 3, 4]

# print all elements
# while cycle
index = 0
while index < len(numbers):
  current_element = numbers[index]
  print(current_element)
  index += 1

# for cycle - with index
for index in range(len(numbers)):
  current_element = numbers[index]
  print(current_element)
  
# for cycle - implicit
for element in numbers:
  print(element)

# implicit for can't change array
# change only with index
# increase all values in numbers array by one
numbers = [1, 2, 3, 4]

i = 0
while i < len(numbers):
  numbers[i] += 1
  i += 1
  
# or

for i in range(numbers):
  numbers[i] += 1

# result -> numbers = [2, 3, 4, 5]

```


