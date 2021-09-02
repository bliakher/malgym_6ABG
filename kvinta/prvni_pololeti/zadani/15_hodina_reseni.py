# printing dictionary separated ----------------------------

def count(list):
  dict = {} 
  for i in list:
    if i in dict:
      dict[i] += 1  
    else:
      dict[i] = 1
  print_pairs(dict)
  
def print_pairs(dictionary):
  for i in dictionary:
    print(i + ": " + str(dictionary[i]))
    
# reading fridge items from input --------------------------

def input_to_array ():
  array = []
  inpt = str(input())
  while inpt != " ":
    array.append(inpt)
    inpt = str(input())
  return array

# interesting short way to do it:

# split() splits string into parts by a separator (in this case white space)
# it returns array of the parts of the string

def create_input_list():
  ls = input("Items: ").split(" ")
  count(ls)
  
# creating sets --------------------------------------------
# function set() takes something iterable (like an array) and makes a set of it's values

def setify(list):
  return set(list)

# references - explanation is in spoiler -------------------


  
