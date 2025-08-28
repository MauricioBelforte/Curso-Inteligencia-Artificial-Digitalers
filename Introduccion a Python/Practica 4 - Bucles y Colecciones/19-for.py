# Bucle for en Python
# Los bucles for se aplican siempre sobre listas.

numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# El bucle for se utiliza para iterar sobre una secuencia (como una lista, tupla o cadena) y ejecutar un bloque de código para cada elemento de la secuencia.
for numero in numeros_primos:  # Itera sobre cada elemento de la lista numeros_primos
    print("Numero primo:", numero)  # Imprime el número primo actual

alumnos = ["Ana", "Luis", "Pedro", "Maria"]

for alumno in alumnos:
    print("Alumno: ",alumno)


# También puedes usar el bucle for para iterar sobre un rango de números.
for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
    print("Numero primo: ",i)

# También puedes usar la función range() para generar una secuencia de números.
for i in range(5):  # Itera desde 0 hasta 4
    print("Número:", i)  # Imprime el número actual en la iteración

# Por ejemplo, para imprimir los números del 1 al 10:
for i in range(1, 11):
 print(i)

# O para iterar sobre un rango específico
for i in range(1, 10, 2):  # Itera desde 1 hasta 9 con un paso de 2
    print("Número impar:", i)  # Imprime el número impar actual 


# Otros ejemplos:

# Imprimir los nombres de los clientes
clientes = ["Rodolfo", "Emilia", "Jorge", "Juana"]
for cliente in clientes:
    print("Ingresó al sistema el cliente: " + cliente)

# Imprimir el cuadrado de los números en una lista
for numero in [2, 1, 3, 5]:
    print(numero ** 2)

# Imprimir los números del 100 al 500
for numero in range(100, 501):
    print(numero)