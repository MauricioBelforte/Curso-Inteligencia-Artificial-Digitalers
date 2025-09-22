
""" 
Ejercicio 4: Palíndromo

Crea una función que devuelva Verdadero si una
lista de elementos es palíndroma (se lee igual en
un sentido que en otro). En caso contrario, debe
devolver Falso.
Por ejemplo:

es_palindromo ([3, 2, 3]) → True
es_palindromo(["m", 2, 2, "m"]) → True

"""

def es_palindromo(lista):
    return lista == lista[::-1]

print("Es palíndromo [3, 2, 3]:", es_palindromo([3, 2, 3]))
print("Es palíndromo ['m', 2, 2, 'm']:", es_palindromo(['m', 2, 2, 'm']))
print("Es palíndromo [1, 2, 3]:", es_palindromo([1, 2, 3]))
print("Es palíndromo ['a', 'b', 'a']:", es_palindromo(['a', 'b', 'a']))
print("Es palíndromo [1, 2, 2, 1]:", es_palindromo([1, 2, 2, 1]))

# Otra forma de hacerlo sin usar slicing
def es_palindromo_v2(lista):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda < derecha:
        if lista[izquierda] != lista[derecha]:
            return False
        izquierda += 1
        derecha -= 1
    return True

print("\nUsando la segunda función:")
print("Es palíndromo [3, 2, 3]:", es_palindromo_v2([3, 2, 3]))
print("Es palíndromo ['m', 2, 2, 'm']:", es_palindromo_v2(['m', 2, 2, 'm']))
print("Es palíndromo [1, 2, 3]:", es_palindromo_v2([1, 2, 3]))
print("Es palíndromo ['a', 'b', 'a']:", es_palindromo_v2(['a', 'b', 'a']))
print("Es palíndromo [1, 2, 2, 1]:", es_palindromo_v2([1, 2, 2, 1]))
