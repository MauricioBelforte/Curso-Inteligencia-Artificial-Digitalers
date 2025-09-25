# Documentación: Pruebas Unitarias en Python con `unittest`

Este documento explica el funcionamiento de un ejemplo de pruebas unitarias en Python, utilizando el módulo `unittest`, que forma parte de la librería estándar de Python. El objetivo es probar una simple función de división, cubriendo tanto el caso de éxito como el manejo de errores.

---

## 1. El Código de la Función (`division.py`)

Este archivo contiene la lógica de negocio que queremos probar. Es la "unidad" de código que se someterá a prueba.

```python
def dividir(a, b):
    """
    Divide dos números.
    :param a: El dividendo.
    :param b: El divisor.
    :return: El resultado de la división.
    :raises ZeroDivisionError: Lanza una excepción si el divisor (b) es 0.
    """
    # Validación de caso límite: Comprobamos si se está intentando dividir por cero.
    if b == 0:
        # Lanzar una excepción específica de Python para este error.
        raise ZeroDivisionError("División por cero")
    
    # Si la validación pasa, la función retorna el resultado.
    return a / b
```

### Puntos Clave:

*   **`def dividir(a, b)`**: Una función estándar de Python que toma dos argumentos.
*   **`if b == 0`**: Una guarda de seguridad para controlar el caso de la división por cero.
*   **`raise ZeroDivisionError`**: A diferencia de un error genérico, Python proporciona excepciones específicas para diferentes tipos de errores. `ZeroDivisionError` es la excepción idiomática y correcta para este escenario, lo que hace que el código sea más explícito y claro.

---

## 2. El Código de la Prueba (`test_division.py`)

Este archivo utiliza el framework `unittest` para verificar que la función `dividir` se comporta como se espera.

```python
# 1. Importamos el módulo `unittest` que proporciona el framework de pruebas.
import unittest
# 2. Importamos la función `dividir` que queremos probar.
from division import dividir

# 3. Creamos una clase que hereda de `unittest.TestCase`.
class TestDivision(unittest.TestCase):

    # 4. Definimos un método de prueba. El nombre debe empezar con `test_`.
    def test_division_correcta(self):
        # 5. Usamos un método de aserción para verificar la igualdad.
        self.assertEqual(dividir(10, 2), 5)

    # 6. Definimos otro método de prueba para el caso de error.
    def test_division_por_cero(self):
        # 7. Usamos un manejador de contexto para verificar que se lanza una excepción.
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

# 8. Este bloque permite ejecutar las pruebas directamente desde la terminal.
if __name__ == "__main__":
    unittest.main()
```

### Puntos Clave:

*   **`import unittest`**: Importa el framework de pruebas, que ya viene incluido en Python.
*   **`class TestDivision(unittest.TestCase)`**: En `unittest`, las pruebas se organizan en clases que deben heredar de `unittest.TestCase`. Esta herencia proporciona acceso a los métodos de aserción (como `assertEqual`).
*   **`def test_...`**: Los métodos dentro de la clase que representan casos de prueba **deben** comenzar con el prefijo `test_`. Así es como el corredor de pruebas (`test runner`) los identifica.
*   **`self.assertEqual(a, b)`**: Es un **método de aserción** que verifica si `a` es igual a `b`. Es el equivalente a `expect(a).toBe(b)` en Jest.
*   **`with self.assertRaises(...)`**: Esta es la forma idiomática en Python para probar que se lanza una excepción. Es un **manejador de contexto** que ejecuta el código anidado. La prueba pasa si el código dentro del bloque `with` lanza la excepción especificada (`ZeroDivisionError`). Si no lanza ninguna excepción, o lanza una diferente, la prueba falla.
*   **`if __name__ == "__main__"`**: Este es un bloque estándar en Python que permite que el archivo se ejecute como un script. Al correr `python test_division.py`, se invoca a `unittest.main()`, que descubre y ejecuta automáticamente todas las pruebas en el archivo.