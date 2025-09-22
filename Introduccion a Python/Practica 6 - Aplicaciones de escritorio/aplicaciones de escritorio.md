# Aplicaciones de escritorio

Las aplicaciones de escritorio son programas que se ejecutan en el sistema operativo de una computadora y proporcionan una interfaz gráfica de usuario (GUI) para interactuar con el usuario. Python ofrece varias bibliotecas para crear aplicaciones de escritorio, siendo las más populares Tkinter, PyQt y Kivy.

## Tkinter
Tkinter es la biblioteca estándar de Python para crear interfaces gráficas de usuario. El módulo Tkinter es un paquete GUI (interfaz gráfica de usuario) que trabaja con el paradigma de orientación a objetos.
Viene incluida con la instalación de Python, por lo que no necesitas instalar nada adicional para usarla. Aquí hay un ejemplo básico de una aplicación Tkinter:

```python

import tkinter as tk
from tkinter import messagebox


def on_button_click():
    messagebox.showinfo("Mensaje", "¡Hola, mundo!")

# Crear la ventana principal
root = tk.Tk()
# Configurar la ventana
root.title("Aplicación Tkinter")
# Crear un botón
button = tk.Button(root, text="Haz clic aquí", command=on_button_click)
# Empaquetar el botón en la ventana
button.pack()
# Iniciar el bucle principal de la aplicación
root.mainloop()


```


El sistema de geometría en tkinter también se basa en objetos. Los gestores de geometría como pack(), grid() y place() son métodos que pertenecen a cada widget y determinan cómo se organizan en la ventana. 



















## PyQt
PyQt es un conjunto de enlaces de Python para la biblioteca Qt, que es una biblioteca popular para crear interfaces gráficas de usuario. PyQt ofrece una amplia gama de widgets y herramientas para desarrollar aplicaciones complejas. Para usar PyQt, primero debes instalarlo:

```pip install PyQt5
```
Aquí hay un ejemplo básico de una aplicación PyQt:

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
def on_button_click():
    QMessageBox.information(window, "Mensaje", "¡Hola, mundo!") 
# Crear la aplicación
app = QApplication(sys.argv)
# Crear la ventana principal
window = QWidget()
window.setWindowTitle("Aplicación PyQt")
# Crear un botón
button = QPushButton("Haz clic aquí", window)
button.clicked.connect(on_button_click)
button.resize(100, 30)
button.move(50, 50)
# Mostrar la ventana
window.show()
# Iniciar el bucle principal de la aplicación
sys.exit(app.exec_())
```

## Kivy
Kivy es una biblioteca de código abierto para desarrollar aplicaciones multitáctiles y de interfaz gráfica de usuario. Es especialmente útil para crear aplicaciones que funcionen en múltiples plataformas, incluyendo Windows, macOS, Linux, iOS y Android. Para usar Kivy, primero debes instalarlo:

```pip install kivy
```
Aquí hay un ejemplo básico de una aplicación Kivy:

```python
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
class MyApp(App):
    def build(self):
        button = Button(text="Haz clic aquí")
        button.bind(on_press=self.on_button_click)
        return button
    def on_button_click(self, instance):
        instance.text = "¡Hola, mundo!"
if __name__ == "__main__":
    MyApp().run()
```
## Conclusión
Estas son solo algunas de las bibliotecas disponibles para crear aplicaciones de escritorio en Python. Dependiendo de tus necesidades y preferencias, puedes elegir la que mejor se adapte a tu proyecto. Cada una de estas bibliotecas tiene su propia documentación y comunidad, lo que facilita el aprendizaje y la resolución de problemas.

## Recursos Adicionales
- [Documentación de Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Documentación de PyQt](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [Documentación de Kivy](https://kivy.org/doc/stable/)
- [Tutorial de Tkinter en Real Python](https://realpython.com/python-gui-tkinter/)
- [Tutorial de PyQt en ZetCode](https://zetcode.com/gui/pyqt5/)
- [Tutorial de Kivy en Kivy.org](https://kivy.org/doc/stable/gettingstarted/intro.html)