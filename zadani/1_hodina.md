## 1. hodina - 1. 2. 2021

### Warm up
What will the following code do? Answer to chat.
``` python
a = 2
b = 3
c = 5

print(str(a) + str(b) + str(c))
```

### Usefull functions with strings
- string is like array of letters: ``` "hello"[0] --> "h" ```
- slicing: ``` "hello"[1:3] --> "el" ```
- concatenation: ``` "a" + "b" --> "ab" ```
- split(deliminator) - splits string to parts separated by deliminator, returns them as array
``` python
string = "a,b,c,d"
parts = string.split(',')
# parts --> ["a", "b", "c", "d"]
```
- strip(chars) - removes leading and trailing characters of a string
``` python
string = "      hello  "
# without arguments it trims whitespaces
print(string.strip()) # --> "hello"

# you can specify caracters to trim
string = ".....,.,hello,,,.."
print(string.split(",.")) # --> "hello"
```
