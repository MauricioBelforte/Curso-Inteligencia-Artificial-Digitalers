import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
# Cambiar el título de la ventana
ventana.title("Ejemplo con pack()")
# Configurar tamaño de la ventana
ventana.geometry("300x200")

# Crear y posicionar widgets usando pack()

# Crea un primer label y lo configura con color rojo de fondo y texto blanco.
label1 = tk.Label(ventana, text="Etiqueta Superior", bg="red", fg="white")
# Apila el label y queda en la parte superior
# pady agrega un poco de espacio vertical alrededor del label
label1.pack(pady=5, fill=tk.X) # Y fill lo hace expandirse horizontalmente

# Crea un segundo label y lo configura con color azul de fondo y texto gris.
label2 = tk.Label(ventana, text="Etiqueta Inferior", bg="blue", fg="grey")
# Apila el label y queda en la parte inferior
# pady agrega un poco de espacio vertical alrededor del label
label2.pack(pady=5, fill=tk.X) # Y fill lo hace expandirse horizontalmente

# Crea dos botones y los posiciona a los lados izquierdo y derecho

# Crea un botón a la izquierda
boton_izq = tk.Button(ventana, text="Izquierda")
# Se apila a la izquierda
boton_izq.pack(side=tk.LEFT, padx=10) # side lo posiciona a la izquierda

# Crea un botón a la derecha
boton_der = tk.Button(ventana, text="Derecha")
# Se apila a la derecha
boton_der.pack(side=tk.RIGHT, padx=10) # side lo posiciona a la derecha

# Ejecutar la aplicación
ventana.mainloop()