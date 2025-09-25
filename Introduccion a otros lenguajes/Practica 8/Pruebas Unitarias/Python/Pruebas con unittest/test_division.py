# 1. Importamos el módulo `unittest` que proporciona el framework de pruebas.
import unittest
# 2. Importamos la función `dividir` que queremos probar.
from division import dividir

# 3. Creamos una clase que hereda de `unittest.TestCase`.
#    Esta clase agrupará todas nuestras pruebas relacionadas con la división.
class TestDivision(unittest.TestCase):

    # 4. Definimos un método de prueba para el "camino feliz".
    #    ¡Importante! El nombre del método debe empezar con `test_`.
    def test_division_correcta(self):
        # 5. `self.assertEqual` es un método de aserción de unittest.
        #    Verifica si el primer argumento (el resultado de dividir(10, 2))
        #    es igual al segundo argumento (5).
        self.assertEqual(dividir(10, 2), 5)

    # 6. Definimos otro método de prueba para el caso de error.
    def test_division_por_cero(self):
        # 7. `self.assertRaises` es un "context manager" (manejador de contexto).
        #    Afirma que el código que se ejecuta DENTRO del bloque `with`
        #    DEBE lanzar la excepción especificada (ZeroDivisionError).
        #    Si lo hace, la prueba pasa. Si no lanza ninguna excepción o lanza
        #    una diferente, la prueba falla.
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

# 8. Este bloque estándar permite ejecutar las pruebas directamente desde la terminal
#    corriendo `python test_division.py`. `unittest.main()` descubre y ejecuta los tests.
if __name__ == "__main__":
    unittest.main()