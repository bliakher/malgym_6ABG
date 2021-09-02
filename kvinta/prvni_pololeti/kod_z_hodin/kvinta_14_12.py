
"""

def function(param1, param2):
    #body
    # b not visible
    
    b = 5
    # b is visible
    # b is a local variable
    print(b)
    print(a)
    print(param1)
    print(param2 * 5)
    return b

# scope (visibility) of variables - viditelnost promenych

def sum_of_2(a, b):
    sum = a + b
    return sum

def sum_of_3(a,b,c):
    sum = a + b + c
    return sum

a = 3
# a is a global variable
# global x local variables

print(a)
five = function(1, 2)

m = max([1,2,3])
# procedures x functions

# index

a = [1, 3, 5, 3, 6]
print(a.index(3)) # time complexity linear
# worst case


print(a.count(3)) # time complexity linear
"""
"""
go through the list
compare each element to the one
for each good we find we increase counter
"""

# more data structures
# variable
# array / list
# each value has
# ordered by indexes
# list[index]
# indexes: 0, 1, .., len-1

# dictionary - slovnik
# pairs: key - value (klic - hodnota)


list_of_presents = {"Nikola" : "chocolate",
                    "Filip" : "car",
                    "Max" : "arduino",
                    "Krystof" : "arduino"}

present_of_Max = list_of_presents["Max"]
print(present_of_Max)

list_of_presents["Jirka"] = "salami"
#list_of_presents["Ondra"] = ["quiet", "new PC"]

print(list_of_presents)

for key in list_of_presents:
    print(list_of_presents[key])


# set - mnozina
# {1, 2, 3} == {1, 2, 2, 3}

my_set = {2, 3, 4, 17}
print(my_set)
my_set.add(5)
my_set.add(4)
print(my_set)

# create a set of all kinds of presents from
# the present list (dictionary)

list_of_presents = {"Nikola" : "chocolate",
                    "Filip" : "car",
                    "Max" : "arduino"}

presents = {"first_present"}

for key in list_of_presents:
    presents.add(list_of_presents[key])
print(presents)


















