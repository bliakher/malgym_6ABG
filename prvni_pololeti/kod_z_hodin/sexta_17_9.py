poklad = "OOOXXOOOOXOOOOXXOXXXOXOOOOOXOOOOOXOOOOXXOOXOOOOXXXOOOXXXOOXXXOXXOOOOOXXOOOXXXOOOOOXOXXOOOOXXXOXXXOOOXXOXXXOOOXXOOXXXOOOXXOOOOXXXOOOXOOOOOXXXOOXOOOOXXXOOXXOOOOXOOOXOOOOXXXOOOO"

mince = 0
diam = 0

for vec in poklad:
  if vec == "O":
    mince += 1
  elif vec == "X":
    diam += 1

print(mince)
print(diam)

koruny = 0

while diam > 0 and mince > 1:
  mince -= 2
  diam -= 1
  koruny += 1

print(koruny)

with open("rodokmen.txt", "r") as f:
  babicka = f.readline()
  deti = int(f.readline())
  vnoucata = 0
  for i in range(deti):
    f.readline() 
    deti_ditete = int(f.readline())
    vnoucata += deti_ditete
    for j in range(deti_ditete):
      f.readline()

print(vnoucata)


