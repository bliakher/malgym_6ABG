
# pole - array
# pairs: index - value

a = ["a", "b", "c"]
# idx 0 - a
# idx 1 - b

# accessing element

# value = array[index]
# ordered

b = ["b", "c", "a"] # this array different from a


# dictionaries - slovniky
# data structure
# pairs: key - value

d = {"a" : "ahoj", "b" : "bagr", "c" : "citron"}

# accessing value
# value = dict[key]
# unordered

e = {"a" : "ahoj", "c" : "citron", "b" : "bagr"} # d and e are the same

print(d)
print(e)

dict_a = {0 : "a", 1 : "b", 2 : "c", 5 : "d"}
dict_a[0]

# add pair
# d[key] = value
d["a"] = "andel"
d["d"] = "dum"

print(d)


def count(list):
  dict = {}
  # pairs: key= product : value= amount in the fridge
  for i in list:
    if i in dict:
      dict[i] += 1
    else:
      dict[i] = 1
      
  print_pairs(dict)
  

def print_pairs(dictionary):
    for i in dictionary: # loop through keys
        print(i + ": " + str(dictionary[i]))

count(["egg", "banana", "egg"])


# function decomposition











