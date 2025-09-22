""" Ejercicio 3:
Crea una aplicación de escritorio que simule un
dado, es decir, debe arrojar número aleatorio de
1 al 6.
● La vista de la aplicación debería ser similar a
la imagen de la derecha.
● En la caja, deberían de aparecer los resultados
aleatorios cada vez que se presiona el botón.
● Antes de mostrar los resultados se limpia la
caja, dejando el mismo resultado hasta que se
vuelve a pulsar. 
 """

import tkinter as tk
import random

class DadoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Dado")
        self.root.geometry("200x150")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        self.root.eval('tk::PlaceWindow . center')  # Centrar la ventana en la pantalla

        self.resultado_label = tk.Label(root, text="", font=("Helvetica", 48), bg="#f0f0f0")
        self.resultado_label.pack(pady=10)

        self.tirar_boton = tk.Button(root, text="Tirar Dado", command=self.tirar_dado)
        self.tirar_boton.pack(pady=10)

    def tirar_dado(self):
        resultado = random.randint(1, 6)
        self.resultado_label.config(text=str(resultado))

if __name__ == "__main__":
    root = tk.Tk()
    app = DadoApp(root)
    root.mainloop()
# Fin del programa
