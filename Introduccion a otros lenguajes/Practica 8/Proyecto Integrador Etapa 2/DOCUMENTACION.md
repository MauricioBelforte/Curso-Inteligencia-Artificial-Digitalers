# Documentación del Proyecto: Implementación de Pruebas Unitarias

Este documento detalla los pasos y conceptos aplicados para integrar pruebas unitarias en el proyecto, asegurando la calidad y el correcto funcionamiento de la lógica de negocio.

## 1. ¿Qué son las Pruebas Unitarias y por qué Jest?

Una **prueba unitaria** es un fragmento de código que verifica el comportamiento de una "unidad" aislada de nuestro software (en este caso, una clase o un método). El objetivo es garantizar que cada pieza funcione como se espera antes de integrarla con el resto del sistema.

Para este proyecto, elegimos **Jest**, un popular framework de pruebas de JavaScript por varias razones:
*   **Configuración Cero:** Es muy fácil de instalar y empezar a usar.
*   **Todo en Uno:** Incluye un ejecutor de pruebas, una librería de aserciones (`expect`) y la capacidad de crear "mocks" (simulaciones), todo en un solo paquete.
*   **Rápido y Eficiente:** Ejecuta pruebas en paralelo para acelerar el proceso.

## 2. Configuración del Entorno de Pruebas

Para poder ejecutar las pruebas, seguimos estos pasos en la terminal, desde la carpeta raíz del proyecto (`Proyecto Integrador Etapa 2/`).

### Paso 1: Inicializar el Proyecto con NPM
Ejecutamos el comando:
```bash
npm init -y
```
*   **¿Qué hace?**: Este comando crea un archivo `package.json`. Este archivo es el manifiesto del proyecto: describe sus propiedades (nombre, versión) y, lo más importante, gestiona sus dependencias y scripts. La bandera `-y` acepta todas las opciones por defecto.

### Paso 2: Instalar Jest
A continuación, instalamos Jest como una dependencia de desarrollo:
```bash
npm install --save-dev jest
```
*   **¿Qué hace?**: Descarga Jest y lo añade a la sección `devDependencies` de nuestro `package.json`.
*   **`--save-dev`**: Indica que Jest es una herramienta necesaria solo para el desarrollo y las pruebas, no para que la aplicación final funcione en producción.
*   Esto también crea la carpeta `node_modules` (donde se guardan los paquetes descargados) y el archivo `package-lock.json` (que asegura que siempre se instale la misma versión de las dependencias).

### Paso 3: Configurar el Script de Prueba
Modificamos el archivo `package.json` para añadir un atajo que nos permita ejecutar las pruebas fácilmente.
```json
// package.json
"scripts": {
  "test": "jest"
},
```
*   **¿Qué hace?**: Ahora, cada vez que ejecutemos `npm test` en la terminal, NPM sabrá que debe invocar a Jest.

## 3. Estructura del Proyecto y Organización

Para mantener el código fuente separado del código de prueba, creamos una carpeta especial.

```
Proyecto Integrador Etapa 2/
├── __tests__/
│   └── modelo.test.js  <-- Nuestras pruebas viven aquí
├── node_modules/
├── modelo.js           <-- La lógica de nuestra aplicación
├── package.json
└── DOCUMENTACION.md
```

*   **¿Por qué la carpeta `__tests__`?**: Es una convención estándar. Jest está preconfigurado para buscar y ejecutar automáticamente cualquier archivo que se encuentre dentro de una carpeta con este nombre. Esto mantiene nuestro proyecto limpio y organizado.

## 4. Escribiendo las Pruebas (`modelo.test.js`)

El archivo `modelo.test.js` contiene la lógica para verificar nuestras clases.

### Estructura Básica de una Prueba
```javascript
// 1. Importamos las clases que queremos probar
const { Cliente, Fintech } = require('../modelo.js');

// 2. Agrupamos pruebas relacionadas con `describe`
describe('Fintech', () => {
    
    // 3. `beforeEach` se ejecuta antes de CADA prueba en este grupo
    beforeEach(() => {
        // Esto asegura que cada prueba comience con un estado limpio
        fintech = new Fintech();
    });

    // 4. `it` define un caso de prueba específico
    it('debería crear un cliente y su cuenta asociada', () => {
        // Lógica de la prueba...
        const cliente = fintech.crearCliente(...);

        // 5. `expect` es la aserción: ¿se cumplió la expectativa?
        expect(cliente).toBeInstanceOf(Cliente);
        expect(fintech.clientes.size).toBe(1);
    });
});
```

## 5. El Misterio del Guion Bajo (`_`) en las Propiedades

Notamos un error de "Maximum call stack size exceeded" (bucle infinito). Esto ocurría por cómo funcionan los `getters` y `setters` en JavaScript.

### El Problema
```javascript
class Cliente {
    // ...
    set apellido(nuevoApellido) {
        // ¡ERROR! Al asignar a `this.apellido`, se vuelve a llamar a este mismo setter.
        this.apellido = nuevoApellido; 
    }
}
```

### La Solución: Propiedades de Respaldo (Backing Properties)
Para solucionarlo, usamos una convención de JavaScript: una propiedad interna con un guion bajo (`_`) para almacenar el valor real.

```javascript
class Cliente {
    // ...
    get apellido() {
        // El getter devuelve el valor de la propiedad interna.
        return this._apellido;
    }

    set apellido(nuevoApellido) {
        // El setter público modifica la propiedad interna.
        this._apellido = nuevoApellido;
    }
}
```
*   **¿Es algo de JavaScript?**: Sí. El guion bajo no tiene un poder especial en el lenguaje; es una **convención** entre desarrolladores que significa: "Esta propiedad es para uso interno de la clase, no la modifiques directamente desde fuera. Usa el getter o el setter público (`cliente.apellido`)".
*   Ahora, cuando hacemos `cliente.apellido = "Perez"`, se llama al `setter`, que a su vez modifica `this._apellido`. No hay bucle.

## 6. Preparando el Código para ser Probado (`modelo.js`)

Para que Jest (que se ejecuta en un entorno de Node.js) pudiera "ver" nuestras clases, tuvimos que exportarlas.

```javascript
// Al final de modelo.js

// Exporta las clases para poder usarlas en otros módulos (como los tests)
module.exports = { Cliente, Cuenta, Fintech, Movimiento };
```
Esto hace que las clases estén disponibles para ser importadas en `modelo.test.js` con `require('../modelo.js')`.

## 7. Cómo Ejecutar las Pruebas

Con todo configurado, ejecutar las pruebas es tan simple como abrir la terminal en la raíz del proyecto y correr:

```bash
npm test
```

Jest buscará todos los archivos de prueba, los ejecutará y mostrará un resumen claro de qué pruebas pasaron y cuáles fallaron. Esto nos da confianza para seguir desarrollando y modificando nuestro código, sabiendo que tenemos una red de seguridad que nos avisará si algo se rompe.