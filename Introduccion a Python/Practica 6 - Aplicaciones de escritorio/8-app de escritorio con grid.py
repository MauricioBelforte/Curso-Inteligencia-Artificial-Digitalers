import tkinter as tk

# --- Configuración de la Ventana Principal ---
ventana_principal = tk.Tk()
ventana_principal.title("Diseño Responsivo con Grid (Todo en Grid)")
ventana_principal.geometry("450x300") # Tamaño inicial de ejemplo para la ventana

# --- Definición de Funciones ---

# Función que se ejecuta al oprimir el botón "Oprimir"
def on_button_click():
    print("Hola Alumnos!")

# Función que se ejecuta al oprimir el botón "Mostrar Nombre"
# Obtiene el texto de la caja y lo imprime en la consola.
def enviar_nombre():
    print("Nombre ingresado:", caja.get())

# --- Configuración de la Responsividad de Filas y Columnas con grid() ---
# Esta es la clave para que los elementos se adapten cuando redimensiones la ventana.

# Configuración de las columnas:
# columnconfigure(índice_columna, weight=peso)
# El 'weight' determina cuánto espacio extra absorberá una columna
# en relación con otras columnas cuando la ventana se expanda horizontalmente.

# La columna 0 contendrá la etiqueta "Ingresa tu nombre" y la caja de texto.
# Le damos un 'weight=2' para que se expanda el doble que la columna 1,
# permitiendo que la caja de texto crezca más que el botón adyacente.
ventana_principal.columnconfigure(0, weight=2)

# La columna 1 contendrá el botón "Mostrar Nombre".
# Le damos un 'weight=1'. Se expandirá, pero menos que la columna 0.
ventana_principal.columnconfigure(1, weight=1)

# Configuración de las filas:
# rowconfigure(índice_fila, weight=peso)
# Similar a las columnas, el 'weight' para las filas determina cuánto
# espacio extra absorberá una fila cuando la ventana se expanda verticalmente.

# La fila 0 contendrá el botón "Oprimir".
# Le damos un 'weight=0' porque no queremos que esta fila se expanda verticalmente.
# Esto mantiene el botón "Oprimir" en la parte superior sin que se aleje demasiado si la ventana se agranda.
ventana_principal.rowconfigure(0, weight=0)

# La fila 1 contendrá la etiqueta "Ingresa tu nombre".
# También 'weight=0' porque no necesitamos que esta fila se expanda.
ventana_principal.rowconfigure(1, weight=0)

# La fila 2 contendrá la caja de texto y el botón "Mostrar Nombre".
# Le damos un 'weight=1' para que esta fila sí se expanda verticalmente
# si la ventana se agranda, empujando el contenido hacia abajo.
ventana_principal.rowconfigure(2, weight=1)

# --- Creación y Posicionamiento de Widgets (Todo con grid()) ---

# 1. Botón "Oprimir"
button = tk.Button(ventana_principal, text="Oprimir", command=on_button_click)
# .grid() posiciona el widget en la cuadrícula.
# row=0: Lo coloca en la primera fila.
# column=0: Lo inicia en la primera columna.
# columnspan=2: Hace que este botón abarque dos columnas (columna 0 y columna 1),
#               lo que ayuda a centrarlo sobre los elementos de abajo.
# padx=10, pady=20: Añaden 10 píxeles de relleno horizontal y 20 de relleno vertical
#                   alrededor del botón dentro de su celda.
# sticky="nswe": CRUCIAL para la responsividad. Le dice al widget que se "pegue"
#                a los bordes Norte, Sur, Oeste y Este de su celda.
#                Esto hace que el botón se expanda para llenar todo el espacio
#                disponible en la celda asignada, tanto horizontal como verticalmente.
button.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky="nswe")

# 2. Etiqueta "Ingresa tu nombre"
etiqueta = tk.Label(ventana_principal, text="Ingresa tu nombre")
# row=1, column=0: La coloca en la segunda fila, primera columna.
# padx=10, pady=5: Relleno alrededor de la etiqueta.
# sticky="w": Hace que la etiqueta se alinee al lado Oeste (izquierda) de su celda.
etiqueta.grid(row=1, column=0, padx=10, pady=5, sticky="w")

# 3. Caja de Texto (Entry)
caja = tk.Entry(ventana_principal)
# row=2, column=0: La coloca en la tercera fila, primera columna.
# padx=10: Relleno horizontal.
# pady=(0, 10): Relleno vertical: 0 píxeles arriba, 10 píxeles abajo.
#               Esto crea un espacio entre la caja y cualquier cosa debajo.
# sticky="ew": CRUCIAL. Hace que la caja de texto se estire horizontalmente
#              para ocupar todo el ancho disponible en la columna 0.
caja.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="ew")

# 4. Botón "Mostrar Nombre"
button_ingresar = tk.Button(ventana_principal, text="Mostrar Nombre", command=enviar_nombre)
# row=2, column=1: Lo coloca en la tercera fila, segunda columna, justo al lado de la caja.
# padx=(0, 10): Relleno horizontal: 0 píxeles a la izquierda (para que esté pegado a la caja)
#               y 10 píxeles a la derecha.
# pady=(0, 10): Relleno vertical: 0 píxeles arriba, 10 píxeles abajo.
# sticky="ew": CRUCIAL. Hace que el botón se estire horizontalmente para ocupar
#              todo el ancho disponible en la columna 1.
button_ingresar.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

# --- Ejecución de la Aplicación ---
# Inicia el bucle de eventos de Tkinter, manteniendo la ventana abierta
# y respondiendo a interacciones del usuario.
ventana_principal.mainloop()