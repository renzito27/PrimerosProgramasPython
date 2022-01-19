#libreria para operar con cuadros de dialogo
from tkinter import filedialog
from notaMusical import NotaMusical
# ventana para ecoger archivo a reproducir
nombreArchivo = filedialog.askopenfilename()
if len(nombreArchivo) > 0:
    #abrir archivo
    lineasCancion = open(nombreArchivo,"r") #abrir el archivo para solo lectura
    #recorrer las lineas del archivo
    for linea in lineasCancion:
        datos = linea.split(",")
        nm = NotaMusical(datos[0],datos[1])
        print(nm.nota, nm.escala, nm.tiempo)
        nm.reproducir()
        
    
