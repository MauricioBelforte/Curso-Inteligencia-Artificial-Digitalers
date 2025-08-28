# Diccionarios

# Los diccionarios son colecciones, pero sus elementos (o valores) no están ordenados ni asociados a un índice, sino a una clave. 
# Los miembros de un diccionario son pares de clave-valor.


# Este código crea un diccionario de nombre alumno1 cuyas claves son "nombre" y "cursos", y sus valores, respectivamente, "Pablo" y 3. 
alumno1 = {"nombre": "Pablo", "cursos": 3}


# Los valores de un diccionario pueden ser cualquier tipo de dato, incluidos otros diccionarios y listas. 
# En cambio, las claves tienen ciertas restricciones (por ejemplo, no pueden repetirse)

print(alumno1["nombre"])
print(alumno1["cursos"])
# Accedemos a los valores del diccionario usando sus claves entre corchetes

# También podemos usar el método get() para acceder a los valores
print(alumno1.get("nombre"))
print(alumno1.get("cursos"))

# La ventaja de get() es que si la clave no existe, no lanza un error, sino que devuelve None (o un valor por defecto si se lo indicamos)
print(alumno1.get("edad"))  # Devuelve None
print(alumno1.get("edad", 18))  # Devuelve 18 como valor


# Del mismo modo, puedes cambiar los valores:
alumno1["cursos"] = 4

# O bien crear nuevos pares clave-valor:
alumno1["curso_actual"] = "Python"

# Cada clave debe ser única porque funciona como un identificador del valor asociado. 
# Si intentas agregar una clave duplicada, el valor más reciente sobrescribirá el valor anterior para esa clave.


# Usando un bucle for sobre un diccionario, tienes acceso a cada una de sus claves. Por ejemplo:

for clave in alumno1:
    print(clave)
    print(alumno1[clave])  # Accedemos al valor usando la clave

# Los diccionarios permiten crear estructuras de datos más complejas
# Por ejemplo, para almacenar la información de un alumno. 
# Para mostrar por pantalla el diccionario completo, utiliza:

alumno_a = {"nombre": "Sofía", "edad":15, (10, 20): True}
print("Diccionario completo", alumno_a)
