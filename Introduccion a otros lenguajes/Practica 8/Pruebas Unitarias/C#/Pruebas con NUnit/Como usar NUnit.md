

## 🔹 Paso a paso en C# con NUnit (en VS Code)

1. **Abrí una carpeta vacía** en VS Code donde quieras guardar el proyecto.

2. **Creá una solución** (esto organiza los proyectos):

   ```bash
   dotnet new sln -n PruebasUnitarias
   ```

3. **Creá el proyecto de lógica** (ejemplo: donde va `Division.cs`):

   ```bash
   dotnet new classlib -n Logica
   ```

   Esto crea la carpeta `Logica` con `Logica.csproj`.

4. **Creá el proyecto de pruebas con NUnit**:

   ```bash
   dotnet new nunit -n Logica.Tests
   ```

   👉 Este paso es el importante: ya incluye
   `NUnit`, `NUnit3TestAdapter`, `Microsoft.NET.Test.Sdk` en el `.csproj`.
   No tenés que hacer `dotnet add package` manual.

5. **Agregá los proyectos a la solución**:

   ```bash
   dotnet sln add Logica/Logica.csproj
   dotnet sln add Logica.Tests/Logica.Tests.csproj
   ```

6. **Conectá el proyecto de pruebas con la lógica**:

   ```bash
   dotnet add Logica.Tests/Logica.Tests.csproj reference Logica/Logica.csproj
   ```

---

## 🔹 Archivos

### `Logica/Division.cs`

```csharp
public class Division {
    public static double Dividir(double a, double b) {
        if (b == 0) throw new DivideByZeroException("División por cero");
        return a / b;
    }
}
```

### `Logica.Tests/DivisionTests.cs`

```csharp
using NUnit.Framework;

namespace Logica.Tests {
    public class DivisionTests {

        [Test]
        public void DivisionCorrecta() {
            // NUnit usa Assert.That
            Assert.That(Division.Dividir(10, 2), Is.EqualTo(5));
        }

        [Test]
        public void DivisionPorCero() {
            Assert.Throws<System.DivideByZeroException>(() => Division.Dividir(10, 0));
        }
    }
}

```

---

## 🔹 Correr los tests

Desde la carpeta raíz (donde está el `.sln`):

```bash
dotnet test
```

Si todo va bien deberías ver algo así:

```
Passed!  - Failed: 0, Passed: 2, Skipped: 0
```

---

✅ Con este flujo no hace falta instalar paquetes a mano, solo usar `dotnet new nunit`.

---

