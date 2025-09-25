

# Guía: Pruebas Unitarias en C# con NUnit

Este documento explica paso a paso cómo crear y ejecutar pruebas unitarias en **C# usando NUnit**, trabajando con **Visual Studio Code** y también comparando con **Visual Studio completo**.

---

## 🔹 ¿Qué son las pruebas unitarias?

Las pruebas unitarias son pequeños programas que verifican si una función o clase de nuestro código funciona como esperamos. Sirven para detectar errores temprano y asegurar la calidad del software.

---

## 🔹 Configuración en VS Code (CLI de .NET)

### 1. Crear una solución

```bash
dotnet new sln -n PruebasUnitarias
```

Esto genera un archivo `.sln` que sirve para organizar proyectos.

### 2. Crear el proyecto de lógica

```bash
dotnet new classlib -n Logica
```

Aquí irá nuestro código principal.

### 3. Crear el proyecto de pruebas con NUnit

```bash
dotnet new nunit -n Logica.Tests
```

Este comando ya incluye:

* `NUnit`
* `NUnit3TestAdapter`
* `Microsoft.NET.Test.Sdk`

Así evitamos instalar paquetes manualmente.

### 4. Agregar proyectos a la solución

```bash
dotnet sln add Logica/Logica.csproj
 dotnet sln add Logica.Tests/Logica.Tests.csproj
```

### 5. Conectar el proyecto de pruebas con la lógica

```bash
dotnet add Logica.Tests/Logica.Tests.csproj reference Logica/Logica.csproj
```

### 6. Ejecutar las pruebas

```bash
dotnet test
```

---

## 🔹 Código de ejemplo

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

## 🔹 Diferencias de sintaxis en frameworks de test

* **MSTest**: `Assert.AreEqual(expected, actual)`
* **NUnit**: `Assert.That(actual, Is.EqualTo(expected))`

---

## 🔹 VS Code vs Visual Studio completo

### En **Visual Studio Code**

* Todo se hace con la **terminal** usando comandos `dotnet`.
* Para usar NUnit hay dos formas:

  1. **Manual**: crear proyecto (`dotnet new console`) y luego instalar paquetes con `dotnet add package`.
  2. **Automática (recomendada)**: `dotnet new nunit`, que ya trae los paquetes listos.

### En **Visual Studio completo (IDE grande)**

* Podés crear un **proyecto de pruebas unitarias** desde el asistente.

  * Elegís si querés MSTest, NUnit o xUnit.
  * Los paquetes NuGet se instalan solos.
* Si creás un proyecto vacío (ejemplo: consola), ahí sí debés instalar manualmente los paquetes (`NUnit`, `NUnit3TestAdapter`, `Microsoft.NET.Test.Sdk`) desde el **Administrador de Paquetes NuGet** gráfico.
* Para correr los tests usás el **Test Explorer**, no la terminal.

✅ Conclusión:

* En **VS Code** se trabaja más con la terminal.
* En **Visual Studio completo**, todo es más automático y visual.

---

## 🔹 Resultado esperado al correr `dotnet test`

```
Passed!  - Failed: 0, Passed: 2, Skipped: 0
```




# Pruebas unitarias en C# con NUnit — Paso a paso

**Propósito:** Documentar paso a paso cómo creamos un proyecto con una librería (`Logica`) y un proyecto de pruebas con **NUnit** (`Logica.Tests`), el código (`Division.cs`), los tests (`DivisionTests.cs`) y cómo ejecutar todo desde la terminal (VS Code).

---

## Requisitos

* .NET SDK instalado (comprobá con `dotnet --version`).
* Visual Studio Code (opcional, pero recomendado) o cualquier editor de texto.
* Extensión recomendada en VS Code: **C# (OmniSharp)**. Opcional: extensiones de Test Explorer para ejecutar tests con UI.

---

## Resumen de la estructura que vamos a crear

```
PruebasUnitarias/             # carpeta raíz de la solución
├─ PruebasUnitarias.sln       # solución (opcional pero útil)
├─ Logica/                    # proyecto de librería con la lógica a testear
│  └─ Division.cs
└─ Logica.Tests/              # proyecto de pruebas (NUnit)
   └─ DivisionTests.cs
```

---

## Comandos (creación de la solución y proyectos)

Abrí la terminal (VS Code o PowerShell / Bash) y corré los siguientes comandos **desde la carpeta donde querés crear el proyecto**:

```bash
dotnet new sln -n PruebasUnitarias
dotnet new classlib -n Logica
dotnet new nunit -n Logica.Tests

dotnet sln add Logica/Logica.csproj
dotnet sln add Logica.Tests/Logica.Tests.csproj

dotnet add Logica.Tests/Logica.Tests.csproj reference Logica/Logica.csproj
```

**Qué hace cada comando:**

* `dotnet new sln -n PruebasUnitarias`: crea una solución llamada `PruebasUnitarias`.
* `dotnet new classlib -n Logica`: crea un proyecto de biblioteca (`Logica`) donde ponemos `Division.cs`.
* `dotnet new nunit -n Logica.Tests`: crea un proyecto de pruebas ya configurado con NUnit (no necesitas instalar paquetes manualmente).
* `dotnet sln add ...`: agrega ambos proyectos a la solución.
* `dotnet add ... reference ...`: hace que `Logica.Tests` referencie a `Logica` para poder probar su código.

---

## Código: `Logica/Division.cs`

```csharp
public class Division {
    public static double Dividir(double a, double b) {
        if (b == 0) throw new DivideByZeroException("División por cero");
        return a / b;
    }
}
```

### Explicación línea por línea

* `public class Division { ... }` — declaramos una **clase pública** llamada `Division`. Public asegura que otros proyectos (p. ej. `Logica.Tests`) puedan acceder a ella.
* `public static double Dividir(double a, double b) { ... }` — definimos un **método estático** llamado `Dividir` que toma dos `double` y devuelve un `double`:

  * `public`: accesible desde fuera de la clase.
  * `static`: no hace falta instanciar `Division` para usar el método; se usa como `Division.Dividir(...)`.
  * `double`: tipo numérico decimal de doble precisión.
* `if (b == 0) throw new DivideByZeroException("División por cero");` — si el divisor es cero, lanzamos (throw) una excepción **`DivideByZeroException`** indicando el problema. Esto es útil para que el test verifique que la función responde lanzando una excepción en ese caso.
* `return a / b;` — realiza la división y devuelve el resultado. Si `b` fuera 0, no se llega a esta línea por la excepción anterior.

> Nota: podés fully-qualify `System.DivideByZeroException` si preferís, pero no es obligatorio si `System` está disponible implícitamente.

---

## Tests: `Logica.Tests/DivisionTests.cs`

```csharp
using NUnit.Framework;

namespace Logica.Tests {
    public class DivisionTests {

        [Test]
        public void DivisionCorrecta() {
            Assert.That(Division.Dividir(10, 2), Is.EqualTo(5));
        }

        [Test]
        public void DivisionPorCero() {
            Assert.Throws<System.DivideByZeroException>(() => Division.Dividir(10, 0));
        }
    }
}
```

### Explicación de los elementos clave

* `using NUnit.Framework;` — importa las herramientas de NUnit (atributos, `Assert`, etc.).
* `namespace Logica.Tests { ... }` — define un espacio de nombres para los tests (opcional, ayuda a organizar).
* `public class DivisionTests { ... }` — la clase que contiene los tests.
* `[Test]` — atributo que marca un método como caso de test que el runner (dotnet test) debe ejecutar.

**Las aserciones:**

* `Assert.That(Division.Dividir(10, 2), Is.EqualTo(5));`

  * Verificamos que el resultado de `Division.Dividir(10, 2)` sea igual a `5`.
  * `Assert.That(actual, Is.EqualTo(expected))` es la forma recomendada y explícita en NUnit.
* `Assert.Throws<System.DivideByZeroException>(() => Division.Dividir(10, 0));`

  * Verificamos que ejecutar `Division.Dividir(10, 0)` **lanza** una excepción `DivideByZeroException`.
  * `Assert.Throws<TException>(Action)` espera que la acción lance la excepción `TException`.

---

## Ejecutar los tests

Desde la carpeta raíz (donde está `PruebasUnitarias.sln`), ejecutá:

```bash
dotnet test
```

Salida esperada (resumen):

```
Passed!  - Failed: 0, Passed: 2, Skipped: 0
```

Si algún test falla, `dotnet test` mostrará detalles de la excepción o del assert que haya fallado.

---

## Sobre el error que viste: `Assert` no contiene `AreEqual`

El error `CS0117: 'Assert' no contiene una definición para 'AreEqual'` puede deberse a varias causas:

1. **Conflicto de nombres / `using` incorrecto**: podría haber otro tipo `Assert` en scope (p. ej. de MSTest o de otro paquete) que no tiene `AreEqual` con la misma firma, o no se está importando `NUnit.Framework` correctamente.
2. **Plantilla equivocada**: si por error el proyecto de tests no es realmente un proyecto NUnit (p. ej. fue creado con MSTest), la API de `Assert` puede variar.

**Cómo evitarlo**:

* Usamos `dotnet new nunit` para crear el proyecto de tests; ese template ya referencia las librerías correctas.
* En la guía preferimos `Assert.That(...)` (sintaxis explícita de NUnit), que es idiomática y evita ambigüedades.

Si querés usar la forma `Assert.AreEqual(expected, actual)` y te da error, comprobá:

* `using NUnit.Framework;` está presente.
* No hay `using` que traiga otro `Assert` en conflicto.
* El `csproj` de `Logica.Tests` referencia a `NUnit` (el template `dotnet new nunit` lo hace automáticamente).

---

## Script (PowerShell) para crear todo de una vez en Windows (copiar/pegar)

> Este script crea la solución, los proyectos, agrega referencias y crea los archivos `Division.cs` y `DivisionTests.cs` con el contenido mostrado arriba, y finalmente ejecuta `dotnet test`.

```powershell
# Crear solución y proyectos
dotnet new sln -n PruebasUnitarias
dotnet new classlib -n Logica
dotnet new nunit -n Logica.Tests

dotnet sln add Logica/Logica.csproj
dotnet sln add Logica.Tests/Logica.Tests.csproj

dotnet add Logica.Tests/Logica.Tests.csproj reference Logica/Logica.csproj

# Crear Division.cs
@"
public class Division {
    public static double Dividir(double a, double b) {
        if (b == 0) throw new System.DivideByZeroException("División por cero");
        return a / b;
    }
}
"@ | Out-File -Encoding UTF8 Logica\Division.cs

# Crear DivisionTests.cs
@"
using NUnit.Framework;

namespace Logica.Tests {
    public class DivisionTests {

        [Test]
        public void DivisionCorrecta() {
            Assert.That(Division.Dividir(10, 2), Is.EqualTo(5));
        }

        [Test]
        public void DivisionPorCero() {
            Assert.Throws<System.DivideByZeroException>(() => Division.Dividir(10, 0));
        }
    }
}
"@ | Out-File -Encoding UTF8 Logica.Tests\DivisionTests.cs

# Ejecutar tests
dotnet test
```

Si usás **Bash** o Git Bash, el script de creación de archivos cambia (usá `cat > archivo << 'EOF' ... EOF`).

---

## Consejos / buenas prácticas

* Mantené responsabilidades separadas: la lógica en `Logica` y los tests en `Logica.Tests`.
* Pon nombres descriptivos a los tests y cubrí ambos casos: comportamiento esperado y casos de error (excepciones).
* Usá el Test Explorer en VS Code si preferís una interfaz gráfica para ejecutar tests y ver resultados.
* Si querés agrupar tests por categoría u ordenar, NUnit soporta `[SetUp]`, `[TearDown]`, `[TestCase]`, `[Category("...")]`, etc.

---

