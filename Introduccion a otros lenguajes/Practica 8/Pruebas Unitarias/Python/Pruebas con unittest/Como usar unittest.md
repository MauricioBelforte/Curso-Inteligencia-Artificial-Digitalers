
## 🔹 **Python**

* El módulo `unittest` **ya viene en la librería estándar** de Python.
* No necesitas instalar nada.

---

## 🔹 Python (usando **unittest**)

```python
# Crear el archivo division.py
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero")
    return a / b
```

```python
# Crear el archivo test_division.py
import unittest
from division import dividir

class TestDivision(unittest.TestCase):

    def test_division_correcta(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_division_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

if __name__ == "__main__":
    unittest.main()
```

---

* Solo ejecutás:

  ```bash
  python test_division.py
  ```

