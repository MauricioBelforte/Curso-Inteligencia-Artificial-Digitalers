
""" Ejercicio 4
Calculadora
Crea una aplicación de escritorio con dos cajas
de texto y un botón, de modo que al presionarlo
se imprima en pantalla la suma de los dos
números ingresados en las primeras.
La disposición de los controles y el tamaño de la
ventana quedan a tu criterio. """

import tkinter as tk
# Importamos el módulo messagebox que nos permite mostrar cuadros de diálogo
from tkinter import messagebox



# Función para sumar los números y mostrar el resultado
def sumar_numeros():
    try:
        num1 = float(caja_texto1.get())
        num2 = float(caja_texto2.get())
        resultado = num1 + num2
        # Mostrar el resultado en un cuadro de diálogo
        messagebox.showinfo("Resultado", f"La suma es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")





# Crear la ventana principal
ventana = tk.Tk()
# Configura el titulo de la ventana
ventana.title("Calculadora de Suma")
# Configura el tamaño de la ventana
ventana.geometry("300x200")
# Configura la ventana para que no se pueda redimensionar
ventana.resizable(False, False)
# Cambia el color de fondo de la ventana
ventana.configure(bg="#f0f0f0")
# Centrar la ventana en la pantalla
ventana.eval('tk::PlaceWindow . center')


# Crear etiquetas y cajas de texto

# Crea la primer etiqueta
etiqueta1 = tk.Label(ventana, text="Número 1:", bg="#f0f0f0")
# Agrega la etiqueta a la ventana con un poco de espacio vertical
etiqueta1.pack(pady=5)

# Crea la primer caja de texto
caja_texto1 = tk.Entry(ventana)
# Agrega la caja de texto a la ventana con un poco de espacio vertical
caja_texto1.pack(pady=5)

# Crea la segunda etiqueta y caja de texto
etiqueta2 = tk.Label(ventana, text="Número 2:", bg="#f0f0f0")
etiqueta2.pack(pady=5)
caja_texto2 = tk.Entry(ventana)
caja_texto2.pack(pady=5)




# Crear botón para realizar la suma
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar_numeros)
boton_sumar.pack(pady=10, ipadx=10, ipady=5)
# Ejecutar la aplicación
ventana.mainloop()  
# Fin del programa

