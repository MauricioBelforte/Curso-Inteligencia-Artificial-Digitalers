""" 
Ejercicio 1
Crea un programa para estudiantes que cumpla con
esta tarea: cada alumno debe ingresar su nota y, de
acuerdo con eso, el sistema debe mostrar un mensaje
que diga:
● “Excelente” si la nota es un 10.
● “Muy bien” si está entre 7 y 9.
● “Bien” si está entre un 4 y un 6.
● “Mal” si está entre 0 y 3.
● Si la nota no corresponde a ninguno de estos
valores, mostrar “La nota ingresada es incorrecta”. 
"""

nota = int(input("Ingrese su nota (0-10): "))
if nota == 10:
    print("Excelente")
elif 7 <= nota <= 9:
    print("Muy bien")
elif 4 <= nota <= 6:
    print("Bien")
elif 0 <= nota <= 3:
    print("Mal")
else:
    print("La nota ingresada es incorrecta")    

