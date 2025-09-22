
""" 
Ejercicio 1
Generar un rango con una función
Crea una función rango (desde, hasta, intervalo)
que retorne una lista de números, tal como la
función incorporada range(), aunque según el
intervalo especificado.
No puedes usar la función range() para resolver
este ejercicio.
Por ejemplo, el siguiente código:
lista = rango(1, 10, 2)
print(lista)

debe imprimir:
[1, 3, 5, 7, 9]
Puesto que se genera una lista desde 1 hasta 10
con un intervalo de 2.
 """

def rango(desde, hasta, intervalo):
    lista = []
    numero = desde
    while numero < hasta:
        lista.append(numero)
        numero += intervalo
    return lista

# Prueba de la función
lista = rango(1, 10, 2)
print(lista)
# Salida esperada: [1, 3, 5, 7, 9]