# Ejemplo de variables y operaciones

# Donde la variable es un nombre cualquiera (escrito, por convención, siempre en minúscula) 

""" 
La sintaxis para crear una variable es:
variable = expresión 
"""

# Tipos de variables

# Variables string
nombre= "Juan"

# Variables numéricas
edad= 30
altura= 1.75

edad_en_5_años = edad + 5
es_mayor_de_edad = edad >= 18

mensaje = f"Nombre: {nombre}, Edad: {edad}, Altura: {altura}"

print(mensaje)
print(f"Edad en 5 años: {edad_en_5_años}")
print(f"¿Es mayor de edad? {'Sí' if es_mayor_de_edad else 'No'}")


# Variables booleanas
#Las variables booleanas representan valores lógicos de verdad, limitándose únicamente a dos posibles estados: verdadero (True) o falso (False).

esta_lloviendo = True
tiene_paraguas = False
es_fin_de_semana = True

print(f"¿Está lloviendo? {'Sí' if esta_lloviendo else 'No'}")
print(f"¿Tiene paraguas? {'Sí' if tiene_paraguas else 'No'}")
print(f"¿Es fin de semana? {'Sí' if es_fin_de_semana else 'No'}")



a = 200
b = 33

if a > b:
    print("a es mayor que b")
else:
    print("a no es mayor que b")

