# Documentación: Creando Componentes Reutilizables con JavaScript (Vanilla JS)

Este documento explica cómo se ha construido un componente de formulario reutilizable utilizando únicamente JavaScript moderno, sin depender de ningún framework como React, Vue o Angular. El objetivo es demostrar cómo las características nativas del lenguaje, como las Clases y los Módulos, nos permiten crear código encapsulado, organizado y fácil de mantener.

---

## 1. Conceptos Clave

Para entender cómo funciona este proyecto, es fundamental conocer tres conceptos de JavaScript moderno:

### a. Clases de JavaScript (ES6)

Una clase es una "plantilla" para crear objetos. En nuestro caso, `ComponenteFormulario.js` define una clase llamada `ComponenteFormulario`.

*   **Encapsulación:** La clase agrupa toda la lógica y los datos relacionados con el formulario (renderizarlo, obtener sus valores, limpiarlo, manejar sus eventos) en un solo lugar.
*   **Reutilización:** Podemos crear múltiples instancias de esta clase (`new ComponenteFormulario(...)`) en diferentes partes de nuestra web, y cada una funcionará de manera independiente.
*   **Estado y Comportamiento:** La clase tiene propiedades (como `this.contenedor` o `this.formulario`) que guardan su estado, y métodos (como `renderizar()` o `limpiar()`) que definen su comportamiento.

### b. Módulos de JavaScript (ESM - ECMAScript Modules)

Los módulos nos permiten dividir nuestro código en archivos separados y reutilizables.

*   **`export`**: La línea `export default ComponenteFormulario;` en `ComponenteFormulario.js` hace que la clase esté disponible para ser utilizada por otros archivos.
*   **`import`**: La línea `import ComponenteFormulario from './ComponenteFormulario.js';` en `scripts.js` trae esa clase para poder usarla.
*   **`type="module"`**: Para que el navegador entienda la sintaxis `import`/`export`, es **crucial** añadir el atributo `type="module"` a la etiqueta `<script>` en el `index.html`. Sin esto, el navegador generaría un error de sintaxis.

```html
<!-- En index.html -->
<script type="module" src="scripts.js"></script>
```

### c. Eventos Personalizados (Custom Events)

¿Cómo sabe nuestra aplicación principal (el código en `scripts.js`) que el usuario ha pulsado el botón "Enviar" *dentro* del componente? El componente no debería tener que conocer la lógica externa.

La solución es la comunicación mediante eventos.

1.  **El Componente Despacha un Evento:** Cuando el formulario se envía correctamente, el componente crea y "despacha" (emite) un evento personalizado con los datos del formulario.

    ```javascript
    // Dentro de ComponenteFormulario.js
    const eventoPersonalizado = new CustomEvent('formularioEnviado', {
        detail: valores, // 'valores' es un objeto con los datos del form
        bubbles: true    // Permite que el evento "suba" por el DOM
    });
    this.formulario.dispatchEvent(eventoPersonalizado);
    ```

2.  **La Aplicación Escucha el Evento:** El archivo `scripts.js` (que actúa como la aplicación "padre") se pone a la escucha de este evento específico (`formularioEnviado`) en el contenedor. Cuando lo captura, puede acceder a los datos a través de `e.detail`.

    ```javascript
    // Dentro de scripts.js
    contenedor.addEventListener('formularioEnviado', (e) => {
        console.log('Datos recibidos desde el componente:', e.detail);
        // Aquí hacemos lo que queramos con los datos
    });
    ```

Este patrón de comunicación es muy potente porque **desacopla** el componente de la aplicación. El componente solo se encarga de emitir un aviso, y no le importa quién lo escuche o qué se haga con la información.

---

## 2. Flujo de Ejecución del Programa

El programa se ejecuta en el siguiente orden:

1.  **Carga del HTML:** El navegador lee `index.html` y encuentra la etiqueta `<script type="module" src="scripts.js"></script>`.

2.  **Ejecución de `scripts.js`:**
    *   Gracias a `type="module"`, el navegador procesa la línea `import ComponenteFormulario from './ComponenteFormulario.js';`.
    *   Busca y ejecuta el archivo `ComponenteFormulario.js` para tener la clase disponible.
    *   Obtiene el `div` con `id="contenedor"`.
    *   Crea una nueva instancia del componente: `new ComponenteFormulario(contenedor, ...)`. En este punto, el constructor de la clase se ejecuta, pero todavía no se ha dibujado nada en la pantalla.
    *   Llama al método `miFormulario.renderizar()`.

3.  **Ejecución de `renderizar()`:**
    *   Este método genera el HTML del formulario como un string y lo inyecta en el `div` contenedor usando `this.contenedor.innerHTML`.
    *   Una vez que el HTML está en el DOM, busca el elemento `<form>` que acaba de crear y lo guarda en `this.formulario`.
    *   Llama al método privado `_vincularEventos()` para añadir los `event listeners` de `submit` y `click` al formulario.

4.  **Estado de Espera:** La aplicación queda a la espera de la interacción del usuario.

5.  **Interacción del Usuario:**
    *   **Si el usuario hace clic en "Enviar"**:
        *   Se dispara el evento `submit` del formulario.
        *   El listener dentro de `_vincularEventos` se activa.
        *   `evento.preventDefault()` evita que la página se recargue.
        *   Se obtienen los valores del formulario.
        *   Tras una validación simple, se crea y despacha el `CustomEvent` llamado `formularioEnviado`.
        *   El `addEventListener` en `scripts.js` captura este evento, lee los datos de `e.detail` y muestra el `alert`.
    *   **Si el usuario hace clic en "Limpiar"**:
        *   Se dispara el evento `click`.
        *   El listener de `click` en `_vincularEventos` detecta que el objetivo era el botón de limpiar y llama al método `this.limpiar()`, que resetea el formulario.

---

## Conclusión

Este pequeño proyecto demuestra que no siempre se necesita un framework pesado para crear aplicaciones web estructuradas. Usando clases, módulos y eventos personalizados, podemos construir componentes encapsulados y reutilizables que mantienen nuestro código limpio, desacoplado y fácil de testear.