import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
# Cambiar el título de la ventana
ventana.title("Ejemplo con grid()")

# Hacemos que la columna 1 se expanda si la ventana cambia de tamaño
ventana.columnconfigure(1, weight=1)

# Crear y posicionar widgets usando grid()
etiqueta_nombre = tk.Label(ventana, text="Nombre:")
# Colocamos la etiqueta en la fila 0, columna 0
# Sticky la alinea a la izquierda (west) 
etiqueta_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="w") # Alineado al oeste (izquierda)


# Crear una caja de texto

caja_nombre = tk.Entry(ventana)
# Colocamos la caja en la fila 0, columna 1
# Sticky la alinea a la derecha (east) y la hace expandirse horizontalmente (ew)
caja_nombre.grid(row=0, column=1, padx=10, pady=10, sticky="ew") # Se expande de este a oeste

# Crear un botón
boton_enviar = tk.Button(ventana, text="Enviar")
# Colocamos el botón en la fila 1, columna 1
boton_enviar.grid(row=1, column=1, padx=10, pady=10, sticky="e") # Alineado al este (derecha)

# Ejecutar la aplicación
ventana.mainloop()