""" 
📌 ¿Qué es una tupla?
- Es una colección ordenada de elementos.
- Se define con paréntesis: (valor1, valor2, valor3)
- Ideal para almacenar datos que no deberían cambiar (❌ Inmutable): como coordenadas, configuraciones, o valores fijos
 """
# Las tuplas no permiten asignación de ítems y tampoco tienen métodos.

# Definimos una tupla con datos personales
persona = ("Mauricio", 29, "Argentina")

# Accedemos a los elementos como si fuera una lista
print(persona[0])  # Imprime "Mauricio"
print(persona[1])  # Imprime 29

# Intentar modificarla generará un error
# persona[1] = 30  # ❌ Esto lanzaría un TypeError


""" 🧠 ¿Cuándo conviene usar tuplas?
- Cuando querés garantizar que los datos no se modifiquen.
- Para funciones que retornan múltiples valores, como:
 """

def obtener_dimensiones():
    return (1920, 1080)

ancho, alto = obtener_dimensiones()
print(f"Resolución: {ancho}x{alto}")


""" 
💡 ¿Cuándo elegir cada una?
- Usá listas cuando vas a agregar, eliminar o cambiar datos.
- Usá tuplas cuando querés proteger la estructura y garantizar que esos datos permanezcan intactos.
 """