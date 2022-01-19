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
class Departamento(Territorio):
    def __init__(varClase,valores):
        super().__init__(valores)
        #metodo estatico
    def obtener (codigo=""):
         #abrimos el documento xml
        dXML = datosXML.parse("Departamentos.xml")
        #obtener la lista de nodos
        nodos = dXML.getroot()

        if codigo =="":
            #obtener la lista de deppartamentos
            lista = []
            for n in nodos:
                lista.append(Departamento([n.attrib["Codigo"], n.attrib["Nombre"]]))
            return lista
        else:
            #buscar el pais que corresponda  al codigo
            for n in nodos:
                if n.attrib["Codigo"] == codigo:
                    return Departamento([n.attrib["Codigo"], n.attrib["Nombre"]])
            return None

class Municipio (Territorio):
    def __init__(varClase,valores, codigoDepartamento):
        super().__init__(valores)
        varClase.departamento = Departamento.obtener(codigoDepartamento)
    def obtener(codigo="",codigoDepto=""):
        #abrimos el documento xml
        dXML = datosXML.parse("Municipios.xml")
        #obtener la lista de nodos
        nodos = dXML.getroot()
        if codigo =="":
                #obtener la lista de municipios
            lista = []
            for n in nodos:
                agregar = True
                if codigodepto != "" and n.attrib["CodigoDepartamento"]!=codigoDepto:
                    agregar = False
                if agregar:    
                    m = (Municipio([n.attrib["Codigo"], n.attrib["Nombre"]],\
                                    n.attrib["CodigoDepartamento"])
                    lista.append(m)
            return lista
        else:
            #buscar el pais que corresponda  al codigo
            for n in nodos:
                if n.attrib["CodigoMunicipio"] == codigo:
                    return Municipio([n.attrib["Codigo"], n.attrib["Nombre"]],\
                                   n.attrib["CodigoDepartamento"])
            return None        

#programa principal
codigo = input("Codigo del depto a consultar")
depto = Departamento.obtener(codigo)
if depto != None:
    rd = depto.obtenerRegistro()
    print("Los municipios del Departamento", rd["Nombre"], "son")
    #obtener la lista de municipios para un departamento
    mpios = Municipio.obtener(codigoDepto = rd["Codigo"])
    for m in mpios:
        print(m.obtenerRegistro()["Nombre"]

else:
    print("El departamento con ese codigo no existe")
    
