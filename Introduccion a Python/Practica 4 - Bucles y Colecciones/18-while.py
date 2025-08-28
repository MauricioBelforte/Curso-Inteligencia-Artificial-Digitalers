# Bucle while en Python

# El bucle while ejecuta un bloque de código mientras una condición sea verdadera.

contador = 0  # Inicializamos el contador
while contador < 5:  # Mientras el contador sea menor que 5
    print("Contador:", contador)  # Imprime el valor actual del contador
    contador += 1  # Incrementa el contador en 1
print("Bucle terminado, contador:", contador)  # Imprime el valor final del contador


# El segundo método para finalizar un bucle es vía la palabra reservada break. 

a = 1
while True:
    if a < 5:
        print("Hola mundo")
        a = a + 1
    else:
        break


# Otros ejemplos:

cant = 1
while cant <= 5:
    print("Servidor encendido")
    cant = cant + 1


cant = 1
while True:
    if cant <= 5:
        print("Servidor encendido")
    else:
        break
    cant = cant + 1
print("Servidor apagado")


# Menu con while True y break

while True:
 print(" *** MENÚ ***")
 print("1 - Alta de usuario")
 print("2 - Modificar usuario")
 print("3 - Eliminar usuario")
 print("4 - Listar")
 print("5 - Salir")
 opcion = int(input("Ingrese una opción: "))
 if opcion == 1:
     print("SE CARGA UN NUEVO USUARIO")
 elif opcion == 2:
    print("SE MODIFICA UN USUARIO EXISTENTE")
 elif opcion == 3:
     print("SE ELIMINA UN USUARIO EXISTENTE")
 elif opcion == 4:
    print("SE MUESTRA POR PANTALLA UN LISTADO DE CLIENTES")
 elif opcion == 5:
    print("Gracias por utilizar el sistema")
    break
 else:
     print("Opción incorrecta")
