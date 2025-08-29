""" Ejercicio 5
Escribe un programa que permita crear una lista
de nombres.
Para ello, el programa debe pedir un número y
luego solicitar esa cantidad de nombres para
crear la lista. Por último, el programa tiene que
mostrar la lista creada.
 """

cantidad_nombres = int(input("¿Cuántos nombres desea ingresar? "))
nombres = []
for elemento in range(cantidad_nombres):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
print("La lista de nombres es:", nombres)

# Otra forma de hacerlo con while

cantidad_nombres2 = int(input("¿Cuántos nombres desea ingresar? "))
nombres2 = []
contador = 0
while contador < cantidad_nombres2:
    nombre2 = input("Ingrese un nombre: ")
    nombres2.append(nombre2)
    contador += 1
print("La lista de nombres es:", nombres2)

