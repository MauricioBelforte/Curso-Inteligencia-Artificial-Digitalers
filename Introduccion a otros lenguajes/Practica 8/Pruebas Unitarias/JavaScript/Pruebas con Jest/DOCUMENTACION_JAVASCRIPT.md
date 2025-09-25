# Documentación: Pruebas Unitarias en JavaScript con Jest

Este documento explica el funcionamiento de un ejemplo básico de pruebas unitarias en JavaScript, utilizando el framework [Jest](https://jestjs.io/). El objetivo es probar una simple función de división, cubriendo tanto el caso de éxito como el manejo de errores.

---

## 1. El Código de la Función (`division.js`)

Este archivo contiene la lógica de negocio que queremos probar. Es una "unidad" de código aislada.

```javascript
/**
 * Divide dos números.
 * @param {number} a - El dividendo (el número que se va a dividir).
 * @param {number} b - El divisor (el número por el que se divide).
 * @returns {number} El resultado de la división.
 * @throws {Error} Lanza un error si el divisor (b) es 0.
 */
function dividir(a, b) {
  // Validación de caso límite: Comprobamos si se está intentando dividir por cero.
  if (b === 0) {
    // Si la condición se cumple, la función se detiene y lanza un error.
    throw new Error("División por cero");
  }
  // Si no se dividió por cero, la función retorna el resultado esperado.
  return a / b;
}

// Hacemos que la función `dividir` esté disponible para ser usada en otros archivos.
module.exports = dividir;
```

### Puntos Clave:

*   **`function dividir(a, b)`**: Una función simple que toma dos argumentos para realizar una operación matemática.
*   **`if (b === 0)`**: Es una **guarda de seguridad**. La división por cero es una operación indefinida que causa errores. Con esta condición, anticipamos y controlamos el problema.
*   **`throw new Error(...)`**: Es la forma estándar en JavaScript de señalar que algo ha salido mal de forma excepcional. Detiene la ejecución de la función y notifica que ocurrió un error.
*   **`module.exports`**: Es el mecanismo del sistema de módulos de Node.js (CommonJS) para **exportar** funcionalidades. Esto permite que otros archivos puedan **importar** y usar la función `dividir`.

---

## 2. El Código de la Prueba (`division.test.js`)

Este archivo utiliza Jest para verificar que la función `dividir` se comporta como esperamos en diferentes escenarios.

```javascript
// Importación: Traemos la función `dividir` desde el otro archivo para poder usarla.
const dividir = require("./division");

// Primer caso de prueba: El "camino feliz"
test("División correcta", () => {
  // Se espera que el resultado de dividir 10 entre 2 sea 5.
  expect(dividir(10, 2)).toBe(5);
});

// Segundo caso de prueba: Manejo de errores
test("División por cero lanza error", () => {
  // Se espera que al llamar a dividir(10, 0), se lance un error con un mensaje específico.
  expect(() => dividir(10, 0)).toThrow("División por cero");
});
```

### Puntos Clave:

*   **`require("./division")`**: **Importa** la función que vamos a probar, gracias a que fue exportada en `division.js`.
*   **`test(...)`**: Es una función global que Jest proporciona para definir un **caso de prueba**. Recibe dos argumentos:
    1.  Una `string` que describe lo que la prueba verifica.
    2.  Una función que contiene la lógica de la prueba.
*   **`expect(valor)`**: Es el corazón de una prueba en Jest. Envuelve el valor o resultado que quieres comprobar. Devuelve un objeto "expectation" sobre el cual puedes usar "matchers".
*   **`.toBe(esperado)`**: Es un **"matcher"**. Comprueba si el resultado de `expect` es estrictamente igual (`===`) al valor esperado. Es ideal para tipos de datos primitivos (números, strings, booleanos).
*   **`.toThrow(mensaje)`**: Otro "matcher", diseñado para verificar errores.
    *   La sintaxis `expect(() => dividir(10, 0))` es crucial. Para probar que una función lanza un error, debemos envolver la llamada a esa función dentro de otra función anónima (`() => ...`).
    *   El matcher `.toThrow()` comprueba que, al ejecutar esa función, efectivamente se lanzó un error. Opcionalmente, se le puede pasar un `string` para verificar que el mensaje del error es el esperado.