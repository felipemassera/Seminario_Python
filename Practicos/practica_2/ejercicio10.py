import time

def String_a_List(nombres):
    """ Recibo un string con nombres y lo transformo en una lista  con los mismos nombres"""
    nombres = nombres.replace("\n", "")
    nombres = nombres.replace(" ", "")
    nombres = nombres.replace("'", "")
    return nombres.split(',')

def armar_zip(nombres,notas_1,notas_2):
    """ Recibo 3 listas, las cuales se realiza un procedimiento de merge para generar un diccionario
    cuya clave = nombre y valor= una tupla con notas [nota2,nota2] """
    return{i:(j,k) for i,j,k in zip(nombres,notas_1,notas_2)}
    
def sacar_promedios(diccio):
    """ Recibo un diccionario con nombres y 2 valores por y calculo el promedio por alumno,
    retornando el promedio general del alumno"""
    return map(lambda clave:sum(diccio[clave])/2,diccio)
       
def prom_total(promedios):
    """ Recibo un diccionario con nombres y 2 valores por cada entrada,
    retornando el promedio general del curso (numero  flotante) """
    return (sum(promedios.values())/len(promedios))

def max_prom(promedios):
    """Recibe un diccionario cuyas claves = nombres y sus valores = promedio del alumno,
    retornando el promedio maximo"""
    return max(promedios,key=promedios.get)

def min_nota(diccio):
    """Recibe un diccionario cuyas claves = nombres y sus valores = [nota1,nota2],
    retornando la clave (nombre) de la persona que tenga la menor nota entre las dos listas (nota1 y nota2)"""
    return min(diccio,key=lambda x:min(diccio[x]))   

nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

"""evaluamos tiempo de ejecucion"""
start_time = time.time() 

#inciso 1 armo estructura conjunta entre listas
diccio= armar_zip(String_a_List(nombres),notas_1,notas_2)

#inciso 2 genero un diccionario "nombre" : "nota promedio del alumno"
promedios={i:j for i,j in zip(diccio,sacar_promedios(diccio))}
print('Promedios por alumnos: ',promedios)

#inciso 3
print (f"El promedio total del curso: {prom_total(promedios)}")

#inciso 4
print(f"Alumno con la nota promedio mas alta: {max_prom(promedios)}")

#inciso 5
print(f"Alumno con la nota mas baja: {min_nota(diccio)}")

#aca termina de medir y calcular el tiempo de ejecucion
end_time = time.time()   
elapsed_time = end_time - start_time
print(f"Tiempo de ejecución: {elapsed_time} segundos")