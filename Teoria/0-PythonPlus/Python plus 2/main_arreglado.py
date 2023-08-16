import json
import csv
from random import randrange
import clases


def obtengoDatos():
    """Funcion que abre el archivo (csv o json) al azar, y retorna los
        datos en forma de diccionario"""

    opcion = randrange(2)
    try:
        if opcion == 0:
            archi = open("datos.json", "r")
            datos = json.load(archi)
            archi.close()
        elif opcion == 1:
            archi = open("datos.csv", "r")
            csvreader = csv.reader(archi, delimiter=",")
            linea1 = next(csvreader)
            linea2 = next(csvreader)
            datos = dict(zip(linea1, linea2))
            archi.close()
        else:
            datos = {}
        return datos
    except (FileNotFoundError, PermissionError):
        raise (FileNotFoundError)


try:
    datos = obtengoDatos()
    try:
        banda = clases.Banda(datos["nombre"], datos["genero"])
        print(banda)
    except KeyError:
        print("La clave no existe")
    print("FIN DEL PROGRAMA")
except FileNotFoundError:
    print("Archivo no encontrado.")
