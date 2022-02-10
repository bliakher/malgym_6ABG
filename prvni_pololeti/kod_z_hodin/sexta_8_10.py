""""
def funkce(parametr):
  print(parametr)

def f(cislo, pismeno):
  print()
  return cislo

def sum(a, b):
  res = a + b
  return res
  print("neco")

def cyklus():
  for i in range(6):
    return i

def nic_nevraci():
  x = 1 + 3
  return

nic = None

print(nic_nevraci())

def deleni(a, b):
  if b == 0:
    return None
  return a / b
a = 2
b = 0
if b == 0:
  print(None)
print(a / b)


print(cyklus())

res = sum(2, 3)
x = 5 + 4

f(1, "a")
"""
"""
word = str(input()) 
letter = str(input()) 

count = 0 

def countLetter(word, letter): 
  #global count
  count = 0
  for i in word: 
      if letter == i: 
          count = count + 1 
  return count
 
count = countLetter(word, letter) 
print(count)
"""



def count_letter2(word, substring): 
  a = 0 
  b = len(substring) 
  substring_count = 0 
  while b<=len(word): 
    A = word[a:b] 
    if A == substring: 
      substring_count += 1 
    a += 1 
    b += 1 
  return substring_count 

print(count_letter2("abrakadabraka", "ab"))
print(count_letter2("bbbb", "bbb"))


def count_substring(word, substring):
  result = 0
  i = 0
  while i <= len(word) - len(substring):
    if word[i] == substring[0]:
      areTheSame = True
      j = i
      for char in substring:
        if word[j] != char:
          areTheSame = False
          break
        j += 1
      if areTheSame:
        result += 1
    i += 1

  return result






