import string
"""7. Dada una frase identificar mayúsculas, minúsculas y caracteres no letras y contar la cantidad de palabras sin distinguir entre mayúsculas y minúsculas, en la frase."""
texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que el de una mujer es de $45.000. Además, las mujeres tienen menos posibilidades de acceder a puestos de liderazgo en las empresas.
  """
#NO SE ENTIENDE LA CONSIGNA


"""LISTO LAS PALABRAS MAY, MIN y ESP"""  
text_split= texto.split() 
lista_minuscula= []
lista_mayuscula= []
lista_especial= []
upper = []
lower = []
chars = []

for elem in text_split:    
    if elem[0] in string.ascii_lowercase:
        lista_minuscula.append(elem)
    elif elem[0] in string.ascii_uppercase:
        lista_mayuscula.append(elem)
    else:
        lista_especial.append(elem)        

"""separamos las letras y las contabilizamos de otra manera"""
for word in text_split:
    for letter in word:
        if letter.isupper():
            upper.append(letter)
        elif letter.islower():
            lower.append(letter)
        else:
            chars.append(letter)

print(f"Minuscula: {(lista_minuscula)}")    
print(f"Mayuscula: {(lista_mayuscula)}")    
print(f"Especial: {(lista_especial)}")    
print(F"Cantidad de palabras totales {len(text_split)} sin caracteristicas especiales: {len(lista_minuscula)+len(lista_mayuscula)}")
print(f"Palabras Minusculas: {len(lista_minuscula)}, Letras Minusculas {len(lower)}")    
print(f"Palabras Mayuscula: {len(lista_mayuscula)}, Letras Mayusculas {len(upper)}")    
print(f"Palabras Especial: {len(lista_especial)}, Letras Especiales {len(chars)}")
