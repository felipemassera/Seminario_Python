 """PREGUNTA: cuales errores de estilo de pep8 tiene el codigo
 RESPUESTA: El código presentado tiene algunos errores de estilo de acuerdo con las convenciones de PEP 8:
  1# Importaciones en líneas separadas: Según PEP 8, las importaciones deben estar en líneas separadas. 
        Puedes separar las importaciones de json y csv en dos líneas diferentes.
  2# Espacios alrededor de operadores: PEP 8 recomienda agregar espacios alrededor de operadores (=) para mejorar la legibilidad.
        Puedes añadir espacios antes y después de los operadores de asignación en las líneas donde se asignan valores a las variables.
  2# Espacios después de las comas: PEP 8 sugiere agregar un espacio después de las comas en las listas de argumentos o elementos.
        Puedes agregar espacios después de las comas en las llamadas a las funciones dict() y Banda()."""
"""

### Pregunta: Corregir el siguiente programa.

Aquí hay una versión corregida del programa con los posibles errores solucionados: """

import json
import csv
from random import randrange
from clases import Banda

def obtengoDatos():
    opcion = randrange(2)
    Datos = {}  # Definir una variable Datos con un diccionario vacío como valor predeterminado

    if opcion == 0:
        archi = open("datos.json", "r")
        Datos = json.load(archi)
        archi.close()
    elif opcion == 1:
        archi = open("datos.csv", "r")
        csvreader = csv.reader(archi, delimiter=',')
        linea1 = next(csvreader)
        linea2 = next(csvreader)
        Datos = dict(zip(linea1, linea2))
        archi.close()

    return Datos

Datos = obtengoDatos()

banda = Banda(Datos['nombre'], Datos["genero"])

print(banda)
print("FIN DEL PROGRAMA")

""" Recuerda asegurarte de tener el archivo "clases.py" en el mismo directorio que este programa, o bien,
 ajustar la importación de la clase Banda según la estructura de tu proyecto. Además, asegúrate de tener
 los archivos "datos.json" y "datos.csv" en el directorio correcto o proporcionar la ruta correcta a esos archivos."""
 
