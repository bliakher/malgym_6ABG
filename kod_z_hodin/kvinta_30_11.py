
# if condition:
#    body


# while condition:
#   body

# for variable in iterable:
#   body

#range(1, 6)
#string
#array/lists

array = [1, 2, 3]
first = array[0]
array[0] = 7

array.append(6)

length = len(array)

#test
"""
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 1:
        print(num)
"""
#sort
#reverse
#max
"""
list = [1, 2, 3]
max = max(list)
list.remove(max)
second = max(list)
"""
#array.remove(element)

#array.index(element)

#array.count(element)


# range(6) -> 0, 1, ..., 5
# range(min, max) -> min, min+1, ..., max-1
# range(min, max, step) -> min, min+step, min+step+step, ... , max-1
"""
for i in range(0, 10, 2):
    print(i)
    
print("------------")

for i in range(10, 0, -2):
    print(i)


#slices

num = [1, 2, 3, 4, 5]
print(num[2:4])
print(num[2:])
print(num[:3])


string = "hello"
pole = ["h", "e", "l"]
print(string[1:4])
"""

# functions

#examples
#max()
#print()

#syntax
# def function_name(parameters):
#   body

#function_name()

# procedure

def hello():
    print("Hello!")
    print("Welcome to my app!")

hello()

# parameters / arguments

def hello_user(user_name):
    print("Hello, " + user_name + "!")
    print("Welcome to my app!")

hello_user("Anna")
#print(user_name) - error - can't see variable
    

# functions
#return value - navratova hodnota

list = [1, 2, 3]
m = max(list)

# return
a = 2 + 3

def add(a, b):
    sum = a + b
    return sum

def add(a, b):
    return a + b

c = add(2, 3)
print(c)


# write function divide(a, b) -> divide them -> return result
# check if b not 0 -> None

def divide(a,b):
    if b == 0:
        print("Can't divide by zero.")
        return None
    else:
        division = a // b
        return division


print(divide(4, 2))
print(divide(4, 0))






























