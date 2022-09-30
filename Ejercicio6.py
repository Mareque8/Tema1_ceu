el = [1,5,-2]
lista = []

def agregar_una_vez(lista,el):
    if el in lista:
        raise ValueError("ERROR: Imposible añadir elementos duplicados => [{}}]".format(el))
    lista.append(el)

try:
    agregar_una_vez(el,10)
    agregar_una_vez(el, -2)
except ValueError:
    print("ERROR")
else:
    print("Elemento guardado")
finally:
    print("La lista final es {}".format(el))

agregar_una_vez(lista,el)




