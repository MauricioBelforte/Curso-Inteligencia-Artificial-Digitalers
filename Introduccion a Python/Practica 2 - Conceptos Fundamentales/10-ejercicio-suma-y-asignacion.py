# Programa que calcula la suma de dos números y los asigna a una variable

""" 
Python no permite operaciones directas entre tipos incompatibles, 
demandando conversiones explicitas mediante funciones como:
- int(): Convierte un número decimal, booleano o una cadena que representa un entero en un número entero (int).
Ejemplo: int('42') devuelve 42, int(3.9) devuelve 3.
- str(): Convierte cualquier tipo de dato (como números, booleanos o listas) en una cadena de texto.
Ejemplo: str(123) devuelve '123'.
- float(): Convierte enteros, booleanos o cadenas numéricas en un número decimal (float).
Ejemplo: float('3.14') devuelve 3.14, float(10) devuelve 10.0.

"""

# 📥 input() en Python espera que el usuario escriba algo por teclado y lo devuelve como una cadena de texto (str).


# Ingrese el primer número
numero1 = int(input("Ingrese el primer número: "))

# Ingrese el segundo número
numero2 = int(input("Ingrese el segundo número: "))

# Calcular la suma de los dos números
suma = numero1 + numero2

# Imprimir el resultado
print(f"La suma de {numero1} y {numero2} es: {suma}")


