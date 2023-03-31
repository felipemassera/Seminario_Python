import time
import string
"""8. Escriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la misma es un [Heterograma](https://es.qaz.wiki/wiki/Isogram) (tenga en cuenta que el contenido del enlace es una traducción del inglés por lo cual las palabras que nombra no son heterogramas en español). Un Heterograma es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres.

**Tener en cuenta**
- Lo que no se puede repetir en la frase son sólo aquellos caracteres que sean letras.
- No se distingue entre mayúsculas y minúsculas, es decir si en la frase o palabra tenemos la letra "T" y la letra "t" la misma NO será un Hererograma.
- Para simplificar el ejercicio vamos a tomar como que las letras con tilde y sin tilde son distintas. Ya que Python las diferencia:

**Ejemplos**
|Entreda|¿Heterograma?|
|-----|-----|
|cruzamiento|Sí|
|centrifugados|Sí|
|portón|Sí|
|casa|No|
|día de sol|No|
|con diez uñas|Sí|
|no-se-duplica|Sí|"""

letras = string.ascii_lowercase

is_heterogram = input("Insert a word: ")
#is_heterogram = "Melvin Schwarzkopf"

"""evaluamos tiempo de ejecucion"""
start_time = time.time() 

is_heterogram.lower()
i=0
ok=True
while ok and i<len(letras):
   if (is_heterogram.count(letras[i])>1):
       ok= False
   i+=1    
print('Es heterograma')if ok else print('No Es heterograma')

#aca termina de medir y calcular el tiempo de ejecucion
end_time = time.time()   
elapsed_time = end_time - start_time
print(f"Tiempo de ejecución: {elapsed_time} segundos")



#for char in is_heterogram.lower(): #divido la palabra en letras
#    if char.lower
#    
#    print(char)
    
    
    