word='ANANA'
for valor in (word):      
    print(valor)
casa='casita que te quiero linda'
print(casa.strip(""))#elimina lo buscado en una cadena de caracteres

intentos = 5
print('Hola {} !!! Ganaste! y necesitaste {} intentos!!!'.format("Lionel", intentos))

num="4-7-10-13-16-19-22-25-28-31-34-37-40-43-46-49-52-55-58-61-64-67-70-73-76-79-82-85-88-91-94-97-100-103-106-109-112-115-118-121-124-1"
nue_num= num.split('-')
nue=[]
for elem in nue_num:
    nue.append(int(elem))
print(sum(nue))
print(sum(nue)/len(nue))

        
print("END CODE".center(60,"*")) #centra y muestra la cadena