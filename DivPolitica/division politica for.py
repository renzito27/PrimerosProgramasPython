#libreria para operar datos xml
import xml.etree.ElementTree as datosXML
class Territorio ():
    #metodo constructor
    def _init_(varClase , valores):
        varClase.campos = ["Codigo","Nombre"]
        varClase.valores = valores
        
    def obtenerRegistro(varClase):
        return dict(zip(varClase.campos,varClase.valores))
        
class Pais(Territorio):
    
    #metodo constructor que altera el heredado
    def _init_(varClase , valores):
        super()._init_(valores)
        varClase.campos.append("CodigoAlfa2")
        varClase.campos.append("CodigoAlfa3")

    def obtener():
        #abrimos el documento xml
        dXML = datosXML.parse("Paises.xml")
        #obtener la lista de nodos
        nodos = dXML.getroot()
        lista = []
        #recorrer las lista de nodos de manera objetual
        for n in nodos:
            p = Pais([n.attrib["Nombre"], n.attrib["Codigo"], n.attrib["CodigoA2"], n.attrib["CodigoA3"]])
            lista.append(p)
        return lista

#programa principal
#obetener la lista de paises
paises = Pais.obtener()
#mostrar los datos del pais en la posicion 30
for i in range(0, len(paises)):
    p = paises[i]
    r = p.obtenerRegistro()
    print("Nombre del Pais:", r["Nombre"],"Codigo ALFA:",r["CodigoALFA2"])
