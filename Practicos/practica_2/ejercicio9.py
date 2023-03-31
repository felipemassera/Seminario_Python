import time
#"""9. Escriba un programa que solicite por teclado una palabra y calcule el valor de la misma dada la siguiente tabla de valores del juego Scrabble:
#|Letra                       |valor|
#|-----                       |-----|
#|A, E, I, O, U, L, N, R, S, T|1|
#|D, G                        |2|
#|B, C, M, P                  |3|
#|F, H, V, W, Y               |4|
#|K                           |5|
#|J, X                        |8|
#|Q, Z                        |10|
#"""


diccio = {
    ("A", "E", "I", "O", "U", "L","N","R","S","T"):1,
    ("D","G"):2,
    ("B", "C", "M", "P" ): 3,
    ("F", "H", "V", "W","Y" ): 4,
    ("K"):5,
    ("J","X"):8,
    ("Q","Z"):10}   

diccio2 = {
    "AEIOULNRST":1,
    "DG":2,
    "BCMP": 3,
    "FHVWY": 4,
    "K":5,
    "JX":8,
    "QZ":10
}

text = input("ingrese una palabra: ").upper()
"""evaluamos tiempo de ejecucion"""
start_time = time.time()

resultado =0
claves=list(diccio2.keys())
for elem in text:
    i=0
    ok=True
    while ((ok)and(i<len(claves))):
        if(elem in claves[i]):
            llave=claves[i]
            ok=False
        i+=1    
    resultado+=diccio2[llave]

print(resultado)

#aca termina de medir y calcular el tiempo de ejecucion
end_time = time.time()   
elapsed_time = end_time - start_time
print(f"Tiempo de ejecución: {elapsed_time} segundos")
