En cada lenguaje cambia un poco. Te detallo caso por caso:

---

## 🔹 **JavaScript**

* El ejemplo lo hice con **Jest** porque es el más usado.
* Sí, tenés que instalarlo:

  ```bash
  npm init -y
  npm install --save-dev jest
  ```
* En tu `package.json`, agregás:

  ```json
  "scripts": {
    "test": "jest"
  }
  ```
* Luego corrés:

  ```bash
  npm test
  ```

👉 Si no querés instalar nada extra, podés probar el código con `console.log` directamente, pero no tendrías tests formales.

---

## 🔹 **Python**

* El módulo `unittest` **ya viene en la librería estándar** de Python.
* No necesitas instalar nada.
* Solo ejecutás:

  ```bash
  python -m unittest test_division.py
  ```

---

## 🔹 **C#** (Tener en cuenta que esta opcion no funciona en VS Code)

* El ejemplo usa **NUnit**, que sí requiere instalación de paquetes con NuGet:

  ```bash
  dotnet add package NUnit
  dotnet add package NUnit3TestAdapter
  dotnet add package Microsoft.NET.Test.Sdk
  ```
* Después corrés los tests con:

  ```bash
  dotnet test
  ```

👉 Si no querés instalar NUnit, también podés usar **xUnit** o **MSTest**, pero siempre hay que agregar algún framework de test.

---


Con **Visual Studio (el IDE completo, no VS Code)** la cosa cambia un poco:

---

### 🔹 En Visual Studio completo

1. Creás un **proyecto de pruebas unitarias** desde el asistente (te deja elegir: MSTest, NUnit o xUnit).
   👉 Visual Studio ya te instala y configura los paquetes de NuGet automáticamente.

2. Si en cambio creás un **proyecto vacío** (por ejemplo, un "Console App"), ahí sí tenés que:

   * Abrir el **Administrador de Paquetes NuGet** desde el IDE.
   * Buscar e instalar `NUnit`, `NUnit3TestAdapter` y `Microsoft.NET.Test.Sdk`.
   * Recién ahí podés escribir tus tests.

3. Cuando corrés los tests, Visual Studio usa el **Test Explorer** integrado (no necesitás la terminal).

---

### 🔹 Diferencia con VS Code

* En **VS Code** trabajás siempre con la **CLI de .NET (`dotnet`)**.

  * Si querés hacerlo “a mano”:

    ```bash
    dotnet new console -n MiProyecto
    cd MiProyecto
    dotnet add package NUnit
    dotnet add package NUnit3TestAdapter
    dotnet add package Microsoft.NET.Test.Sdk
    ```
  * O con el atajo:

    ```bash
    dotnet new nunit -n MiProyecto
    ```

* En **Visual Studio completo**, esas opciones ya están integradas en el asistente y en el gestor de paquetes.
  👉 Es más “gráfico” y más parecido a lo que estabas intentando.

---



## 🔹 **Java**

* El ejemplo está con **JUnit 5**, que también se instala.
* Si usás **Maven**, en el `pom.xml` agregás:

  ```xml
  <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter</artifactId>
      <version>5.10.0</version>
      <scope>test</scope>
  </dependency>
  ```
* Si usás **Gradle**:

  ```gradle
  testImplementation 'org.junit.jupiter:junit-jupiter:5.10.0'
  ```
* Luego corrés:

  ```bash
  mvn test
  ```

  o

  ```bash
  gradle test
  ```

---

✅ Resumen:

* **JS → instalar Jest (npm)**.
* **Python → ya tenés unittest, no instalás nada**.
* **C# → instalar NUnit (NuGet)**.
* **Java → instalar JUnit (Maven/Gradle)**.


---

👌 Entendido. Te armo **pruebas unitarias sencillas** en los cuatro lenguajes solicitados (JavaScript, Python, C# y Java).
Cada uno valida dos casos:

* Una división correcta.
* Una división por cero.

---

## 🔹 JavaScript (usando **Jest** como framework)

```javascript
// division.js
function dividir(a, b) {
  if (b === 0) throw new Error("División por cero");
  return a / b;
}
module.exports = dividir;
```

```javascript
// division.test.js
const dividir = require("./division");

test("División correcta", () => {
  expect(dividir(10, 2)).toBe(5);
});

test("División por cero lanza error", () => {
  expect(() => dividir(10, 0)).toThrow("División por cero");
});
```

---

## 🔹 Python (usando **unittest**)

```python
# division.py
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero")
    return a / b
```

```python
# test_division.py
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

## 🔹 C# (usando **NUnit**)

```csharp
// Division.cs
public class Division {
    public static double Dividir(double a, double b) {
        if (b == 0) throw new DivideByZeroException("División por cero");
        return a / b;
    }
}
```

```csharp
// DivisionTests.cs
using NUnit.Framework;

[TestFixture]
public class DivisionTests {

    [Test]
    public void DivisionCorrecta() {
        Assert.AreEqual(5, Division.Dividir(10, 2));
    }

    [Test]
    public void DivisionPorCero() {
        Assert.Throws<System.DivideByZeroException>(() => Division.Dividir(10, 0));
    }
}
```

---

## 🔹 Java (usando **JUnit 5**)

```java
// Division.java
public class Division {
    public static double dividir(double a, double b) {
        if (b == 0) throw new ArithmeticException("División por cero");
        return a / b;
    }
}
```

```java
// DivisionTest.java
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class DivisionTest {

    @Test
    void divisionCorrecta() {
        assertEquals(5, Division.dividir(10, 2));
    }

    @Test
    void divisionPorCero() {
        assertThrows(ArithmeticException.class, () -> Division.dividir(10, 0));
    }
}
```

---

👉 Estos ejemplos usan frameworks muy comunes:

* **Jest** en JS
* **unittest** en Python
* **NUnit** en C#
* **JUnit 5** en Java
