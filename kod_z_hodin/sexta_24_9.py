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

