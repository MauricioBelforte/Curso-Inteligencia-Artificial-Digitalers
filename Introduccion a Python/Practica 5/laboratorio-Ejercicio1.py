""" 
Ejercicio 1: Estrellas

Escribe una función mostrar_estrellas(cantidad)
que muestre tantos * como indica cantidad,
comenzando con un *.
Por ejemplo:
mostrar_estrellas(5)
*
**
***
****
*****
"""

def mostrar_estrellas(cantidad):
    for i in range(1, cantidad + 1):
        print('*' * i)



print("Con cantidad 5:")
mostrar_estrellas(5)

print("\nCon cantidad 3:")
mostrar_estrellas(3)

print("\nCon cantidad 7:")
mostrar_estrellas(7)
