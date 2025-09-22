""" 

Etapa 4
1. Migra las tres funcionalidades del programa
(agregar alumno, ver la cantidad de cursos de
un alumno y ver la lista completa) a una
aplicación de escritorio. La información se
seguirá mostrando en la consola.
2. Con botones se debe poder ver la lista de
alumnos, agregar un nuevo alumno, ver
cantidad de cursos y salir.

El botón “Ver lista de alumnos” debe mostrar
la lista de los alumnos en la consola.
● “Agregar a la lista” debe agregar un nuevo
alumno al diccionario con el nombre y la
cantidad de cursos ingresados en las cajas de
texto correspondientes.
● “Ver cantidad de cursos” debe mostrar el
número de cursos asociados al nombre
ingresado en la primera caja de texto.
 """

""" CONTEXTO:
 
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
 Opción 1:
Ingrese el nombre del alumno: Pablo
Ingrese la cantidad de cursos: 3
¡El alumno fue añadido a la lista!

Si se presiona 2, recorrer la lista de alumnos y mostrar por pantalla.
 Opción 2:
Lista de alumnos:
Pablo - 3 cursos

Si presiona 3, saludar al usuario y salir del sistema.
 Opción 3:

¡Gracias por utilizar el programa!

Si el usuario presiona cualquier otro número, se debe informar que la opción no es correcta y volver a mostrar el menú.
 Opción distinta de 1, 2 o 3:
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

"""

# Etapa 4
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Alumnos")
ventana.geometry("400x300")
ventana.resizable(False, False)
ventana.configure(bg="#f0f0f0")
ventana.eval('tk::PlaceWindow . center')  # Centrar la ventana en la pantalla   
# Diccionario para almacenar los alumnos
diccionario_alumnos = {}
# Función para agregar un alumno
def agregar_alumno():
    nombre_alumno = entrada_nombre.get()
    try:
        cantidad_cursos = int(entrada_cursos.get())
        diccionario_alumnos[nombre_alumno] = cantidad_cursos
        print("¡El alumno fue añadido a la lista!")
    except ValueError:
        print("Por favor, ingrese un número válido para la cantidad de cursos.")
# Función para ver la lista de alumnos
def ver_lista_alumnos():    
    print("Lista de alumnos:")
    for alumno, cursos in diccionario_alumnos.items():
        print(f"{alumno} - {cursos} cursos")
# Función para ver la cantidad de cursos de un alumno
def ver_cantidad_cursos():
    nombre_alumno = entrada_nombre.get()
    if nombre_alumno in diccionario_alumnos:
        print(f"{nombre_alumno} está inscrito en {diccionario_alumnos[nombre_alumno]} cursos.")
    else:
        print(f"El alumno {nombre_alumno} no está en la lista.")    
# Crear etiquetas y cajas de texto
etiqueta_nombre = tk.Label(ventana, text="Nombre del Alumno:", bg="grey")
etiqueta_nombre.pack(pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)
etiqueta_cursos = tk.Label(ventana, text="Cantidad de Cursos:", bg="grey")
etiqueta_cursos.pack(pady=5)
entrada_cursos = tk.Entry(ventana)
entrada_cursos.pack(pady=5)
# Crear botones
boton_agregar = tk.Button(ventana, text="Agregar Alumno", command=agregar_alumno, bg="#007BFF", fg="white")
boton_agregar.pack(pady=5)
boton_ver_lista = tk.Button(ventana, text="Ver Lista de Alumnos", command=ver_lista_alumnos, bg="#28A745", fg="white")
boton_ver_lista.pack(pady=5)
boton_ver_cursos = tk.Button(ventana, text="Ver Cantidad de Cursos", command=ver_cantidad_cursos, bg="#17A2B8", fg="white")
boton_ver_cursos.pack(pady=5)
# Iniciar el bucle principal de la aplicación
ventana.mainloop()
# Fin del programa
