# cargar la libreria para GUI
from tkinter import *

from tkinter import messagebox

#importar libreria para calculos con números reales
import math

#importar libreria para calculos matematicos con numeros imaginarios o complejos

import cmath

V= Tk()
V.title("Raices ecuación cuadrática")
#V.minsize(width=300, heigth=200)


txtA = Entry(V, width = 10)
txtA.grid(row=0, column=1)
txtB = Entry(V, width = 10)
txtB.grid(row=1, column=1)
txtC = Entry(V, width = 10)
txtC.grid(row=2, column=1)

Label (V, text =" Coeficiente A :").grid(row=0, column=0)
Label (V, text =" Coeficiente B :").grid(row=1, column=0)
Label (V, text =" Coeficiente C :").grid(row=2, column=0)

Label (V, text="Raiz x1").grid(row=4,column=0)
Label (V, text="Raiz x2").grid(row=5,column=0)

txtx1 = Entry(V, width=30)
txtx1.grid(row=4, column=1)
txtx1.configure(state=DISABLED)
txtx2 = Entry(V, width=30)
txtx2.grid(row=5, column=1)
txtx2.configure(state=DISABLED)

def calcularRaices():
    #obtener datos de entrada
    a=float(txtA.get())
    b=float(txtB.get())
    c=float(txtC.get())
    #proceso
    if a!=0:
        r = b ** 2 - 4 * a * c
        if r > 0:
            x1 = (-b + math.sqrt (r)) / (2*a)
            x2 = (-b - math.sqrt (r)) / (2*a)
        else:
            x1 = (-b + cmath.sqrt (r)) / (2*a)
            x2 = (-b - cmath.sqrt (r)) / (2*a)
        txtx1.configure(state=NORMAL)
        txtx1.delete(0,END)
        txtx1.insert(0,str(x1))
        txtx1.configure(state=DISABLED)

        txtx2.configure(state=NORMAL)
        txtx2.delete(0,END)
        txtx2.insert(0,str(x2))
        txtx2.configure(state=DISABLED)

        
    else:
        messagebox.showerror ("error al calcular","la ecuación no es cuadrática")

        
    
Button(V, text="Calcular",command=calcularRaices ).grid(row=3, column=0, columnspan=2)   
