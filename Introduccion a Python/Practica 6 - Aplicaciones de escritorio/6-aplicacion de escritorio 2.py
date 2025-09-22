# Programa que muestra mensajes por consola

import tkinter as tk

# Crear la ventana principal 
ventana_principal = tk.Tk()
# Cambiar el título de la ventana
ventana_principal.title("Ejemplo de boton")
# Configurar tamaño de la ventana
ventana_principal.geometry("400x300")


# Se define una funcion que sera llamada cuando se presione algun boton. 
# Tk se encargará de llamarla cuando el usuario presione en el botón, a través del argumento command
def on_button_click():
    print("Hola Alumnos!")

# Se define una funcion que sera llamada cuando se presione algun boton.
# Tk se encargará de llamarla cuando el usuario presione en el botón, a través del argumento command
def enviar_nombre():
    print(caja.get())




# Crear un botón
# Tk se encargará de llamar a la función on_button_click cuando el usuario presione el botón, a través del argumento command
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
# Tk se encargará de llamar a la función enviar_nombre cuando el usuario presione el botón, a través del argumento command
button_ingresar = tk.Button(ventana_principal, text="Mostrar Nombre", command=enviar_nombre)
# Agregar botón a la ventana
# Colocar el botón al lado de la caja usando place()
# Calculamos la posición x: (x de la caja + ancho de la caja + un pequeño espacio)
# Mantenemos la misma 'y' para que estén alineados verticalmente.
button_ingresar.place(x=20 + 200 + 10, y=120, width=120, height=25) # x=230

# Ejecutar la aplicación
ventana_principal.mainloop()