# Programa que imprime en consola el nombre de usuario ingresado y tiene opción de salir de la app

import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
# Cambiar el título de la ventana
ventana.title("Aplicación de Escritorio")
# Configurar tamaño de la ventana
ventana.geometry("400x200")

# Funciones para los botones

# Definir función al oprimir botón
""" 
Todas las cajas de texto incluyen una función llamada get() que retorna la cadena ingresada por el usuario. 
Para llamarla, se usa la siguiente sintaxis: caja.get().
 """
def ingresar_usuario():
 nombre = caja_nombre.get()
 print("Accedió " + nombre)

def cerrar_app():
 ventana.destroy()

# Crear y posicionar widgets usando place()
etiqueta_nombre = tk.Label(text="Ingrese su nombre")
etiqueta_nombre.place(x=20, y=30)

# Crear caja de texto
caja_nombre = tk.Entry()
caja_nombre.place(x=20, y=50, width=70, height=25)


# Crear botones

# Botón Ingresar
boton_ingreso = tk.Button(text="Ingresar", command=ingresar_usuario)
boton_ingreso.place(x=110, y=150, width=80, height=30)

# Botón Salir
boton_salir = tk.Button(text="Salir", command=cerrar_app)
boton_salir.place(x=290, y=150, width=80, height=30)

# Ejecutar la aplicación
ventana.mainloop()