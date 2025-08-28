# Operadores de pertenencia

# En Python, los operadores in y not in se llaman operadores de pertenencia (membership)
# Se usan para determinar si las variables se encuentran en una colección (lista, tupla y diccionario) o no.


# in
# Devuelve True cuando el valor está presente en la secuencia.
 
# not in
# Devuelve True cuando el valor no está presente en la secuencia.


# Para el caso de los diccionarios, se puede realizar la operación de pertenencia para la clave, pero no para el valor.
# En los diccionarios, se pregunta por el key.
print("Diccionarios\n")

alumnos = {"Juan":5,"Florencia":10,"Horacio":1}

print("Juan" in alumnos)
# True
print("Victoria" in alumnos)
# False
print("Florencia" not in alumnos)
# False
print("Esteban" not in alumnos)
# True


print("\n")

# En las listas, se pregunta directamente por el elemento (ítem).
print("Listas\n")

nombres = ["Juan","Tomas","Susana"]

print("Susana" in nombres)
# True
print("Alejandro" in nombres)
# False