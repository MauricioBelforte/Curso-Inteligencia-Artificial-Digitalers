
""" Ejercicio 2
Desarrolla una función que reciba una lista con
números enteros y devuelva en una matriz:
● Como primer elemento, una lista con los
números pares.
● Como segundo elemento, una lista de los
números impares de la lista recibida.
 """

def separar_pares_impares(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    return [pares, impares]

# Prueba de la función
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = separar_pares_impares(lista_numeros)
print(resultado)  # Salida esperada: [[2, 4, 6, 8, 10], [1, 3, 5, 7, 9]]
# Fin del programa