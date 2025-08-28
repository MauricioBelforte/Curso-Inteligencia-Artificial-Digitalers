# Laboratorio 

# **Ejercicio 1**

# 1. Crea un programa que permita ingresar dos cadenas vía la consola y las compare. Luego, debe imprimir un mensaje en caso de que sean iguales y otro en caso de que sean diferentes.

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

if cadena1 == cadena2:
    print("Las cadenas son iguales.")
else:
    print("Las cadenas son diferentes.")


# 2. Crea un programa que solicite el nombre de un alumno a través de la consola, y luego chequee que no esté vacío. En caso de estarlo, tiene que imprimir un mensaje de error; caso contrario, deberá imprimir un mensaje indicando que se ingresó correctamente.

nombre_alumno = input("Ingrese el nombre del alumno: ")

if nombre_alumno == "":
    print("Error: El nombre del alumno no puede estar vacío.")
else:
    print("El nombre del alumno se ingresó correctamente.")

# 3. Pedir la edad por teclado y comparar si es mayor o menor de edad. No olvidar que, para poder comparar el ingreso, debe ser convertido a `int`, ya que el usuario ingresa un número entero.

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")  