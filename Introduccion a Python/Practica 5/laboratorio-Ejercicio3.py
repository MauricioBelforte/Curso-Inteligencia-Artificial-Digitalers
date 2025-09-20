""" 
Ejercicio 3: Generar un rango con una función

Crea una función rango(desde, hasta,
intervalo) que retorne una lista de números, tal
como la función incorporada range(), aunque
según el intervalo especificado.

Por ejemplo, el siguiente código:
lista = rango(1, 10, 2)
print(lista)

Debe imprimir: [1, 3, 5, 7, 9], puesto que se
genera una lista desde 1 hasta 10 con un
intervalo de 2.
 """
def rango(desde, hasta, intervalo):
    lista = []
    for numero in range(desde, hasta, intervalo):
        lista.append(numero)
    return lista

lista = rango(1, 10, 2)
print("\nRango de 1 a 10 con intervalo 2:")
print(lista)

lista = rango(5, 20, 3)
print("\nRango de 5 a 20 con intervalo 3:")
print(lista)

