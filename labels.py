from tkinter import *

# Configuración de la raíz
root = Tk()
root.title("Hola mundo")
root.resizable(1,1)
root.iconbitmap('python.ico')

texto = StringVar()
texto.set("Un nuevo texto")

#comando place para acomdar el texto por medio de coordenadas
#label = Label(root, text="Hola Mundo")
#label.place(x=200,y=200)

#acomodo con pack
"""Label(root, text="¡Hola mundo!").pack(anchor="nw")
label = Label(root, text="¡Otra etiqueta!")
label.pack(anchor="center")
Label(root, text="¡Última etiqueta!").pack(anchor="se")

label.config(bg="green", fg="blue", font=("Verdana",24))
label.config(textvariable=texto)"""

#cambiar texto por imagen
imagen = PhotoImage(file="python.png")
Label(root, image=imagen, bd=0).pack(side="left")

# Finalmente bucle de la aplicación
root.mainloop()

