from tkinter import *

# Configuración de la raíz
root = Tk()
root.title("Hola mundo")
root.resizable(1,1)
root.iconbitmap('python.ico')

"""
#colocar con frame para que no se sobreescriban
frame=Frame(root)
frame.pack()

label1 = Label(frame,text="Nombre")
label1.pack(side="left")

caja1=Entry(frame)
caja1.pack(side="right")

frame2=Frame(root)
frame2.pack()

label2 = Label(frame2,text="Contraseña")
label2.pack(side="left")

caja2=Entry(frame2)
caja2.pack(side="right")"""

#usando grid()

label = Label(root, text="Nombre muy largo")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="normal")

label2 = Label(root, text="Contraseña")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="center", show="?")

#pad  se refiere al margen de X y Y 
#sticky pegado del widget a un lado (norte, sur, este y oesta N S E W)
#show mostrar caracteres o mostrar simbolos
#state activado o desactivado
# justify alinear a la izquierda , derecha o centro

# Finalmente bucle de la apliación
root.mainloop()

