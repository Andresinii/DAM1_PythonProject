x = int(input("Introduce un número: "))
y = int(input("Introduce otro: "))

if x >= y: 
    numIni = x
    numFin = y - 1
else:
    numIni = y
    numFin = x - 1

for i in (numIni,numFin):
    print(str(i) + "")
    if numIni != numFin:
        print ("-")