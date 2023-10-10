""" PSEUDOCÓDIGO.
Inicio
    Lee n1
    Lee n2
    
    Si (n2 == n1) entonces
        Escribe "ERROR"
    sino    
        Si (n1<n2) entonces
            Escribe "El primer número es el menor."
        sino
            Escribe "El segundo número es el menor.")

Fin
"""















n1 = int(input("Introduzca un número: "))
n2 = int(input("Introduzca otro: "))

if n1<n2:
    print("El primer número ("+ str(n1)+") es el menor.")
elif n2<n1:
    print("El segundo número ("+ str(n2)+") es el menor.")
    