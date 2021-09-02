# reseni s dvemi pruchody posloupnosti

list = []
cislo = 0
while cislo != -1:
    cislo = int(input())
    list.append(cislo)

nejvetsi = list[0]
list2 = []

for cislo in list:
    if cislo > nejvetsi:
        nejvetsi = cislo

for cislo in list:
    if cislo != nejvetsi:
        list2.append(cislo)

nejvetsi2 = list2[0]

for cislo2 in list2:
    if cislo2 > nejvetsi2:
        nejvetsi2 = cislo2

print(nejvetsi2)

# lepsi reseni s jednim pruchodem

cislo = 0
nejvetsi_cislo = 0
druhe_nejvetsi_cislo = 0

while cislo != -1:
    cislo = int(input("číslo: "))
    if cislo > nejvetsi_cislo:
        druhe_nejvetsi_cislo = nejvetsi_cislo
        nejvetsi_cislo = cislo
    else:
        if cislo > druhe_nejvetsi_cislo:
            druhe_nejvetsi_cislo = cislo
print("druhé největší číslo: ", druhe_nejvetsi_cislo)

