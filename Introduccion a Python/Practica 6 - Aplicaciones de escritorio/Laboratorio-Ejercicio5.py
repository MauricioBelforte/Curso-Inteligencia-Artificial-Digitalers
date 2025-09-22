
""" Ejercicio 5: Adivinar números
Escribe un programa donde el usuario debe
adivinar un número oculto (generado
aleatoriamente) en un rango entre 10 y 40, en 5
intentos.
Opcional: El programa puede guiar al usuario
indicando si elnúmero es mayor o menor.
 """

import random

numero_oculto = random.randint(10, 40)
intentos = 5

while intentos > 0:
    print(f"Tienes {intentos} intentos restantes.")
    intento = int(input("Adivina el número (entre 10 y 40): "))
    if intento < 10 or intento > 40:
        print("Por favor, ingresa un número dentro del rango especificado.")
        continue
    if intento == numero_oculto:
        print("¡Felicidades! ¡Adivinaste el número!")
        break
    elif intento < numero_oculto:
        print("El número oculto es mayor.")
    else:
        print("El número oculto es menor.")
    intentos -= 1

if intentos == 0:
    print(f"Lo siento, has agotado tus intentos. El número oculto era {numero_oculto}.")
# Fin del programa

# Prueba del programa
print(f"Número oculto para pruebas: {numero_oculto}")