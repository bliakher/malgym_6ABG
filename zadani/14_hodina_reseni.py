# sum of elements in the list -----------------------

def sum (list):
    num = 0
    for i in range(len(list)):
        num = num + list[i]
    return num
    
# basics about dictionaries --------------------------

names = {
# key : value (klic : hodnota)
"name" : "Max",
# za kazdym parem musi byt carka jinak bude syntax error
"surname" : "Klimes"
}

names ["surname"] = "Tittelbachova"
#chaning a value
names ["favourite programming language"] = "Python"
#adding a key value pair

#for key in names:
 #looping thru dictionary 
 
# dictionary with names ------------------------------

names = ["Jane", "Edgar Allan", "Lev"]
surnames = ["Austen", "Poe", "Tolstoy"]
def dictionary(a, b):
  dictionary = {}
  for i in range(len(a)):
    name = a[i] #key
    surname = b[i]  #value
    dictionary[name] = surname
  return dictionary

dict = dictionary(names,surnames)
print(dict)

# fridge simpler version ------------------------------

def count_items(fridge_list):
  amount_dict = {"egg" : 0, "milk" : 0, "cheese" : 0}
  for item in fridge_list:
    amount_dict[item] += 1
  print(amount_dict)

fridge = ["egg", "egg", "milk", "cheese", "egg", "cheese"]
count_items(fridge)

# fridge full version ----------------------------------

def count(list):
  dict = {} 
  for i in list:
    if i in dict:
      dict[i] += 1
    else:
      dict[i] = 1
  
  for i in dc:
    print(i + ": " + str(dc[i]))



