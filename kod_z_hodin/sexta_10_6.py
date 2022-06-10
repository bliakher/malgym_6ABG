import pandas as pd
import matplotlib.pyplot as plt

obyvatele = pd.read_csv("obyvatele.csv")
#print(obyvatele.head(5))

jmena = obyvatele[["jméno", "přijmení"]]
#print(jmena.head(5))

zeny = obyvatele[obyvatele["pohlaví"] == "F"]
muzi = obyvatele[obyvatele["pohlaví"] == "M"]

urcene_pohlavi = obyvatele[obyvatele["pohlaví"].isin(["F", "M"])]
#print(urcene_pohlavi.head(5))

#obyvatele["novy"] = obyvatele["pohlaví"] * 2
#print(obyvatele.head(5))

def ziskat_vek(cislo):
    cifry = str(cislo)[:2]
    vek = 2022 - (1900 + int(cifry))
    return vek

def preloz_pohlavi(id):
    return "muž" if id == "M" else "žena"

"""
rodna_cisla = obyvatele["rodné_číslo"]
veky = []
for cislo in rodna_cisla:
    vek = ziskat_vek(cislo)
    veky.append(vek)
obyvatele["věk"] = veky
"""

obyvatele["věk"] = obyvatele["rodné_číslo"].apply(ziskat_vek)

obyvatele["pohlavi_nazev"] = obyvatele["pohlaví"].apply(preloz_pohlavi)

#print(obyvatele.head(5))

print("průměrný věk:", obyvatele["věk"].mean())
print(obyvatele["věk"].describe())

zeny = obyvatele[obyvatele["pohlaví"] == "F"]
muzi = obyvatele[obyvatele["pohlaví"] == "M"]

print("průměrný věk:", zeny["věk"].mean())
print("průměrný věk:", muzi["věk"].mean())

prumer_vek = obyvatele.groupby("pohlaví")["věk"].mean()
print(prumer_vek)


def prvni_cifra(psc):
    return int(str(psc)[0])

obyvatele["PSČ_začátek"] = obyvatele["PSČ"].apply(prvni_cifra)
#print(obyvatele.head(5))

psc = pd.read_csv("psc.csv")

nova = pd.merge(obyvatele, psc, how="left", on="PSČ_začátek")
#print(nova.head(5))


regiony = nova.groupby("název")["název"].count()
print(regiony)

print(regiony.keys())
print(regiony.array)

fig, ax = plt.subplots()

ax.set_title("Počet obyvatel v regionu")
ax.set_xlabel("region")
ax.set_ylabel("počet obyvatel")

ax.bar(regiony.keys(), regiony.array)


plt.show()
