# Matrices

# En resumen, son listas que contienen otras listas.
# Una lista se llama matriz cuando contiene otras listas como elementos. 
# Se usan para representar datos en dos dimensiones, como tablas o cuadrículas.

# Ejemplo de una matriz 2x2
m = [[10,20],[30,40]]

print(type(m))
# <class 'list'>
print("Matriz 2x2 de números enteros: ", m)
# [[10, 20], [30, 40]]


# Ejemplo de una matriz 2x3
mi_lista = [[3.14, "Hola mundo"], [True, False, -5]]
print("Matriz 2x3 con diferentes tipos de datos: ", mi_lista)
# El codigo crea una lista con dos elementos, que a su vez son listas.
# Se accede a los elementos indicando, entre corchetes, primero la fila y luego la columna.

print("La primer fila de la matriz es: ",mi_lista[0])
# [3.14, 'Hola mundo']
print("La segunda fila de la matriz es: ",mi_lista[1])
# [True, False, -5]
print(mi_lista[0][0])
# 3.14
print(mi_lista[0][1])
# 'Hola mundo'
print(mi_lista[1][0])
# True
print(mi_lista[1][1])
# False
print(mi_lista[1][2])
# -5