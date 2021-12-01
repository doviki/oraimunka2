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
if a>=0:
    print(a)
else:
    print("A szám negatív")
    

#4. írj programot, mely bekér két számot és eldönti mennyi a távolságuk a számegyenesen!

a=int(input("Adj meg egy számot: "))
b=int(input("Adj meg még egy számot: "))
x=a-b

if a<0:
    print("{0} két szám távolsága a számegyensen".format(-(x)))
else:       
    print("{0} két szám távolsága a számegyensen".format(x))

#5. írj programot, mely addig kér számokat a billentyűzetről amig összegük kisebb mint 100!

