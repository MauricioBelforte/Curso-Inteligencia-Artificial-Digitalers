# ¿Qué son los argumentos en Python? 

Los argumentos son valores que se pasan a una función cuando esta es llamada. 
Sirven para proporcionar datos de entrada que la función utiliza para realizar su tarea. 
Los argumentos se definen dentro de los paréntesis al momento de declarar la función y pueden ser obligatorios o tener valores predeterminados.

Ej:

```python

    def imprimir_elementos(lista):
        for elemento in lista:
            print(elemento)

    alumnos = ["Pablo", "Juan", "Matias", "Martin"]
    notas = [5.5, 9, 6.25, 8]

    imprimir_elementos(alumnos)
    imprimir_elementos(notas)

```

Una función puede tener múltiples argumentos, la cantidad que sea necesaria. 
Para indicar más de uno, se separan sus nombres por comas.

Ej:

```python

    def imprimir_suma(a, b):
        print("Resultado:")
        print(a + b)

    imprimir_suma(7, 5)
    imprimir_suma(-5, 3.5)

```

# Retorno 

## Valor de retorno
Las funciones pueden opcionalmente devolver un resultado.

Ej:

```python
    def sumar(a, b):
        return a + b

    resultado = sumar(7, 5)
    print(resultado)
    print(sumar(-5, 3.5))
```