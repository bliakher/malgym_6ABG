# warm up ------------------------------------

a = 2
b = 3
c = 5

print(str(a) + str(b) + str(c))

# vysledek: 235
# zduvodneni: str() prevede cisla na retezce, + je konkatenace retezcu - slepi se za sebe

# --------------------------------------------
# number of words 

# simple algorithm ---------------------------

with open("vstup.txt", "r") as f:
  text = f.read()
  words = text.split()
  print("Number of words", len(words))
  
# problem - ends of line
# hello\nfriend - counts as on word

"""
hi   hello
my friend

-> split : ["hi", "hello\nmy", "friend"]
"""


# how to repair? -----------------------------
# read text by lines:

words_count = 0
with open("vstup.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()   # strip the end of line (\n) character
    words = line.split()
    words_count += len(words) # number of words in one line
print("Number of words", words_count)    

# what if file is very long? ------------------

# whole file can't fit to RAM - we need to read it by parts
# by lines or even by one character

"""
cyklus - cteme soubor po znacich, dokud ho nedocteme do konce
znak    -> bily znak
            -> docetli na konec slova -> pricteme +1 slovo
        -> tisknutelny znak
            -> cteme slovo

"""

def open_file(file_name):
    f = open(file_name, 'r')
    return f

def count_words2(file):
    count = 0
    c = file.read(1)
    word = ""
    reading_word = False
    while c != '':
        if not is_space(c):     # is_space(c) == False
            reading_word = True
            word += c
        elif reading_word:  # is_space(c) and reading_word
            reading_word = False
            count += 1
            word = ""
        c = file.read(1)
    return count

def count_words(file):
    c = file.read(1)
    word = ""
    before = ''
    count = 0
    while c != '':
        if is_space(c) and not is_space(before):
            count += 1
            word = ""
        else:   # c je tisknutelny
            word = word + c
        before = c
        c = file.read(1)
    return count

def is_space(ch):
    return ch == ' ' or ch == '\n' or ch == '\r' or ch == '\t'

def solve():
    file_name = input("Enter name of the file:")
    file = open_file(file_name)
    words_count = count_words(file)
    print("Number of words in file:", words_count)
    file.close()

solve()

