""" 
Etapa 3
La lista de alumnos creada en el módulo anterior
ahora debe ser un diccionario, en donde las
claves serán nombres de alumnos y los valores
sus respectivas cantidades de cursos.
Para esto se debe modificar el código de las
opciones 1 y 2 (agregar un nuevo alumno y ver la
lista de alumnos).
La tercera opción será “Ver la cantidad de cursos
de un alumno”. Deberá solicitar el nombre de un
alumno e imprimir en pantalla el número de
cursos que tiene asociados como clave. La cuarta
opción es la de salir, como en la versión anterior.  
"""

"""
CONTEXTO

Etapa 2
Menú
Continúa el desarrollo del código incluyendo estos requisitos:
a. Para ingresar al menú, solicitar nombre de usuario y contraseña. 
Solo si el usuario es “admin” y la contraseña es “uni123”, se muestra el menú. 
De lo contrario, se indica “Usuario y/o contraseña incorrecta”.
Ingrese nombre de usuario: admin
Ingrese la contraseña: uni123



usuario2 = input("Ingrese nombre de usuario: ")
contrasena2 = input("Ingrese la contraseña: ")

if usuario2 == "admin" and contrasena2 == "uni123":
    print("Bienvenido al menú.")
else:
    print("Usuario y/o contraseña incorrecta.")




b. Una vez ingresado, mostrar el siguiente menú:
El sistema debe pedir una opción infinitamente hasta que el usuario escriba “3”.
Ingrese el número de la operación que desea ejecutar:
1 - Añadir un alumno a la lista.
2 - Ver la lista de alumnos.
3 - Salir. 

Si se presiona 1, debe solicitar el nombre de un alumno y la cantidad de cursos en la que se encuentra inscripto.
Estos dos valores deben almacenarse como una lista de dos elementos (el nombre y la cantidad de cursos como un número entero) en una lista de alumnos.
● Opción 1:
Ingrese el nombre del alumno: Pablo
Ingrese la cantidad de cursos: 3
¡El alumno fue añadido a la lista!

Si se presiona 2, recorrer la lista de alumnos y mostrar por pantalla.
● Opción 2:
Lista de alumnos:
Pablo - 3 cursos

Si presiona 3, saludar al usuario y salir del sistema.
● Opción 3:

¡Gracias por utilizar el programa!

Si el usuario presiona cualquier otro número, se debe informar que la opción no es correcta y volver a mostrar el menú.
● Opción distinta de 1, 2 o 3:
La opción ingresada no es correcta, vuelva a intentarlo.




usuario = input("Ingrese nombre de usuario: ")
contrasena = input("Ingrese la contraseña: ")

if usuario == "admin" and contrasena == "uni123":
    print("Bienvenido al menú.")
    lista_alumnos = []
    while True:
        print("Ingrese el número de la operación que desea ejecutar:")
        print("1 - Añadir un alumno a la lista.")
        print("2 - Ver la lista de alumnos.")
        print("3 - Salir.")
        opcion = input()
        if opcion == "1":
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            cantidad_cursos = int(input("Ingrese la cantidad de cursos: "))
            lista_alumnos.append([nombre_alumno, cantidad_cursos])
            print("¡El alumno fue añadido a la lista!")
        elif opcion == "2":
            print("Lista de alumnos:")
            for alumno in lista_alumnos:
                print(f"{alumno[0]} - {alumno[1]} cursos")
        elif opcion == "3":
            print("¡Gracias por utilizar el programa!")
            break
        else:
            print("La opción ingresada no es correcta, vuelva a intentarlo.")
else:
    print("Usuario y/o contraseña incorrecta.")

"""

# Etapa 3
usuario = input("Ingrese nombre de usuario: ")
contrasena = input("Ingrese la contraseña: ")

if usuario == "admin" and contrasena == "uni123":
    print("Bienvenido al menú.")
    diccionario_alumnos = {}
    while True:
        print("Ingrese el número de la operación que desea ejecutar:")
        print("1 - Añadir un alumno a la lista.")
        print("2 - Ver la lista de alumnos.")
        print("3 - Ver la cantidad de cursos de un alumno.")
        print("4 - Salir.")
        opcion = input()
        if opcion == "1":
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            cantidad_cursos = int(input("Ingrese la cantidad de cursos: "))
            diccionario_alumnos[nombre_alumno] = cantidad_cursos
            print("¡El alumno fue añadido a la lista!")
        elif opcion == "2":
            print("Lista de alumnos:")
            for alumno, cursos in diccionario_alumnos.items():
                print(f"{alumno} - {cursos} cursos")
        elif opcion == "3":
            nombre_alumno = input("Ingrese el nombre del alumno: ")
            if nombre_alumno in diccionario_alumnos:
                print(f"{nombre_alumno} está inscrito en {diccionario_alumnos[nombre_alumno]} cursos.")
            else:
                print(f"El alumno {nombre_alumno} no está en la lista.")
        elif opcion == "4":
            print("¡Gracias por utilizar el programa!")
            break
        else:
            print("La opción ingresada no es correcta, vuelva a intentarlo.")
else:
    print("Usuario y/o contraseña incorrecta.")

    