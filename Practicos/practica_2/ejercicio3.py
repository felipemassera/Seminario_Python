import string
"""3. Dado el siguiente texto guardado en la varible *jupyter_info*,  solicite por teclado **una letra** e imprima las palabras que
comienzan con dicha letra. En caso que no se haya inrgesado un letra, indique el error. *Ver: módulo string*
"""

jupyter_info = """ JupyterLab is a web-based interactive development environment for Jupyter notebooks, 
code, and data. JupyterLab is flexible: configure and arrange the user interface to support a wide range 
of workflows in data science, scientific computing, and machine learning. JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing ones.
"""
list= jupyter_info.lower().split()

char = input("**insert one char:**")
if (len(char)==1)and(char in string.ascii_letters) :
    for elem in list:
        if elem.startswith(char):
            print(elem)
else:
   print("*See: String module*")

