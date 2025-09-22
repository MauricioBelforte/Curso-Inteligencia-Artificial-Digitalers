
""" Ejercicio 6: Lista de números aleatorios
Haz una lista que contenga 10 números
aleatorios entre 10 y 50. En pantalla deben
aparecer los números separados por un guión
medio.
Puedes guiarte con el ejemplo de la derecha.
 """

import random
# Generar una lista de 10 números aleatorios entre 10 y 50
numeros_aleatorios = [random.randint(10, 50) for _ in range(10)]


print("-".join(map(str, numeros_aleatorios)))
# Salida esperada: Una lista de 10 números aleatorios entre 10 y 50, separados por guiones medios




#.join() Une los elementos de una lista en un solo string, separados por el string especificado
# Puedes usar join() para crear una cadena a partir de una lista de cadenas, especificando un separador.

# map() Aplica una función a cada elemento de la lista y devuelve una nueva lista con los resultados
# Puedes usar map() para transformar los elementos de una lista sin necesidad de un bucle explícito.

# str Convierte un valor a una cadena de texto