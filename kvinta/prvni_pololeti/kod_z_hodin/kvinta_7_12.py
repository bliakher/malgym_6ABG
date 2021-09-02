
def name(parameter):
    print(parameter)


name("Evgenia")

def index(array, value):
# index of first element in array with value
    counter = 0
    for element in array:
        if element == value:
            return counter
        counter += 1
    return -1

def index(array, value):
# index of first element in array with value
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

a = [1,1,2,5]
idx = index(a, 2)
print(idx)
