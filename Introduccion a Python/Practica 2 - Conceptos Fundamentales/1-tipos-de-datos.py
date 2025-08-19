# Función type()
# La función type(), nos permite averiguar el tipo de dato de una variable


# Comprobación de tipos de datos

dato= 45.3  # Cambia este valor para probar diferentes tipos de datos

if type(dato) is int:
    print("El dato es un entero")
if type(dato) is float:
    print("El dato es un flotante")
if type(dato) is str:
    print("El dato es una cadena de texto")
if type(dato) is bool:
    print("El dato es un booleano")
if type(dato) is list:
    print("El dato es una lista")   
if type(dato) is tuple:
    print("El dato es una tupla")
if type(dato) is dict:
    print("El dato es un diccionario")
if type(dato) is set:
    print("El dato es un conjunto")
if type(dato) is complex:
    print("El dato es un número complejo")
if type(dato) is object:
    print("El dato es un objeto")




# None
# Cuando queremos crear un objeto, pero por el momento no asignarle ningún valor, generalmente se utiliza None 


""" 
a = None
type(a)
<class 'NoneType'> 
"""