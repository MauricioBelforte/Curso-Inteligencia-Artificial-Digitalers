// ComponenteFormulario.js
class ComponenteFormulario {
    /**
     * @param {HTMLElement} contenedorPadre - Elemento donde se renderizará el formulario
     * @param {Object} [opciones] - Opciones opcionales (ej: id del formulario)
     */
    constructor(contenedorPadre, opciones = {}) {
        if (!(contenedorPadre instanceof HTMLElement)) {
            throw new Error('contenedorPadre debe ser un HTMLElement válido');
        }
        this.contenedor = contenedorPadre;
        this.idFormulario = opciones.idFormulario || 'formulario-usuario';
        this.formulario = null; // referencia al formulario
    }

    /**
     * Renderiza el formulario dentro del contenedor usando innerHTML
     */
    renderizar() {
        this.contenedor.innerHTML = `
      <form id="${this.idFormulario}" class="formulario" novalidate>
        <div class="campo">
          <label for="${this.idFormulario}-nombre">Nombre</label>
          <input type="text" id="${this.idFormulario}-nombre" name="nombre" required />
        </div>

        <div class="campo">
          <label for="${this.idFormulario}-apellido">Apellido</label>
          <input type="text" id="${this.idFormulario}-apellido" name="apellido" required />
        </div>

        <div class="campo">
          <label for="${this.idFormulario}-documento">Documento</label>
          <input type="text" id="${this.idFormulario}-documento" name="documento" inputmode="numeric" />
        </div>

        <div class="campo">
          <label for="${this.idFormulario}-fecha">Fecha de nacimiento</label>
          <input type="date" id="${this.idFormulario}-fecha" name="fechaNacimiento" />
        </div>

        <div class="acciones">
          <button type="submit">Enviar</button>
          <button type="button" data-accion="limpiar">Limpiar</button>
        </div>
      </form>
    `;

        this.formulario = this.contenedor.querySelector(`#${this.idFormulario}`);
        this._vincularEventos();
    }

    /**
     * Obtiene los valores del formulario como objeto
     */
    obtenerValores() {
        if (!this.formulario) return null;
        const datos = new FormData(this.formulario);
        return {
            nombre: datos.get('nombre') || '',
            apellido: datos.get('apellido') || '',
            documento: datos.get('documento') || '',
            fechaNacimiento: datos.get('fechaNacimiento') || ''
        };
    }

    /**
     * Limpia el formulario
     */
    limpiar() {
        if (this.formulario) this.formulario.reset();
    }

    /**
     * Vincula los eventos internos de submit y limpiar
     * @private
     */
    _vincularEventos() {
        if (!this.formulario) return;

        this.formulario.addEventListener('submit', (evento) => {
            evento.preventDefault();
            const valores = this.obtenerValores();

            // Validación simple
            if (!valores.nombre.trim() || !valores.apellido.trim()) {
                console.warn('Nombre y apellido son obligatorios');
                return;
            }

            // Evento personalizado con los datos del formulario
            const eventoPersonalizado = new CustomEvent('formularioEnviado', {
                detail: valores,
                bubbles: true,
                cancelable: true
            });
            this.formulario.dispatchEvent(eventoPersonalizado);
        });

        this.formulario.addEventListener('click', (evento) => {
            const boton = evento.target.closest('button[data-accion="limpiar"]');
            if (boton) this.limpiar();
        });
    }
}

export default ComponenteFormulario; // si usas módulos
