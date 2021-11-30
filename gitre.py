#1. Írjon programot, mely kiírja a képernyőre a 1-10 ig a számok reciprokát!

for szam in range (1,11,1):
    reciprok=1/szam
    print(reciprok)

#2. írj programot, mely beolvassa a hatvány alapját és a kitevőt, és kiírja a hatványértéket!

#3. Írj programot, ami csak pozitív számot hajlandó beolvasni.

alap=int(input("Add meg a hatvány alapot: "))
kitevo=int(input("Add meg a hatvány kitevőt: "))
hatvanyertek=alap**kitevo
print(hatvanyertek)
