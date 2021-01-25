# reading from file -----------------------------------

f = open("a.txt", 'r')
f.read()
f.readline()

# reading by line
for line in f.readlies():
  print(line)
  
# reading by character
c = f.read(1)
while c != "":
  print(c)
  c = f.read(1)
  
# writing to files -------------------------------------

f = open(a.txt, 'w')
f.write("The best text!") # this rewrites the whole file with new text

f = open(a.txt, 'a')
f.write("The best text!") # this adds new text at the end
  
# read from one file write to another ------------------

a = open("a.txt", 'r')
b = open("b.txt", 'w')

content_a = f.read()
b.write(content_a)

a.close()
b.close()

# or

a = open("a.txt", 'r')
b = open("b.txt", 'w')

for line in a.readlines():
  b.write(line)
  
a.close()
b.close()
  





