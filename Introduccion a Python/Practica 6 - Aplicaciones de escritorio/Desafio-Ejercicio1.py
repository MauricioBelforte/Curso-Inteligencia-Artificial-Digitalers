
""" Ejercicio 1
Escribe una función que sirva para multiplicar
cada elemento de una lista numérica por un
valor (ambos deben ser parámetros de función);
y devuelva la nueva lista con cada elemento en
su respectiva posición, pero ya multiplicado. """

def multiplicar_lista(lista, valor):
    nueva_lista = [elemento * valor for elemento in lista]
    return nueva_lista

# Prueba de la función
lista_original = [1, 2, 3, 4, 5]
valor_multiplicacion = 2
nueva_lista_resultante = multiplicar_lista(lista_original, valor_multiplicacion)
print(nueva_lista_resultante)
""" Salida esperada: [2, 4, 6, 8, 10] """
# Fin del programa