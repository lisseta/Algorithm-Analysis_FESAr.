def metodoBurbuja(lista):
    if(type(lista) == list):
        for i in range(1, len(lista)):
            for j in range(0, len(lista) -1):
                if(lista[j] > lista[j + 1]):
                    auxiliar = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = auxiliar
    else:
        print("Te dije que era una lista")

def metodoSeleccion(lista):
    if(type(lista) == list):
        for i in range(0, len(lista)):
            minimo = i
            for j in range(i + 1, len(lista)):
                if(lista[j] < lista[minimo]):
                    minimo = j
            if(i != minimo):
                auxiliar = lista[i]
                lista[i] = lista[minimo]
                lista[minimo] = auxiliar
    else:
        print("Se necesita una lista para funcionar el algoritmo")

def metodoInsercion(lista):
    if(type(lista) == list):
        for i in range(len(lista)):
            for j in range(i, 0, -1):
                if(lista[j - 1] > lista[j]):
                    auxiliar = lista[j]
                    lista[j] = lista[j - 1]
                    lista[j - 1] = auxiliar
    else:
        print("Se necesita una lista para trabajar el metodo")

# def metodoInsercion(lista):
#     for i in range(1, len(lista) -1):
#         auxiliar = lista[i]
#         for j in range(i - 1, (j >= 0 and lista[j] > auxiliar), -1):
#             lista[j + 1] = lista[j]
#             lista[j] = auxiliar

def metodoQuickSort(lista, izquierdo, derecho):
    if(type(lista) == list and type(izquierdo and derecho) == int):
        pivote = lista[izquierdo]
        i = izquierdo
        j = derecho
        
        while (i < j):
            while (lista[i] <= pivote and i < j):
                i += 1
            
            while (lista[j] > pivote):
                j -= 1
            
            if(i < j):
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
        
        lista[izquierdo] = lista[j]
        lista[j] = pivote
        
        if(izquierdo < j - 1):
            metodoQuickSort(lista, izquierdo, j - 1)
        
        if(j + 1 < derecho):
            metodoQuickSort(lista, j + 1, derecho)
    else:
        print("Se necesita una lista para trabajar el metodo")

# Segundo metodo de QuickSort
def metodoQuickSortDos(lista):
    izquierda = []
    centro = []
    derecha = []
    
    if(len(lista) >  1):
        pivote = lista[0]
        for i in lista:
            if(i < pivote):
                izquierda.append(i)
            elif (i == pivote):
                centro.append(i)
            elif(i > pivote):
                derecha.append(i)
        return metodoQuickSortDos(izquierda) + centro + metodoQuickSortDos(derecha)
    else:
        return lista

#Tercer metodo QuickSort
def particionLista(lista, menor, mayor):
    pivote = lista[menor]
    left = menor
    right = mayor
    
    while True:
        while left <= right and lista[left] <= pivote:
            left += 1
        while left <= right and lista[right] >= pivote:
            right -= 1
        
        if right < left:
            break
        else:
            lista[left], lista[right] = lista[right], lista[left]
    lista[menor], lista[right] = lista[right], lista[menor]
    return right

def metodoQuickSortTres(lista, menor, mayor):
    if(menor < mayor):
        pivote = particionLista(lista, menor, mayor)
        metodoQuickSortTres(lista, menor, pivote - 1)
        metodoQuickSortTres(lista, pivote + 1, mayor)


if __name__ == "__main__":
    lista = [34, 5, 23, 98, 557, 34]
    metodoQuickSortTres(lista, 0, len(lista) - 1)
    print(lista)