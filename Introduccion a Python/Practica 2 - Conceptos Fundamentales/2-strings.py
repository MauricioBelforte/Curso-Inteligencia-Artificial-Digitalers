nombre = "Juan"
apellido = "Pérez"
ciudad = "Madrid"

# Concatenación de cadenas o strings
mensaje = nombre + " " + apellido + " vive en " + ciudad

# Metodos de transformación de cadenas
mensaje_mayusculas = mensaje.upper()  # Convierte a mayúsculas
mensaje_minusculas = mensaje.lower()  # Convierte a minúsculas

# Longitud de la cadena
longitud_mensaje = len(mensaje)

# Substrings
inicial_nombre = nombre[0]  # Primera letra del nombre

print("Mensaje:", mensaje)
print("Mensaje en mayúsculas:", mensaje_mayusculas)
print("Mensaje en minúsculas:", mensaje_minusculas)
print("Longitud del mensaje:", longitud_mensaje)
print("Inicial del nombre:", inicial_nombre)


# Donde encontrar más información sobre las funciones:
# https://docs.python.org/3/library/functions.html
