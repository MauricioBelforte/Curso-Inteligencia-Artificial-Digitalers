# Operadores de comparación

# Operadores de comparación en Python
# Los operadores de comparación se utilizan para comparar dos valores y devolver un valor booleano (True o False).
# Estos operadores son útiles en estructuras de control como condicionales y bucles.
# Los operadores de comparacion más comunes son:
# Igualdad (==), Desigualdad (!=), Mayor que (>), Menor que (<), Mayor o igual que (>=), Menor o igual que (<=).



# Igualdad

a = 5
b = 5
if a == b:
    print("a es igual a b")
else:
    print("a no es igual a b")


# Desigualdad

if a != b:
    print("a es diferente de b")
else:
    print("a es igual a b")


# Mayor que

if a > b:
    print("a es mayor que b")
else:
    print("a no es mayor que b")


# Menor que

if a < b:
    print("a es menor que b")
else:
    print("a no es menor que b")


# Mayor o igual que

if a >= b:
    print("a es mayor o igual que b")
else:
    print("a es menor que b")


# Menor o igual que

if a <= b:
    print("a es menor o igual que b")
else:
    print("a es mayor que b")


# Operadores de comparación con diferentes tipos de datos

# Comparación de números

a = 10
b = 20
if a < b:
    print("a es menor que b")
elif a > b:
    print("a es mayor que b")
else:
    print("a es igual a b")


# Comparación de cadenas

cadena1 = "Hola"
cadena2 = "Mundo"
if cadena1 < cadena2:
    print("cadena1 es menor que cadena2")
elif cadena1 > cadena2:
    print("cadena1 es mayor que cadena2")
else:
    print("cadena1 es igual a cadena2")


# Comparación de booleanos

bool1 = True
bool2 = False
if bool1 and not bool2:
    print("bool1 es verdadero y bool2 es falso")
elif bool1 or bool2:
    print("bool1 es verdadero o bool2 es verdadero")
else:
    print("Ambos booleanos son falsos")

