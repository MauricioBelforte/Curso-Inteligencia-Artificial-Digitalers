import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
# Cambiar el título de la ventana
ventana.title("Ejemplo con place()")
# Configurar tamaño de la ventana
ventana.geometry("400x300")

# Posición absoluta de un label configurando texto y colores
label1 = tk.Label(ventana, text="Posición Fija (x=20, y=50)", bg="green", fg="white")
# Posición absoluta usando place()
label1.place(x=20, y=50)
# Como no especificamos los valores de los argumentos width y height, el tamaño es calculado automáticamente por Tk para que se adecue al texto de la etiqueta.



# Posición y tamaño relativos
boton_centro = tk.Button(ventana, text="Botón Centrado")
# Relativo al tamaño de la ventana
boton_centro.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # relx/rely lo posicionan, anchor lo centra en ese punto

# Ejecutar la aplicación
ventana.mainloop()