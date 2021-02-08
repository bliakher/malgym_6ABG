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

