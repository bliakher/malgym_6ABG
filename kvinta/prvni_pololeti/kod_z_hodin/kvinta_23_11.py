# pole / array
# seznam / list

a = [1,2,3]

a.append(4)

first = a[0]

a[0] = 43

length = len(a)

name = []
name.append("Ema")

#test
names = []
surnames = []

# 1.part

names = ["Anna", "Emma"]

for name in names:
    print("Hello, " + name + "!")

# 2.part

name = ["Anna", "Emma", "Max"]
surname = ["k", "r"]

i = 0

while i < len(name):
    print("Hello, " + name[i] + " " + surname[i] + "!")
    i += 1

for i in range(len(name)): # -> 0, 1,.., len-1
    print("Hello, " + name[i] + " " + surname[i] + "!")


zip()

"""
# string formating

#concatenating
a = "ahoj"
b = "b"
ab = a + b
print(ab)

# "multiplying" str
print(a * 3)

# formating
print(f"Variable a is {a}")

"""
# goal: find max in an array

x = [2, 3, 57, 1, 9]

print(57)

# sorted array

sorted_array = [2, 4, 5, 67, 101]
last = sorted_array[len(sorted_array) - 1] #and biggest element
print(last)

# not sorted array

x = [2, 3, 57, 1, 9]

a = 0

x = [2, 3]
x = [2, 3, 57]

current_biggest = x[0]

if x[1] > x[0]:
    current_biggest = x[1]


if x[2] > current_biggest:
    current_biggest = x[2]
    
x = [2, 3, 57, 1, 9]

biggest = x[0]

for num in x:
    if num > biggest:
        biggest = num
print(biggest)
    

# min


min = x[0]

for num in x:
    if num < min:
        min = num
print(min)
      


































