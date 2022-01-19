#libreria para operar datos xml
import xml.etree.ElementTree as datosXML

#abrimos el documento xml
dXML = datosXML.parse("Paises.xml")
#obtener la lista de nodos
nodos = dXML.getroot()

#recorrer las lista de nodos de manera objetual
for n in nodos:
    print(n.attrib["Nombre"])
            
