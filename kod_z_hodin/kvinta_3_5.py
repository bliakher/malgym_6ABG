
vsazene = 5
vygen = 6

sazka = 50
penize = 500

if vsazene > vygen:
    print("Vyhra")
    penize += sazka

elif vsazene == vygen:
    print("Remiza")
    penize += sazka * 0.5

elif vsazene < vygen:
    print("Prohra")
    penize -= sazka

print("Vsadili jste:", vsazene)
print("Padlo:", vygen)
print(penize)


# rekurze

# funkce - volani

def funkce(): # mam funkci - funkce - na radku 29
    print("Ahoj")


print("Zacatek")
funkce() # skoc na radek 29
print("Konec")


print("Zacatek2")
funkce() # skoc na radek 29
print("Konec2")

i = 100
while i < 10:
    i += 1
    
print()

# volaci zasobnik - call stack




    
