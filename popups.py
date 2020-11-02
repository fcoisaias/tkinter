from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()
root.title("Hola mundo")
root.resizable(1,1)
root.iconbitmap('python.ico')


def test():
	# MessageBox.showinfo("Hola!","Hola mundo")
	# MessageBox.showwarning("Alerta","Sección sólo para administradores.")
	# MessageBox.showerror("Error!","Ha ocurrido un error inesperado.")
	# resultado = MessageBox.askquestion("Salir","¿Está seguro que desea salir sin guardar?")
	# if resultado == "yes":  # "no"
	#	root.destroy()
	# resultado = MessageBox.askokcancel("Salir","¿Sobreescribir el fichero actual?")
	# resultado = MessageBox.askyesno("Salir","¿Está seguro que desea salir sin guardar?")
	#if resultado:
	#	root.destroy()
	#resultado = MessageBox.askretrycancel("Reintentar","No se puede conectar")
	#if resultado:
	#	root.destroy()
	
	#popups avanzados
	#color = ColorChooser.askcolor(title="Elige un color")
	#print(color) #comprobar lo que devuelve
	

	#ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:", 
	#	filetypes=(("Fichero de texto","*.txt"),
	#		("Fichero de texto avanzado","*.txt2"),
	#		("Todos los ficheros","*.*")) )

	fichero = FileDialog.asksaveasfile(title="Guardar un fichero", mode="w", defaultextension=".txt") 
	if fichero is not None:
		fichero.write("Hola!")
		fichero.close()


Button(root, text="Haz clic", command=test).pack()


# Finalmente bucle de la apliación
root.mainloop()