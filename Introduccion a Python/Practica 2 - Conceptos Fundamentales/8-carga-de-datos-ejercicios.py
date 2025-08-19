# Programa que imprime el resto de una division

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



# Ingrese el dividendo
dividendo = int(input("Ingrese el dividendo: "))
# Ingrese el divisor
divisor = int(input("Ingrese el divisor: "))

# Calcular el resto de la división
resto = dividendo % divisor
# Imprimir el resultado
print(f"El resto de la división {dividendo} / {divisor} es: {resto}")



