# Programa que captura el contenido de una caja tk.Entry() y con un boton lo muestra en una etiqueta tk.Label()

import tkinter as tk

# Crear la ventana principal 
ventana_principal = tk.Tk()

# Cambiar el título de la ventana 
ventana_principal.title("Ejemplo de boton")
# Configurar tamaño de la ventana
ventana_principal.geometry("400x300")

# Definir función al oprimir botón
def on_button_click():
    print("Hola Alumnos!")

# Definir función para enviar nombre con el boton ingresar
def enviar_nombre():
    #Imprimir en consola el nombre ingresado
    print(caja.get())
    # Cambiar el texto de la etiqueta2 para mostrar el nombre ingresado
    etiqueta2.config(text="Hola "+ caja.get())






# Crear el botón
button = tk.Button(ventana_principal, text="Oprimir", command=on_button_click)
# Agregar botón a la ventana
button.pack(pady=20)


# Crear caja de texto Label
etiqueta = tk.Label(text="Ingresa tu nombre")
etiqueta.place(x=20, y=90)

# Crear caja de texto Entry
caja = tk.Entry()
caja.place(x=20, y=120 , width=200, height=25)

# Crear otro botón
button_ingresar = tk.Button(ventana_principal, text="Mostrar Nombre", command=enviar_nombre)
# Agregar botón a la ventana
# Colocar el botón al lado de la caja usando place()
# Calculamos la posición x: (x de la caja + ancho de la caja + un pequeño espacio)
# Mantenemos la misma 'y' para que estén alineados verticalmente.
button_ingresar.place(x=20 + 200 + 10, y=120, width=120, height=25) # x=230

# Crear etiqueta para mostrar el nombre ingresado
etiqueta2 = tk.Label(text="")
etiqueta2.place(x=20, y=160)


# Ejecutar la aplicación
ventana_principal.mainloop()