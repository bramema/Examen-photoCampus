import json
def leerArchivo(ruta):
    try:
        with open(ruta,"r")as file:
            return json.load(file)
    except Exception:
        return []
    
def guardarArchivo(ruta,datos):
    with open(ruta,"w")as file:
        json.dump(datos,file,indent=4)

def registrarPaquete(listaPaquetes):
    diccionarioPaquetes = {
        "Nombre":input("digite nombre: "),
        "Cantidad":input("digite el numero de fotos: "),
        "Precio":input("digite precio: "),
        "Duracion":input("digite la duracion en horas: ")
    }
    listaPaquetes.append(diccionarioPaquetes)
    guardarArchivo("Paquetes.json",listaPaquetes)
    return listaPaquetes