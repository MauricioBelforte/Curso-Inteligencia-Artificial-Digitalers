
import ComponenteFormulario from './ComponenteFormulario.js';

const contenedor = document.getElementById('contenedor');
const miFormulario = new ComponenteFormulario(contenedor, { idFormulario: 'registro-persona' });
miFormulario.renderizar();

// Escuchar el evento de envío
contenedor.addEventListener('formularioEnviado', (e) => {
    console.log('Datos del formulario:', e.detail);
    alert(`Formulario enviado:\n${JSON.stringify(e.detail, null, 2)}`);
});