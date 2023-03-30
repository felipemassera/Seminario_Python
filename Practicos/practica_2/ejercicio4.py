"""4. Para la aceptación de un artículo en un congreso se definen las siguientes especificaciones que deben cumplir y 
recomendaciones de escritura:

**título**: 10 palabras como máximo
cada oración del **resumen**:
    * hasta 12 palabras: fácil de leer
    * entre 13-17 palabras:  aceptable para leer
    * entre 18-25 palabras: difícil de leer
    * mas de 25 palabras: muy difícil

Dado un artículo en formato string, defina si cumple las especificaciones del título y cuántas oraciones tiene de cada categoría. 
El formato estándar en que recibe el string tiene la siguiente forma:
```Python"""
evaluar = """título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources provides the promise of capturing unprecedented details of large-scale complex systems. However, the specialized knowledge required for developing such ABMs creates barriers to wider adoption and utilization. Here we present our experiences in developing an initial implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our experiences in developing ABM toolkits, including Repast for High Performance Computing (Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling system that can exploit the largest HPC resources and emerging computing architectures.
"""
easy=0
normal=0
hard=0
very_hard=0
max_title_words = 10
title_words=len(evaluar.split("\n")[0].split(": ")[1].split(" "))

if title_words > max_title_words:
    print("wrong title, is too large")
else:
    print("your title is OK")
    
lines= evaluar.split("\n")[1].split(": ")[1].split(".")
print(lines)
for elem in lines : 
    words_lines= len(elem.split(" "))
    if words_lines>25:
        very_hard+=1
    elif words_lines<=25 and words_lines>17:
        hard+=1
    elif words_lines <= 17 and words_lines > 12:
        normal+=1
    else:    
        easy+=1
    
    
    #match words_lines:
    #    case count if (count <= 12):
    #        easy+=1
    #    case count if (count >12) and (count <=17):
    #        normal+=1       
    #    case count if (count > 17) and (count <= 25):
    #        hard+=1
    #    case count if (count>25):
    #        very_hard +=1 
            
print(f"the text have {len(lines)} lines. Easy: {easy} Normal:{normal} , Hard:{hard} , Very Hard: {very_hard}")