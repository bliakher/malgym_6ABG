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

### Working with files
- let's look in the cheatsheet and remind ourselves about files

### Group task
- Work in groups, together write a solution to the task below. Every one in the team should understand the solution. Afterwards, we will come all together and each team will present their solution. From each team the person that wrote the least amount of code should present.

#### Number of words
- Considering an input file vstup.txt determine the number of the words contained in this file. Write total sum of the words into standard output.
-  A word is the maximal continuous interval of characters distinct from the space-character located on one line. Two words are separated by (at least one) space-character.
- At the beginning (of the line) or at its end no space-characters are necessary (i.e., they may be there but also they do not need to be there).
- Don't forget to sensibly divide your code into functions.


