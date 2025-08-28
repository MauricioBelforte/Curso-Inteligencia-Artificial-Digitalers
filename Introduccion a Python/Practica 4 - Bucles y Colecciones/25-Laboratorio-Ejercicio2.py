# **Ejercicio 2**

# 1. Con un bucle `while`, incrementar una variable entera de uno en uno (desde 0 hasta 9, sin incluir el 10). Mostrar por pantalla el resultado en cada vuelta.

contador = 0
while contador < 10:
    print("Contador:", contador)
    contador += 1  # Incrementa el contador en 1

# 2. Pedir por teclado el nombre de usuario. Si está vacío, volver a pedirlo hasta que se ingrese un nombre válido. Luego, saludar al usuario.

nombre_usuario = input("Ingrese su nombre de usuario: ")
while nombre_usuario == "":
    print("Error: El nombre de usuario no puede estar vacío.")
    nombre_usuario = input("Ingrese su nombre de usuario: ")

print("¡Hola,", nombre_usuario, "! Bienvenido.")


