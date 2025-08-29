
""" 
Ejercicio 4

A la derecha, vemos un diagrama de flujo de
cómo se hace para calcular un año bisiesto. La
idea es llevar este algoritmo a código Python.
 """
# mod significa “módulo”, es la división modular %.

# Introduccion a Python/Practica 4 - Bucles y Colecciones/31-Desafio-ejercicio4.png

a = int(input("Ingrese un año: "))
if (a % 400 == 0): 
    print(f"El año {a} es bisiesto.")
elif (a % 4 == 0 ) and (a % 100 != 0) :
    print(f"El año {a} es bisiesto.")
else:
    print(f"El año {a} no es bisiesto.")
