import pandas as pd

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
