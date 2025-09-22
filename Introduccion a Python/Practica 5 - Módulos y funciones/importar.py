import time

# La función time.asctime() devuelve la fecha y hora actual,
# pero para verla en la consola, necesitamos imprimirla.
print(time.asctime())


# Esta funcion se ejecuta luego de 5 segundos
print(time.sleep(5))


# Retorna la resolución del reloj en segundos (float)
# print(time.get_clock_info('time'))

# Otros ejemplos con la librería time
print(time.ctime())          # Fecha y hora actual en formato legible
print(time.time())          # Tiempo en segundos desde la época (1 de enero de 1970)
print(time.localtime())     # Estructura de tiempo local
print(time.gmtime())        # Estructura de tiempo en UTC
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # Formateo de fecha y hora

# Otro modulo estandar de Python es math
import math
print(math.sqrt(16))  # Raíz cuadrada de 16
print(math.factorial(5))  # Factorial de 5
print(math.pi)  # Valor de pi
print(math.e)   # Valor de e
print(math.sin(math.pi / 2))  # Seno de 90 grados (π/2 radianes)
print(math.log(100, 10))  # Logaritmo base 10 de 100
print(math.ceil(4.2))  # Redondeo hacia arriba
print(math.floor(4.7))  # Redondeo hacia abajo
print(math.gcd(48, 18))  # Máximo común divisor de 48 y 18
# print(math.lcm(4, 5))  # Mínimo común múltiplo de 4 y 5 (disponible en Python 3.9+)

# Otros modulos estandares de Python son random, os, sys, json, re, datetime, entre otros.

# Ejemplo de uso del modulo random
import random
print(random.randint(1, 10))  # Número aleatorio entre 1 y 10
print(random.choice(['manzana', 'banana', 'cereza']))  # Elección aleatoria de una lista
print(random.random())  # Número aleatorio entre 0 y 1
print(random.sample(range(100), 5))  # Muestra aleatoria de 5 números únicos del 0 al 99