from tkinter import *

def seleccionar():
	monitor.config(textvariable=opcion)

def reset():
	opcion.set(" ")

# Configuración de la raíz
root = Tk()
root.title("Hola mundo")
root.resizable(1,1)
root.iconbitmap('python.ico')
root.config(bd=30) #añadirle un borde

opcion = IntVar()

Radiobutton(root, text="Opción 1", variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(root, text="Opción 2", variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(root, text="Opción 3", variable=opcion, value=3, command=seleccionar).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()

# Finalmente bucle de la apliación
root.mainloop()

