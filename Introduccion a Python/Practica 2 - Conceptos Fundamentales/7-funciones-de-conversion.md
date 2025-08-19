# La función input() en Python 

Siempre devuelve un valor de tipo string (cadena de texto), aunque el usuario escriba números. Por eso, si necesitas trabajar con números (por ejemplo, para hacer operaciones matemáticas), debes convertir ese string a un tipo numérico, como int() para enteros o float() para decimales.

Por ejemplo:

```python

numero = input("Ingrese un número: ")  # Esto es un string
numero_entero = int(numero)            # Ahora es un entero

```
En tu código:

```python

dividendo = int(input("Ingrese el dividendo: "))

Primero pide el dato como string y luego lo convierte a entero con int()