# Operadores de asignación en Python

# Los operadores de asignación se utilizan para asignar valores a variables.
# Los operadores de asignación más comunes son: =, +=, -=, *=, /=, %=, //=, **=.
# Estos operadores permiten realizar operaciones aritméticas y asignar el resultado a una variable.


# Operadores de asignación básicos

# Asignación simple
x = 10  # Asigna el valor 10 a la variable x

# Asignación con suma
x += 5  # Equivalente a x = x + 5, ahora x es 15

# Asignación con resta
x -= 3  # Equivalente a x = x - 3, ahora x es 12

# Asignación con multiplicación
x *= 2  # Equivalente a x = x * 2, ahora x es 24

# Asignación con división
x /= 4  # Equivalente a x = x / 4, ahora x es 6.0

# Asignación con módulo
x %= 5  # Equivalente a x = x % 5, ahora x es 1.0

# Asignación con división entera
x //= 2  # Equivalente a x = x // 2, ahora x es 0.0

# Asignación con potencia
x **= 3  # Equivalente a x = x ** 3, ahora x es 0.0


# Imprimir el valor final de x
print("Valor final de x:", x)

# Asignación de múltiples variables
a, b, c = 1, 2, 3  # Asigna 1 a a, 2 a b y 3 a c

# Imprimir los valores de a, b y c
print("Valores de a, b y c:", a, b, c)


# Asignación de una variable a otra
d = a  # Asigna el valor de a a d

# Imprimir el valor de d
print("Valor de d (igual a a):", d)

# Asignación de una variable a sí misma
d = d + 1  # Incrementa d en 1, ahora d es 2

# Imprimir el valor final de d
print("Valor final de d:", d)


# Asignación de una variable a una expresión
e = a + b * c  # Asigna el resultado de la expresión a e

# Imprimir el valor de e
print("Valor de e (a + b * c):", e)
