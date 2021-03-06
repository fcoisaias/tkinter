from tkinter import *

# Configuración de la raíz
root = Tk()
root.title("Hola mundo")
root.resizable(1,1)
root.iconbitmap('python.ico')


#principales propiedades del frame
frame = Frame(root, width=480, height=320) #tamaño

#pack se refiere a que se distribuya dentro de la raíz
frame.pack() #por default alinea arriba y al medio
#frame.pack(side="top",anchor="center") #alinear a un lado y anclar
#frame.pack(fill='both', expand=1) #como se distribuye dentro del root expand 1 true 0 false

frame.config(cursor="pirate") #tipo de cursor del mouse
frame.config(bg="lightblue") #Color de fondo
frame.config(bd=25) #tamaño de borde
frame.config(relief="sunken") #estilo de relieve

#mismas propiedades visuales en root
root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")


# Finalmente bucle de la aplicación
root.mainloop()