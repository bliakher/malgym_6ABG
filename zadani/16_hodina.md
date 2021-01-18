## **16.hodina - 18. 1. 2021**

#### Reading files
- try creating a text file in replit (in the panel on the right there is Add file button)
- write some text into the file on multiple lines
- now using python, read the content of the file
- try reading the file by one line and by one character

#### Writing to files
- work with the same file
- think about the difference between these 2:
``` python
f = open(a.txt, 'w')
f.write("The best text!")

f = open(a.txt, 'a')
f.write("The best text!")
```
- first think about it, then try in replit
<details>
<summary>Explanation - spoiler</summary>
``` python
f = open(a.txt, 'w')
f.write("The best text!") # this rewrites the whole file with new text

f = open(a.txt, 'a')
f.write("The best text!") # this adds new text at the end
```
</details>
