from tkinter import *

# Configuración de la raíz
root = Tk()
root.title("Hola mundo")
root.resizable(1,1)
root.iconbitmap('python.ico')

menubar = Menu(root)
root.config(menu=menubar) #añadir al root por que va en la parte superior

filemenu = Menu(menubar, tearoff=0) #botón principal
#tearoff=0 es para no crear botones vacíos
#elementos en el interior del menú de archivo
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator() # se usa para dar un espacio entre comandos
filemenu.add_command(label="Salir", command=root.quit)#cerrar

editmenu = Menu(menubar, tearoff=0)
#elementos en el interior del menú de edición
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")


helpmenu = Menu(menubar, tearoff=0)
#elementos en el interior del menú de ayuda
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()# se usa para dar un espacio entre comandos
helpmenu.add_command(label="Acerca de...")

#esto es antes de agregar los command's
#establecer los nombres de los menus que aparecerán
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

# Finalmente bucle de la apliación
root.mainloop()

