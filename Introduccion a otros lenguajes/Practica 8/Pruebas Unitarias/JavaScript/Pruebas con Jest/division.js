  // 0. Funcion que divide dos números.
  // param {number} a - El dividendo (el número que se va a dividir).
  // param {number} b - El divisor (el número por el que se divide).
  // returns {number} El resultado de la división.
  // throws {Error} Lanza un error si el divisor (b) es 0.
 

function dividir(a, b) {
  // 1. Validación de caso límite: Comprobamos si se está intentando dividir por cero.
  if (b === 0) {
    // 2. Lanzar un error: Si la condición se cumple, la función se detiene inmediatamente
    // y "lanza" un objeto Error con un mensaje descriptivo.
    throw new Error("División por cero");
  }
  // 3. Camino feliz: Si no se dividió por cero, la función retorna el resultado esperado.
  return a / b;
}

// 4. Exportación: Hacemos que la función `dividir` esté disponible para ser usada
// en otros archivos de nuestro proyecto (como el archivo de pruebas).
module.exports = dividir;


/* 
En resumen:

* function dividir(a, b): 
  Una función simple que toma dos argumentos.
* if (b === 0): 
  Es una guarda de seguridad. La división por cero es una indeterminación matemática y en programación suele causar errores. Aquí la anticipamos.
* throw new Error(...): 
  Es la forma estándar en JavaScript de señalar que algo ha salido mal de forma excepcional. Detiene la ejecución de la función.
* module.exports: 
  Es el mecanismo de Node.js para exportar funcionalidades y poder importarlas desde otros archivos con require. 

*/