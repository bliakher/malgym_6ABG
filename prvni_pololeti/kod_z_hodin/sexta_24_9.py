def factorial(n):
  f = 1
  i = 1
  while i <= n:
    f = f * i
    i += 1
  print(f)

def factorial_rec(n):
  if n == 1:
    return 1
  # else 
  f = n * factorial_rec(n-1)
  return f

factorial(5)
print(factorial_rec(5))

n = 5
f = 1
for i in range(1, n+1):
  f = f * i

print(f)

vnoucata = []
with open("rodokmen.txt", "r") as f:
  babicka = f.readline()
  deti = int(f.readline())
  for i in range(deti):
    f.readline() 
    deti_ditete = int(f.readline())
    for j in range(deti_ditete):
      jmeno_vnoucete = f.readline()
      jmeno_vnoucete = jmeno_vnoucete.strip()
      vnoucata.append(jmeno_vnoucete)

print(vnoucata)
print("Pocet vnoucat", len(vnoucata))
kluci = 0
holky = 0

for jmeno in vnoucata:
  if jmeno[0] == "M":
    kluci += 1
  if jmeno[0] == "E":
    holky += 1

print("kluci:", kluci)
print("holky", holky)

def jmeno_vek(radek):
  radek = radek.split()
  jmeno = radek[0]
  vek = int(radek[1])
  return jmeno, vek

