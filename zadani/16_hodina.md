## Working with files - cheatsheet

#### Opening
``` python
f = open(filename, mode)
```
- **f** is a *file handler* - something to work with files
- **filename**: relative to the python program
  - if saved in same directory - just name of the file - a.py
  - saved somewhere else - whole path to file - /Users/evgeniagolubeva/Desktop/a.py
- **modes**: different options to open a file
  - "r" - Read - Default value. Opens a file for reading, error if the file does not exist
  - "w" - Write - Opens a file for writing, creates the file if it does not exist
  - "a" - Append - Opens a file for appending, creates the file if it does not exist



