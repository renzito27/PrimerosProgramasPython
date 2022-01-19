#libreria para operar datos xml
import xml.etree.ElementTree as datosXML
class Territorio ():
    #metodo constructor
    def __init__(varClase , valores):
        varClase.campos = ["Codigo","Nombre"]
        varClase.valores = valores
        
    def obtenerRegistro(varClase):
        return dict(zip(varClase.campos,varClase.valores))
        
class Pais(Territorio):
    
    #metodo constructor que altera el heredado
    def __init__(varClase , valores):
        super().__init__(valores)
        varClase.campos.append("CodigoAlfa2")
        varClase.campos.append("CodigoAlfa3")

    def obtener(codigo=""):
        #abrimos el documento xml
        dXML = datosXML.parse("Paises.xml")
        #obtener la lista de nodos
        nodos = dXML.getroot()
        if codigo == "":
            
            lista = []

            #recorrer las lista de nodos de manera objetual
            for n in nodos:
                p = Pais([n.attrib["Codigo"], n.attrib["Nombre"], n.attrib["CodigoA2"], n.attrib["CodigoA3"]])
                lista.append(p)
            return lista
        else:
            #buscar el pais que corresponda  al codigo
            for n in nodos:
                if n.attrib["Codigo"] == codigo:
                    return Pais([n.attrib["Codigo"], n.attrib["Nombre"], n.attrib["CodigoA2"], n.attrib["CodigoA3"]])
                return None

#programa principal
#obetener la lista de paises
paises = Pais.obtener()
#mostrar los datos del pais en la posicion 30 
r = paises[30].obtenerRegistro()
print("Nombre del Pais:", r["Nombre"],"Codigo Alfa:", r["CodigoAlfa2"])
