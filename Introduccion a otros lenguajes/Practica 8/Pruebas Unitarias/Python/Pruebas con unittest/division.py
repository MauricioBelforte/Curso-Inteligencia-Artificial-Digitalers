# 0. Función que divide dos números.
# :param a: El dividendo (el número que se va a dividir).
# :param b: El divisor (el número por el que se divide).
# :return: El resultado de la división.
# :raises ZeroDivisionError: Lanza una excepción si el divisor (b) es 0.
def dividir(a, b):
    # 1. Validación de caso límite: Comprobamos si se está intentando dividir por cero.
    if b == 0:
        # 2. Lanzar una excepción: En Python, es una buena práctica usar las excepciones
        # incorporadas cuando sea posible. ZeroDivisionError es la excepción específica
        # para este caso.
        raise ZeroDivisionError("División por cero")
    
    # 3. Camino feliz: Si la validación pasa, la función retorna el resultado.
    return a / b