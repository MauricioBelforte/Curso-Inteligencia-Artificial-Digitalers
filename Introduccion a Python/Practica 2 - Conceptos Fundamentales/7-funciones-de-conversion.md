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
```

Primero pide el dato como string y luego lo convierte a entero con int()




# Conversiones entre tipos de datos

Python no permite operaciones directas entre tipos incompatibles, demandando conversiones explicitas mediante funciones como:

- int(): Convierte un número decimal, booleano o una cadena que representa un entero en un número entero (int).
Ejemplo: int('42') devuelve 42, int(3.9) devuelve 3.
- str(): Convierte cualquier tipo de dato (como números, booleanos o listas) en una cadena de texto.
Ejemplo: str(123) devuelve '123'.
- float(): Convierte enteros, booleanos o cadenas numéricas en un número decimal (float).
Ejemplo: float('3.14') devuelve 3.14, float(10) devuelve 10.0.



