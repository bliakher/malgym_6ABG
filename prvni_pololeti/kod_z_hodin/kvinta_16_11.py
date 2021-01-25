
# pole - arrays
# seznam - list

a = 5
b = "hello"

num1 = 1
num2 = 3
num3 = 7
num4 = 18

numbers = [1, 3, 7, 18]

cars = ["Skoda", "BMW", "Fiat"]
#       idx = 0  idx = 1 idx = 2

boolean = [True, False, False]

# pole/array - every value of the same type

# seznam/list - flexible

values = [1, "hello", True]

# list_name[index of value]
# index - from 0

"""
bmw = cars[1]
print(bmw)

numbers[1] = 5
num2 = 5

print(numbers)

cars.append("Mazda")
print(cars)

mazda = cars[3]

# length of array/velikost pole - len()

cars_length = len(cars)
print(cars_length)


word = "hello"
word = ["h", "e", "l", "l", "o"]

for letter in word:
    print(letter)

for car in cars:
    print(car)

idx = 0
while idx < len(cars):
    car = cars[idx]
    print(car)
    idx += 1
"""
"""
numbers = [1, 3, 7, 18]

# add 1 to each element of the list numbers

for num in numbers:
    num = num + 1
    print(num)

for idx in range(len(numbers)): #range(n) -> 0, 1, 2, 3, .., n-1
    num = numbers[idx]
    num += 1
    numbers[idx] = num

print(numbers)    

for idx in range(len(numbers)): #range(n) -> 0, 1, 2, 3, .., n-1
    numbers[idx] += 1

print(numbers)

"""

numbers = [1, 3, 7, 18]

num5 = int(input())

numbers.append(num5)

print(numbers)


numbers = []

# read values from input until we get -1, add each to list

num = int(input())

while num != -1:
    numbers.append(num)
    num = int(input())

print(numbers)

# only add even numbers to list

num = int(input())

while num != -1:
    if (num % 2 == 0):
        numbers.append(num)
    num = int(input())

print(numbers)








