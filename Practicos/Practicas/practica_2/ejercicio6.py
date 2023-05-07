palabra = input("Ingresá una palabra: ")
       
match "a" in palabra , "n" in palabra:
    case True,True : 
        print("Tiene ANbas")
    case True,_ : 
        print("Tiene A pero no N")
    case _,True : 
        print("Tiene N pero no a")
    case _:
     print("no tiene ninguna")
     
#var =(1,1)
#match str(type(var)):
#    case "<class 'int'>":
#        print('es entero')
#    case "<class 'String'>":
#        print('es string')
#    case "<class 'list'>":
#        print('es una Lista')
#    case "<class 'tuple'>":
#        print('es una tupla')
#    case _:
# 
# print('ve tu a saber')