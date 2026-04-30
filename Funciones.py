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