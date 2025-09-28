# Documentación: Creando una SPA con Router y Componente Principal

Este documento explica la arquitectura de "Laboratorio 2", que introduce dos conceptos fundamentales para el desarrollo web moderno en JavaScript: un **Router** y un **Componente de Aplicación**. Juntos, nos permiten crear una **Single Page Application (SPA)** o Aplicación de una Sola Página.

---

## 1. ¿Qué es una Single Page Application (SPA)?

Imagina una aplicación de escritorio tradicional. Cuando haces clic en un menú, no se cierra toda la ventana para abrir una nueva; simplemente, el contenido *dentro* de la ventana cambia.

Una SPA funciona de manera similar en un navegador web:

*   **Una sola carga:** El usuario carga un único archivo HTML (`index.html`) una sola vez.
*   **Navegación sin recargas:** Cuando el usuario navega a diferentes "páginas" (como de "Login" a "Cuenta"), el navegador no recarga la página completa. En su lugar, JavaScript elimina el contenido antiguo y carga el nuevo contenido dinámicamente dentro de un contenedor principal (en nuestro caso, el `<div id="root">`).
*   **Más rápido y fluido:** Esto crea una experiencia de usuario mucho más rápida y fluida, similar a la de una aplicación móvil o de escritorio.

Para lograr esto, necesitamos dos piezas clave: un director de orquesta (`ApplicationComponent`) y un sistema de navegación (`Router`).

---

## 2. El Componente `ApplicationComponent` (`Application.js`)

Piensa en el `ApplicationComponent` como el **cerebro o director de orquesta** de toda tu aplicación. Su trabajo es inicializar y conectar todas las piezas principales.

### Responsabilidades Clave:

1.  **Punto de Entrada:** Se instancia una sola vez cuando la página carga (`window.addEventListener("load", ...)`). Es el punto de partida de toda la lógica de JavaScript.

2.  **Control del DOM:** En su `constructor`, recibe y guarda una referencia al elemento principal donde se renderizará todo el contenido (el `<div id="root">`).

3.  **Crear el Router:** Crea una instancia de nuestro `Router`. El `ApplicationComponent` es el *dueño* del router.

4.  **Configurar las Rutas:** Esta es su tarea más importante. Le dice al `Router` qué debe hacer para cada "página" de la aplicación. Utiliza un método como `router.addRoute()` para asociar una URL (ej: `#/login`) con una función que renderiza la vista correspondiente.

    ```javascript
    // Dentro de ApplicationComponent.js
    _configurarRutas() {
        // Le decimos al router: "Cuando la URL sea #/login, ejecuta esta función"
        this.router.addRoute('#/login', () => {
            // La función se encarga de buscar el HTML de la vista de login,
            // inyectarlo en el 'root' y añadir la lógica necesaria.
            this.mostrarPagina('login'); 
        });

        // Hacemos lo mismo para las otras "páginas"
        this.router.addRoute('#/registro', () => {
            this.mostrarPagina('registro');
        });
    }
    ```

En resumen, el `ApplicationComponent` no renderiza nada directamente, sino que **configura el sistema que decide qué se debe renderizar y cuándo**.

---

## 3. El `Router` (`Router.js`)

Si el `ApplicationComponent` es el cerebro, el `Router` es el **sistema de navegación o el "GPS"** de la aplicación. Su única misión es observar la URL y activar la función correcta cuando esta cambia.

### Responsabilidades Clave:

1.  **Tabla de Rutas:** Mantiene un registro (un objeto o un `Map`) de las rutas que el `ApplicationComponent` le ha configurado. Esta tabla asocia un "path" (ej: `#/login`) con una "acción" (la función a ejecutar).

    ```javascript
    // Estructura interna del Router
    this.rutas = {
        '#/login': () => { /* acción para login */ },
        '#/registro': () => { /* acción para registro */ }
    };
    ```

2.  **Escuchar Cambios en la URL:** Utiliza el evento `hashchange` del navegador. Este evento se dispara automáticamente cada vez que la parte de la URL después del `#` (el "hash") cambia.

    ```javascript
    // Dentro del Router.js
    window.addEventListener('hashchange', () => this._onHashChange());
    ```

3.  **Activar la Ruta Correcta:** Cuando el evento `hashchange` se dispara, el `Router` hace lo siguiente:
    *   Obtiene el nuevo hash de la URL (ej: `window.location.hash`).
    *   Busca ese hash en su tabla de rutas.
    *   Si lo encuentra, **ejecuta la función (acción) asociada**.

### ¿Por qué usamos el "hash" (`#`)?

El hash tiene una propiedad especial: cambiarlo **no provoca una recarga de la página** por parte del navegador. Esto lo convierte en la herramienta perfecta y más sencilla para implementar un enrutador del lado del cliente en una SPA sin necesidad de configuraciones complejas en el servidor.

---

## 4. Flujo de Ejecución Completo

Veamos cómo funciona todo junto, paso a paso:

1.  **Carga Inicial:** El navegador carga `index.html`. El usuario ve la cabecera y un `<div id="root">` vacío. La URL es, por ejemplo, `.../index.html`.

2.  **Arranque de la App:** Se dispara el evento `load`. El script en `index.html` se ejecuta:
    *   `let root = document.getElementById("root");`
    *   `let app = new ApplicationComponent(root);`

3.  **Configuración:** El `constructor` de `ApplicationComponent` se ejecuta:
    *   Guarda el `div#root`.
    *   Crea una nueva instancia del `Router`.
    *   Llama a su método `_configurarRutas()`, registrando todas las rutas y sus acciones en el `Router` (ej: `router.addRoute('#/login', ...)`, `router.addRoute('#/registro', ...)`).
    *   El `Router`, a su vez, empieza a escuchar el evento `hashchange`.

4.  **Navegación Inicial:** Para mostrar una página por defecto, el `ApplicationComponent` puede establecer un hash inicial, por ejemplo: `window.location.hash = '#/login';`.

5.  **El Router Actúa:**
    *   El cambio de hash (`#/login`) dispara el evento `hashchange`.
    *   El `Router` lo detecta, busca `#/login` en su tabla de rutas y encuentra la función que le asoció el `ApplicationComponent`.
    *   Ejecuta esa función.

6.  **Renderizado de la Vista:**
    *   La función (acción) se ejecuta. Típicamente, esta función usa `fetch` para cargar `login.html`.
    *   Una vez cargado, inyecta el contenido HTML en el `div#root` con `root.innerHTML = ...`.
    *   Ahora el usuario ve la página de login.

7.  **Interacción del Usuario:** El usuario hace clic en un enlace como `<a href="#/registro">Registrarse</a>`.
    *   El navegador cambia el hash de la URL a `#/registro` **sin recargar la página**.
    *   El ciclo vuelve a empezar desde el **paso 5**: el `Router` detecta el cambio, busca la nueva ruta y ejecuta la acción correspondiente para mostrar la página de registro.

## Conclusión

Esta arquitectura **desacopla** las responsabilidades:
*   El **`ApplicationComponent`** sabe *qué* páginas existen y *qué* hacer para mostrarlas.
*   El **`Router`** no sabe nada sobre las páginas, solo sabe *cuándo* ha cambiado la URL y a *quién* notificar (ejecutar la acción).
*   Las **vistas** (los archivos `.html` individuales) son solo plantillas tontas que no contienen lógica de navegación.

Este patrón es la base de todos los frameworks modernos como React, Vue y Angular, pero implementado aquí de forma sencilla y con JavaScript puro.

Espero que ahora sí tengas el archivo y la explicación te sea de gran utilidad. ¡Es un concepto clave para el desarrollo web actual!

