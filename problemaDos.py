# Solución para el problema N° 2 de Diseño y Análisis de Algoritmos
# Autor: Sou - Wendy

def suma_maxima(lista):
    tabla = [0] * len(lista)
    for i in range(len(lista)):
        tabla[i] = [0] * len(lista)
    #Metemos los datos al arreglo
    for i in range(len(lista)):
        for j in range(0, i):
            tabla[i][j] = tabla[i - 1][j] + lista[i]
        tabla[i][i] = lista[i]  
    #Buscamos la suma que sea mas larga
    maximo = tabla[0][0]
    indiceUno = 0
    indiceDos = 0
    for i in range(len(lista)):
        for j in range(len(lista)):
            if (tabla[i][j] > maximo):
                maximo = tabla[i][j]
                indiceUno = i
                indiceDos = j
    return(maximo, indiceUno, indiceDos)

def suma_maxima_sec(lista):
    tabla = [0] * len(lista)
    for i in range(len(lista)):
        tabla[i] = [0] * len(lista)
    sumaS = [0] * len(lista)
    for i in range(len(lista)):
        sumaS[i] = [0] * len(lista)
    maximo = 0
    indiceUno = 0
    indiceDos = 0
    for i in range(len(lista)):
        for j in range(i):
            sumaS[i][j] = sumaS[i - 1][j] + lista[i]
            if(sumaS[i][j] > maximo):
                maximo = sumaS[i][j]
                indiceDos = j
                indiceUno = i
        sumaS[i][i] = lista[i]
        if(sumaS[i][i] > maximo):
            maximo = sumaS[i][i]
            indiceUno = i
            indiceDos = i
    return(maximo, indiceUno, indiceDos)

def suma_maxima_terc(lista):
    tabla = [0] * len(lista)
    for i in range(len(lista)):
        tabla[i] = [0] * len(lista)
    #Metemos los datos al arreglo
    for i in range(len(lista)):
        for j in range(0, i):
            tabla[i][j] = tabla[i - 1][j] + lista[i]
        tabla[i][i] = lista[i]
    #Buscamos la suma que sea mas larga
    maximo = 0
    suma = 0
    indiceUno = 0
    indiceDos = 0
    for i in range(len(lista)):
        if(suma + lista[i] > 0):
            suma = suma + lista[i]
        else:
            suma = 0
            indiceUno = i + 1
        if(suma > maximo):
            maximo = suma
            indiceDos = i
    return(maximo, indiceDos, indiceUno)

# -------------------- Prueba -----------------
data = [27, 6, -50, 21, -3, 14, 16, -8, 42, 33, -21, 9]
maximo, indiceDos, indiceUno = suma_maxima(data)
print("La suma maxima es:", maximo, " del segmento de la lista:", data[indiceUno:indiceDos + 1])