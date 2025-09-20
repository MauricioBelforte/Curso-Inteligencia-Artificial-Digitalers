# Variables y ámbitos

Todas las variables en Python tienen un ámbito (scope),
que es el lugar en el que una variable es
reconocida como tal, es decir, el lugar en donde
una variable es visible para otras porciones de
código.

# Alcance de las variables

El alcance de variables es la accesibilidad y
visibilidad que tiene una variable dentro del
código.

## Alcance local
Cuando se declara una variable dentro de una
función, esta se considera local, lo que significa
que solo existe y puede ser utilizada dentro de
esa función específica.
Por ejemplo, la variable x dentro de una función
calcular solo existirá mientras la función se
ejecute, y no es posible acceder a ella desde otras
partes del programa.

```python
    def calcular_promedio():
        # Variables locales
        nota1 = 15
        nota2 = 18
        promedio = (nota1 + nota2) / 2
        return promedio
 ```

## Alcance global

Son aquellas que se declaran fuera de cualquier
función y pueden ser accedidas desde cualquier
parte del programa.
Sin embargo, es importante notar que si se quiere
modificar una variable global dentro de una
función, hay que declararla explícitamente
usando la palabra clave global. Esto le indica a
Python que se desea trabajar con la variable
global y no crear una nueva variable local.

```python
    # Variable global
    nombre_curso = "Python Básico"
    def mostrar_mensaje():
        # Variable local
        mensaje = "Bienvenidos al curso"
        print(mensaje + " de " + nombre_curso) 
 ```

# Python sigue la regla LEGB para buscar variables, de acuerdo con el siguiente orden:

1. Ámbito local.
2. Enclosing (funciones anidadas).
3. Ámbito global.
4. Built-in (funciones incorporadas).
   
Este orden es fundamental para entender cómo Python resuelve los nombres de variables cuando las encuentra en el código.


Es recomendable limitar el uso de variables globales, ya que pueden hacer que el código sea más difícil de mantener y depurar. 
En su lugar, es preferible pasar variables como parámetros a las funciones y devolver resultados mediante return, lo que hace que el código sea más claro y predecible.


Este ejemplo muestra cómo modificar una variable global desde dentro de una función.
Como vimos, se usa la palabra clave global seguida del nombre de la variable. 
Cada vez que se llame a esta función, el contador global def saludo_estudiante(): aumentará en uno.

```python

    contador = 0
    def sumar_punto():
        global contador
        contador = contador + 1
 ```

Este segundo ejemplo muestra el caso contrario, cuando queremos modificar la variable del programa principal desde la función. 
Al usar la palabra global, le indicamos a Python que queremos trabajar con la variable del programa principal y no crear una nueva.

Al ejecutar el código, el valor de contador cambia tanto dentro como fuera de la función, porque estamos trabajando con la misma variable.


```python
    contador = 0 # Variable en programa principal
    def incrementar():
        global contador # Indicamos que usaremos la variable global
        contador = contador + 1
        print("Dentro de la función: " + str(contador))

    print("Valor inicial: " + str(contador))
    incrementar()
    print("Valor final: " + str(contador))
 ```