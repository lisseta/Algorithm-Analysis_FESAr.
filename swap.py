def factorial(valor):
    bandera = 1
    primera = 1
    segunda = 2
    while bandera < valor:
        primera = primera * segunda
        segunda = segunda + 1
        bandera = bandera + 1
    return(primera)

def swap(lista, indiceUno, indiceDos):
    auxi = lista[indiceUno]
    lista[indiceUno] = lista[indiceDos]
    lista[indiceDos] = auxi

