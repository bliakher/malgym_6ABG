## **16.hodina - 18. 1. 2021**

#### Reading files
- try creating a text file in replit (in the panel on the right there is *Add file* button)
- write some text into the file on multiple lines
- now using python, read the content of the file
- try reading the file by one line and by one character
- create another file in a folder - to read it you can use relative path from the main.py file

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

- try creating a file with 
``` python
f = open(b.txt, 'w')
```
- try reading from one file and writing the contents to another file, check that the resulting files are the same


#### File as input
- take the fridge task from the last time 
- instead of reading fridge list from input try reading it from file
