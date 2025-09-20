# El metodo isdecimal()

El método `isdecimal()` en Python `es un método de los strings` que se utiliza para verificar si todos los caracteres en una cadena son decimales. Devuelve `True` si todos los caracteres son decimales y hay al menos un carácter, de lo contrario devuelve `False`.

## ¿Qué es el método isdecimal( ) ?
Los métodos son funciones que tienen algunos objetos en este lenguaje, los cuales ayudan a
resolver una problemática sobre el propio objeto. 
Cuando el usuario ingresa un número por la consola, ese número ingresa al programa como un string, y debería convertirlo. Pero si, hipotéticamente, se diseña un programa en el que se pide un valor numérico entero y luego el usuario ingresa un dato que no se puede convertir con la función int(), el programa termina de forma imprevista porque se produce un error de conversión.
El método isdecimal() que tienen los string permite evaluar si es posible convertir “ese dato” ingresado, o no. 

Observa el ejemplo:

edad = input("Ingrese edad: ")
Ingrese edad: 40
input(edad.isdecimal())
True

# Funciones
Una función es un bloque de código que solo se ejecuta cuando es llamado. Puedes pasar datos, conocidos como parámetros, a una función. Las funciones pueden devolver datos como resultado.

## Definir una función
En Python, puedes definir una función utilizando la palabra clave `def`, seguida del nombre de la
función y paréntesis que pueden incluir parámetros. Aquí hay un ejemplo básico:

```python
def greet(name):
    """Esta función saluda a la persona cuyo nombre se pasa como parámetro."""
    print(f"Hola, {name}!")
```
```python
greet("Alice")  # Llama a la función greet con el argumento "Alice"
# Salida: Hola, Alice!
```

## Parámetros y Argumentos
En la definición de una función, los valores entre paréntesis son llamados parámetros. Cuando llamas a la función, los valores que pasas son llamados argumentos.

```python
def greet(name):
    print(f"Hola, {name}!")
greet("Bob")  # "Bob" es el argumento pasado a la función
# Salida: Hola, Bob!
```

## Valores de Retorno
Las funciones pueden devolver valores utilizando la palabra clave `return`. Aquí hay un ejemplo:
```python
def add(a, b):
    """Esta función devuelve la suma de dos números."""
    return a + b
result = add(5, 3)
print(result)  # Salida: 8
```
## Funciones Anónimas (Lambda)
Python también admite funciones anónimas, conocidas como funciones lambda. Estas son pequeñas funciones que se definen sin un nombre y se utilizan para operaciones simples.

```python
square = lambda x: x * x
result = square(4)
print(result)  # Salida: 16
```
## Documentación de Funciones
Es una buena práctica documentar tus funciones utilizando cadenas de documentación (docstrings). Estas cadenas describen lo que hace la función y cómo usarla.



## Funciones Integradas
Python viene con muchas funciones integradas que puedes usar directamente. Algunos ejemplos comunes incluyen `print()`, `len()`, `type()`, y `int()`.

```python
print("Hola, mundo!")  # Imprime "Hola, mundo!"
length = len("Hola")  # Devuelve la longitud de la cadena
print(length)  # Salida: 4
number = int("123")  # Convierte la cadena "123" a un entero
print(number)  # Salida: 123
print(type(number))  # Salida: <class 'int'>
```

## Alcance de las Variables
El alcance de una variable determina dónde puede ser accedida dentro del código. Las variables definidas dentro de una función tienen un alcance local y solo pueden ser utilizadas dentro de esa función. Las variables definidas fuera de cualquier función tienen un alcance global y pueden ser accedidas desde cualquier parte del código.

```python
x = 10  # Variable global

def my_function():
    y = 5  # Variable local
    print(x)  # Accediendo a la variable global
    print(y)  # Accediendo a la variable local

my_function()
print(x)  # Accediendo a la variable global 
print(y)  # Esto causará un error porque y es una variable local
```