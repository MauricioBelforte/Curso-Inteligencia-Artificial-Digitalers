""" 
Ejercicio 1
Función para forzar el ingreso numérico
Crea una función que fuerce el ingreso de solo
números.
 Debe recibir un número por argumento y
verificar que este sea un número posible de
convertir a int.
 En caso contrario, volver a pedir el ingreso
dentro de la función.
 Deber de retornar el valor convertido a int. 
"""

def ingreso_numerico(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return int(valor)
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Prueba de la función
numero = ingreso_numerico("Ingrese un número: ")
print(f"El número ingresado es: {numero}")
