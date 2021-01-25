"""
a = int(input())
b = int(input())

print(a, b)

a, b = b, a

c = a
a = b
b = c

"""

# stdin standard input
# stout std output
# sterr error output

# type of triangle
# /_\ equilateral rovnostranny
# /__\ rovnoramenny isosceles
# obecny

"""
a = int(input())    # sides of triangle
b = int(input())
c = int(input())

if a == b:
    if b == c:
        print("rovnostranny/equilateral")
    else:
        print("rovnorameny/isosceles")
else:
    if b == c:
        print("rovnorameny/isosceles")
    else:
        if a == c:
            print("rovnorameny/isosceles")
        else:
            print("obecny")


if a == b and b == c:
    print("rovnostranny/equilateral")
elif a == b or b == c or a == c:
    print("rovnorameny/isosceles")
else:
    print("obecny")

"""

# while cycle / loop
# iteration
"""

x = 5

while x != 0:
    x = x - 1
    print(x)

print("end of cycle")
   

a = int(input("Write a num"))
b = int(input("Write a num"))

while b == 0:
    print("Can't devide by 0")
    b = int(input("Write a different num"))

print(a//b)

"""

# for loop
# for _variable_ in something:

word = "hello" # str iterable

for letter in word:
    print(letter)







    

            

