""" 
Etapa 1

Una universidad desea crear un programa para contabilizar los cursos que tiene cada alumno. 
Para ello, se debe realizar primero una aplicación de consola donde solo puede manejar el usuario con
nombre “admin” y contraseña “uni123”.
Una vez ingresado al sistema, debe aparecer un menú de opciones para dar de alta nuevos alumnos con la cantidad de cursos, 
ver listados, ver cursos por alumnos.
Para finalizar, el sistema se debe mostrar en una interfaz gráfica.
 """


""" 
Consigna
Crea un programa que solicite el nombre de un alumno a
través de la consola y la cantidad de cursos, y luego
muestre por pantalla esa información. 
"""



nombre_alumno = input("Ingrese el nombre del alumno: ")
cantidad_cursos = input("Ingrese la cantidad de cursos: ")

print(f"El alumno {nombre_alumno} tiene {cantidad_cursos} cursos.")
