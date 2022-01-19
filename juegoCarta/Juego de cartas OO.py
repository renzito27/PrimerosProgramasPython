#importar la libreria para interfaces graficas

from tkinter import*
#importar caja de mensajes
from tkinter import messagebox
#imoortar la libreria para pestañas
from Jugador import Jugador
from tkinter.ttk import Notebook
from Enumerados import *
v = Tk()
v.title("Juego del apuntado")
v.minsize(width=300, height =200)
#crear el menu principal
mnuP= Menu(v)
#agregar ventana
v.config(menu = mnuP)
j1 = Jugador()
j2 = Jugador()
def repartir():
    global j1 , j2
    j1.repartir
    j2.repartir
    j1.mostrar(f1)
    j2.mostrar(f2)
   
   #messagebox.showinfo("Probando Menu", "Hizo clic en REPARTIR")

def verificar():
    global j1,j2
    if nbJ.index(nbJ.select()) == 0:
        messagebox.showinfo("", j1.verificar())
    elif messagebox.showinfo("", j2.verificar()) 
def salir():
    v.destroy()
    quit()
#opciones del menu
mnuJ = Menu(mnuP)
mnuJ.add_command(label="Repartir",command=repartir)
mnuP.add_command(label="Verificar",command=verificar)
mnuP.add_cascade(label="Juego", menu=mnuJ)

mnuP.add_command(label="Salir", command = salir)

#definir las pestañas
nbJ= Notebook(v)
#expande toda la ventana
nbJ.pack(fill="both", expand="yes")

f1 = Frame (nbJ, bg="green") 
f2 = Frame (nbJ,bg="lightblue")

nbJ.add(f1,text="Martin Estrada Contreras")
nbJ.add(f2, text="Raul Vidal")

