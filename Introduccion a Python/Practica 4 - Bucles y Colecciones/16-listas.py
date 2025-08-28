# Listas en Python

numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

alumnos = ["Ana", "Luis", "Pedro", "María"]

datos = [3.14, True ,-1 , False, "Hola mundo"]


# Las listas son colecciones ordenadas y ✅ Mutables de elementos. 
# Puedes acceder a los elementos por su índice, que comienza en 0.


print(numeros_primos[0])  # Imprime el primer elemento de la lista numeros_primos
print(alumnos[2])         # Imprime el tercer elemento de la lista alumnos
print(datos[4])           # Imprime el quinto elemento de la lista datos


""" 
💡 ¿Cuándo elegir cada una?
- Usá listas cuando vas a agregar, eliminar o cambiar datos.
- Usá tuplas cuando querés proteger la estructura y garantizar que esos datos permanezcan intactos.
 """