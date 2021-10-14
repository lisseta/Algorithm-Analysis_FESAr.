# Solución para el problema N° 3 de Diseño y Análisis de Algoritmos
# Autor: SouYui

from swap import swap, factorial
import copy

# ! Requiere dos tuplas de numeros enteros las cuales significaran puntos de un plano cartesiano
# R Mide la distancia entre dos puntos y los devuelve en una tupla 
#   de distancia hacia la derecha y distancia hacia arriba 
#   en los resltados right y up
def distancia_puntos(puntoInicial, puntoFinal):
    xInicial, yInicial = puntoInicial
    xFinal, yFinal = puntoFinal
    
    right = 0
    up = 0
    
    if(xFinal > xInicial):
        if(yFinal > yInicial):
            right = xFinal - xInicial
            up = yFinal - yInicial
        else:
            print("La posición no es válida, verifique su entrada")
    else:
        print("La posición no es válida, verifique su entrada")
    
    return (right, up)

# ! Requiere las distancias de movimientos a la derecha y hacia arriba en int
# R Crea una lista de elementos para crear las permutaciones
#   devolviendo con n cantidad de 1's para movimientos hacia la derecha
#   y n 2's para movimientos hacia arriba que son proporcionados por <<distancia_puntos>>
def lista_elementos(distanciaX, distanciaY):
    listaResult = []
    
    if(type(distanciaX) == int and type(distanciaY) == int):
        for i in range(distanciaX):
            # 1 es igual a un movimiento a la derecha
            listaResult.append(1)
        for i in range(distanciaY):
            # 2 es igual a un movimiento a la izquierda
            listaResult.append(2)
        return listaResult
    else:
        print("Error de datos, verifique su entrada.")

# ! Requiere una lista de elementos con elementos 1's y 2's
# R Crea una lista de todas las permutaciones posibles para los caminos a tomar por el usuario
#   de caminos hasta llegar a un punto dado
def permutaciones(n):
    s = []
    listaF=[]
    for i in n:
        s.append(i)
    listaF.append(list(s))
    for i in range(1, factorial(len(n))):
        m = len(n) - 2
        while (s[m] >= s[m + 1]):
            m = m - 1
        k = len(n) - 1
        while(s[m] >= s[k]):
            k = k - 1
        swap(s, m, k)
        p = m + 1
        q = len(n) - 1
        while(p < q):
            swap(s, p, q)
            p = p + 1
            q = q - 1
        if(s not in listaF):
            listaF.append(list(s))
    return listaF

# ! Requiere una lista de permutaciones con numeros 1 y 2
# R Cambia cada elemento para darlo con "r" para
#   movimientos hacia la derecha y "u" para movimientos hacia arriba
def cambio_usuario(listaPermutaciones):
    if(type(listaPermutaciones) == list):
        listaResult = []
        for lista in listaPermutaciones:
            for index, value in enumerate(lista):
                if(value == 1):
                    lista[index] = "r"
                if(value == 2):
                    lista[index] = "u"
            listaResult.append(lista)
        return listaResult
    else:
        print("No es una lista, verifique su entrada.")

# ! Requiere dos tuplas de numeros enteros las cuales significaran puntos de un plano cartesiano
# R Devuelve una cadena con todas las permutaciones de todos los caminos a tomar
#   ordenados desde el primero hasta los n con su numeracion
def caminos_dos_puntos(puntoInicial, puntoFinal):
    x, y = distancia_puntos(puntoInicial, puntoFinal)
    lista = lista_elementos(x, y)
    listaPermutaciones = permutaciones(lista)
    listaCambio = copy.deepcopy(listaPermutaciones)
    resultCambio = cambio_usuario(listaCambio)
    
    solucion = "Caminos posibles a tomar de " + str(puntoInicial) + " a " + str(puntoFinal) + ": \n"
    for index, value in enumerate(resultCambio):
        solucion += str(index) + " - " + str(value) + "\n"
    
    return solucion


# -------------------- Prueba -----------------
puntoUno = (5, 3)
puntoDos = (8, 8)

result = caminos_dos_puntos(puntoUno, puntoDos)
print(result)