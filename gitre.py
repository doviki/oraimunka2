#1. Írjon programot, mely kiírja a képernyőre a 1-10 ig a számok reciprokát!

for szam in range (1,11,1):
    reciprok=1/szam
    print(reciprok)

#2. írj programot, mely beolvassa a hatvány alapját és a kitevőt, és kiírja a hatványértéket!

alap=int(input("Add meg a hatvány alapot: "))
kitevo=int(input("Add meg a hatvány kitevőt: "))
hatvanyertek=alap**kitevo
print(hatvanyertek)

#3. Írj programot, ami csak pozitív számot hajlandó beolvasni.

a=int(input("Adj meg egy számot: "))
if a>0:
    print(a)
else:
    print("A szám negatív")
    



