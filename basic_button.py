from tkinter import *

# Configuración de la raíz
root = Tk()
root.title("Hola mundo")
root.resizable(1,1)
root.iconbitmap('python.ico')

def crear_label():
	Label(root,text="Label o etiqueta automática").pack()


Button(root,text="Da clic en este botón",command=crear_label).pack()

# Finalmente bucle de la aplicación
root.mainloop()
