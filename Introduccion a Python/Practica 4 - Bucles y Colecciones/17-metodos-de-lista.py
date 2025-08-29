# Listas en Python
# Las listas es una coleccion ordenada de objetos (de cualquier tipo de dato básicos) agrupados en una misma variable. Cada uno de estos objetos se conoce como elemento. 

numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

alumnos = ["Ana", "Luis", "Pedro", "Maria"]

datos = [3.14, True ,-1 , False, "Hola mundo"]


# Las listas son colecciones ordenadas y mutables de elementos. 
# Puedes acceder a los elementos por su índice, que comienza en 0.
# A cada uno de los elementos se le asigna un índice, que es la posición en la que se encuentra en la lista, empezando del 0.


print(numeros_primos[0])  # Imprime el primer elemento de la lista numeros_primos
print(alumnos[2])         # Imprime el tercer elemento de la lista alumnos
print(datos[4])           # Imprime el quinto elemento de la lista datos

# Además, puedes modificar los elementos de una lista, agregar nuevos elementos o eliminar existentes.

print()



# .append() Para agregar un elemento al final de la lista
print(".append()")
numeros_primos.append(31)  # Agrega el número 31 al final de la lista numeros_primos
print(numeros_primos)      # Imprime la lista actualizada de numeros_primos
print()


# .insert() Para agregar un elemento en una posicion especifica
print(".insert()")
alumnos.insert(2, "Carlos")  # Inserta "Carlos" en la posición 2 de la lista alumnos
print(alumnos)               # Imprime la lista actualizada de alumnos
print()




# .extend() Para agregar varios elementos a la lista
print(".extend()")
numeros_primos.extend([37, 41])  # Agrega múltiples elementos al final de la lista numeros_primos
print(numeros_primos)             # Imprime la lista actualizada de numeros_primos
# Puede ser cualquier objeto iterable 
# objeto_iterable: lista, string, tupla
# nombre_lista.extend(objeto_iterable)
print()




# .pop() Para eliminar y devolver el ultimo elemento de la lista
print(".pop()")
ultimo_numero = numeros_primos.pop()  # Elimina y devuelve el último elemento de la lista numeros_primos
print("Imprime el numero que devolvio el pop: ",ultimo_numero) # Imprime el último número eliminado
print(numeros_primos)             # Imprime la lista actualizada de numeros_primos
print()




# .clear() Para eliminar todos los elementos de la lista
print(".clear()")
numeros_primos.clear()  # Elimina todos los elementos de la lista numeros_primos
print(numeros_primos)  # Imprime la lista vacía
print()


# .len() Para obtener la longitud de la lista
print(".len()")
print("Longitud de numeros_primos:", len(numeros_primos))  # Imprime la longitud de la lista numeros_primos
print("Longitud de alumnos:", len(alumnos))                # Imprime la longitud de la lista alumnos
print()


#.remove() Para eliminar un elemento especifico de la lista, lo busca y lo elimina
print(".remove()")
datos.remove(False)  # Elimina el valor False de la lista datos
print(datos)         # Imprime la lista actualizada de datos
print()


# Otra forma de eliminar elementos: del Para eliminar un elemento en una posicion especifica
print("del")
del alumnos[1]  # Elimina el elemento en la posición 1 de la lista alumnos
print(alumnos)  # Imprime la lista actualizada de alumnos
print()




