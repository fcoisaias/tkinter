from tkinter import *

# Configuración de la raíz
root = Tk()
root.title("Hola mundo")
root.resizable(1,1)
root.iconbitmap('python.ico')



texto = Text(root)
texto.pack()
texto.config(width=30, height=10, font=("Comic Sans MS",15), padx=15, pady=15, selectbackground="red")
#width caracteres por renglón
#height renglones disponibles visibles

# Finalmente bucle de la aplicación
root.mainloop()