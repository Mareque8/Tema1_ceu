def separar(lista):

    pares = []
    impares = []
    for i in lista:
        if i%2 == 0:
            pares.append(i)
        else: 
            impares.append(i)
       
    pares.sort()
    impares.sort()

    return pares,impares
lista = [5,7,1,3,2,4,9,6,8]
pares,impares = separar(lista)
print ("pares: ", pares)
print ("impares: ", impares)