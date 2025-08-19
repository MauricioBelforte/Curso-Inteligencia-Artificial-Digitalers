# Conversion entre fechas

# Importar el módulo datetime


from datetime import datetime

# Fecha actual
fecha_actual = datetime.now()
print("Fecha actual:", fecha_actual)

# Donde ver mas informacion sobre fechas
# https://www.geeksforgeeks.org/python/python-convert-string-to-datetime-and-vice-versa/

# Ejercicio1
#  Convertir una cadena de texto a fecha
print("\nEjercicio 1: Convertir una cadena de texto a fecha")
fecha_str = "2023-10-11 15:30:00"
print("Cadena de fecha:", fecha_str)

# Convertir la cadena a un objeto datetime
fecha_convertida = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
print("Fecha convertida desde cadena:", fecha_convertida)


# Ejercicio 2
print("\nEjercicio 2: Convertir una cadena de fecha con formato personalizado")

s= '2021/05/25'
formato = '%Y/%m/%d'

res = datetime.strptime(s, formato)
print("Fecha convertida desde cadena con formato personalizado:", res)

res2 = datetime.strptime(s, formato).date()
print("Fecha convertida desde cadena con formato personalizado (solo fecha):", res2)