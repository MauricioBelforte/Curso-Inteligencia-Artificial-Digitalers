// 0. El Código de la Prueba (division.test.js)
// Este archivo utiliza el framework Jest para verificar que la función dividir se comporta como esperamos en diferentes escenarios

// 1. Importación: Traemos la función `dividir` desde el otro archivo para poder usarla.
const dividir = require("./division");

// 2. Definición de un "Test Case" o caso de prueba.
test("División correcta", () => {
  // 3. El núcleo de la prueba: `expect` y `matcher`.
  //    - `expect(dividir(10, 2))`: Ejecutamos la función con datos de prueba (10 y 2) y le decimos a Jest que "espere" algo sobre el resultado.
  //    - `.toBe(5)`: Este es el "matcher". Comprueba si el resultado de `expect` es estrictamente igual (===) a 5.
  expect(dividir(10, 2)).toBe(5);
});

// 4. Otro caso de prueba, esta vez para el manejo de errores.
test("División por cero lanza error", () => {
  // 5. Prueba de errores:
  //    - `expect(() => dividir(10, 0))`: ¡Esto es importante! Para probar que una función lanza un error, debemos envolver la llamada a esa función dentro de otra función (aquí una función flecha `() => ...`).
  //    - `.toThrow("División por cero")`: Este matcher verifica dos cosas:
  //      a) Que la función efectivamente lanzó un error.
  //      b) Que el mensaje de ese error es exactamente "División por cero".
  expect(() => dividir(10, 0)).toThrow("División por cero");
});





/* En resumen:

* require("./division"): 
  Importa la función que vamos a probar.
* test(...): 
  Es una función global de Jest que define un bloque de prueba. Recibe una descripción (que aparecerá en la consola) y una función con la lógica de la prueba.
* expect(valor).matcher(esperado): 
  Esta es la sintaxis fundamental de Jest.
* expect(): 
  Envuelve el valor o resultado que quieres comprobar.
* .toBe(), .toThrow(): 
  Son "matchers" o comparadores. Jest tiene muchísimos (toEqual para objetos, toBeNull, toBeTruthy, etc.) que te permiten verificar casi cualquier cosa. 

*/