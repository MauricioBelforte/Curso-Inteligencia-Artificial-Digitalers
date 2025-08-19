# Operadores logicos en Python

# Los operadores lógicos se utilizan para combinar expresiones booleanas y devolver un valor booleano (True o False).
# Los operadores lógicos más comunes son AND, OR y NOT.
# Estos operadores son útiles en estructuras de control como condicionales y bucles.


# Operadores lógicos básicos

# AND (y lógico)
a = True
b = False
resultado_and = a and b  # Devuelve True solo si ambos son True
print("Resultado AND:", resultado_and)


# OR (o lógico)
resultado_or = a or b  # Devuelve True si al menos uno es True
print("Resultado OR:", resultado_or)


# NOT (no lógico)
resultado_not = not a  # Devuelve True si a es False, y viceversa
print("Resultado NOT:", resultado_not)


# Operadores lógicos con condiciones
x = 10
y = 5


# Combinación de condiciones con AND
if x > 5 and y < 10:
    print("x es mayor que 5 y y es menor que 10")


# Combinación de condiciones con OR
if x < 5 or y < 10:
    print("x es menor que 5 o y es menor que 10")


# Combinación de condiciones con NOT
if not (x < 5):
    print("x no es menor que 5")



# Operadores lógicos con diferentes tipos de datos


# Comparación de cadenas
cadena1 = "Hola"
cadena2 = "Mundo"
if cadena1 == "Hola" and cadena2 == "Mundo":
    print("Ambas cadenas son iguales")
