def count_letter(word, letter):
  count = 0
  for char in word:
    if char == letter:
      count += 1
  return count

print(count_letter("abraka", "a"))

def jmeno_vek(radek):
  radek = radek.split()
  jmeno = radek[0]
  vek = int(radek[1])
  return jmeno, vek

vnoucata = []
lidi = {}
with open("rodokmen_vek.txt", "r") as f:
  babicka = f.readline()
  j, v = jmeno_vek(babicka)
  lidi[j] = v
  deti = int(f.readline())
  for i in range(deti):
    dite = f.readline() 
    deti_ditete = int(f.readline())
    for j in range(deti_ditete):
      jmeno_vnoucete = f.readline()
      jmeno_vnoucete = jmeno_vnoucete.strip()
      vnoucata.append(jmeno_vnoucete)

print(lidi)

muzi = {}
