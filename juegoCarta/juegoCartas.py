from tkinter import*

import random

v = Tk()

v.configure(background="green")

def repartir ():

    f = 1
    c = 0

    for i in range (0, 53):
    
    
        #generar numero aleatorio
        nc = random.randrange(1, 53)
        #cargar imagen
        imgCarta = PhotoImage(file="CARTA"+ str(nc)+".gif")
        #mostrar imagen

        lbl=Label(v)
        lbl.configure(image=imgCarta)
        lbl.grid(row=f, column=c)
        lbl.image=imgCarta

        #ajustar coordenadas

        c += 1
        if c>=10:
            f+=1
            c=0
        
Button(v, text="repartir", command=repartir).grid()
