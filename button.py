from tkinter import *

# Configuración de la raíz
root = Tk()
root.title("Hola mundo")
root.resizable(1,1)
root.iconbitmap('python.ico')
root.config(bd=30) #añadirle un borde

def sumar():
	r.set( float(n1.get()) + float(n2.get()) )
	borrar()

def resta():
	r.set( float(n1.get()) - float(n2.get()) )
	borrar()

def producto():
	r.set( float(n1.get()) * float(n2.get()) )
	borrar()

def borrar():
	n1.set("")
	n2.set("")



#variables para  manipular los datos
n1 = StringVar()
n2 = StringVar()
r = StringVar()

#labels y etiquetas
Label(root, text="Número 1").pack()
Entry(root, justify="center", textvariable=n1).pack() # primer numero

Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack() # segundo numero

Label(root, text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack() # resultado

Label(root, text="").pack() #hacer un espacio entre los entry y los botones

#botones a usar
Button(root, text="Sumar", command=sumar).pack(side="left")
Button(root, text="Resta", command=resta).pack(side="left")
Button(root, text="Producto", command=producto).pack(side="left")


# Finalmente bucle de la aplicación
root.mainloop()

