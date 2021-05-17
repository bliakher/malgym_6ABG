
# faktorial - pocet permutaci
# permutace - prehazeni

# mam 5 lidi
# kolika zpusoby je muzu seradit do fronty

# 5! = 5 * 4 * 3 * 2 * 1
# a, b, c, d, e
# b e c
# 5 * 4 * 3 * 2 * 1
"""
def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

print(factorial(3))


# 5! = 5 * (4 * 3 * 2 * 1)
# 5! = 5 * 4!

# n! = n * (n - 1)!
# 1! = 1
# 3! = 3 * 2! = 3 * 2 * 1! = 3 * 2 * 1


def factorial_rec(n):
    if n == 1:
        return 1
    else:
        result = n * factorial_rec(n - 1)
        return result

print(factorial_rec(5))

"""
# fibonacciho posloupnost

# prvni cislo je 0
# druhe cislo je 1
# kazde dalsi cislo je souctem dvou predchozich

# 0, 1, 1, 2, 3, 5, 8, ...

# n-te fibonacciho cislo : f(n)
# f(0) = 0
# f(1) = 1
# f(n) = f(n - 1) + f(n - 2)
"""
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(4))
"""
# nemeli bychom pouzivat rekurzi - neefektivni

# napocitat do n
# pro nejake n (vytiknout cisla od 1 do n)

# nejdriv musime (vytisknout cisla od 1 do n - 1)
# potom vytiskneme n

"""
def count_to(n): 
    if n > 0:
        count_to(n - 1)
        print(n)

count_to(3)
"""

# pole - vytisknout prvky pole

pole = [1, 23, 4, 56]

"""
for prvek in pole:
    print(prvek)
"""
"""

def print_array(a):
    print(a[0])
    if len(a) > 1:
        print_array(a[1:])

print_array(pole)
"""

# cislo - chceme spocitat ciferny soucet
# 123 -> 6
"""
123 % 10 = 3
s = 3 + 2 + 1
12 % 10 = 2
1 % 10 = 1
0 
"""

def cif_souc(n):
    soucet = 0
    while n > 0:
        posl_cifra = n % 10
        soucet += posl_cifra
        n = n // 10
    return soucet

print(cif_souc(123))

# rekurzivne

def ciferny(cislo, soucet = 0):
    if cislo == 0:
        print(soucet)
    else:
        ciferny(cislo // 10, soucet + cislo % 10)

ciferny(1234, 0)
    














    




























    
