def reverse(array):
    idx = len(array) - 1
    rev = []
    while idx > -1:
        item = array[idx]
        rev.append(item)
        idx -= 1
    return rev

def reverse1(array):
    rev = []
    for idx in range(len(array) - 1, -1, -1):
        item = array[idx]
        rev.append(item)
    return rev

#print(reverse1([1, 2, 3,4 ,5]))

def soucet(a, b):
    v = a + b
    return v

#j = 0
#for i in range(5):
#    j = soucet(j, i)
#print(j)

def count_letter2(word, substring): 
  a = 0 
  b = 2 
  substring_count = 0 
  while b<=len(word): 
    A = word[a:b] 
    if A == substring: 
      substring_count += 1 
    a += 1 
    b += 1 
  return substring_count 

print(count_letter2("bbbb", "bbb")) 

