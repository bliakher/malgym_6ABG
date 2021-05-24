"""
def move(f, t):
    print(f"Move disc from {f} to {t}")

def move_via(f, t, h):
    move(f, h)
    move(h, t)


def hanoi(n, f, t, h):
    if n == 0:
        pass
    else:
        hanoi(n - 1, f, h, t)
        move(f, t)
        hanoi(n - 1, h, t, f)


hanoi(5, "A", "C", "B")
"""

def ma(ls, m=None):
    if not ls:
        return m
    if m is None:
        m = ls[0]

    if m < ls[0]:
        m = ls[0]
   
    return ma(ls[1:], m)

print(ma([1, 0, 24, 5, -2]))

def find_max_klimes(array, max_klimes):
    if len(a) < 1:
        return max_klimes
    if array[0] > max_klimes:
        max_klimes = array[0]
    array.pop(0)
    return find_max_klimes(array, max_klimes)








