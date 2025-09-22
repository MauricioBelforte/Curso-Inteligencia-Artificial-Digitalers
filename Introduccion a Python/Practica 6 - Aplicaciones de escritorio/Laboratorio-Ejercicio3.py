
""" Ejercicio 3
Dado
Genera un programa de consola que tenga un
menú y permita generar números aleatorios
entre 1 y 6, como si fuera un dado.
El “Menú” debe contener las opciones:
1. Tirar dado.
2. Salir
 """

import random
def tirar_dado():
    return random.randint(1, 6)
def mostrar_menu():
    print("Menú:")
    print("1. Tirar dado")
    print("2. Salir")
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1 o 2): ")
    if opcion == '1':
        resultado = tirar_dado()
        print(f"Has tirado el dado y ha salido: {resultado}")
    elif opcion == '2':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")
# Fin del programa

# Prueba de la función
resultado = tirar_dado()
print(f"Resultado de tirar el dado: {resultado}")
# Salida esperada: un número entre 1 y 6
