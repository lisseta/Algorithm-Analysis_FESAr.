# ! Requiere una lista de datos de tipo int
# R Devuelve la lista de datos ordenada de manera ascendente
def metodoBurbuja(lista):
    if(type(lista) == list):
        for i in range(1, len(lista)):
            for j in range(0, len(lista) -1):
                if(lista[j] > lista[j + 1]):
                    auxiliar = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = auxiliar
    else:
        print("Te dije que era una lista guey")

# ! Requiere una lista de datos de tipo int
# R Devuelve la lista de datos ordenada de manera ascendente
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

# ! Requiere una lista de datos de tipo int
# R Devuelve la lista de datos ordenada de manera ascendente
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

# ! Requiere una lista de datos de tipo int, 
#   un indice para clasificar el punto menor para el ordenamiento de la lista 
#   y un índice mayor para ordenar la lista como límite final
# R Devuelve la lista de datos ordenada de manera ascendente
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

if __name__ == "__main__":
    lista = [34, 5, 23, 98, 557, 34, 2, 3, 5, 1, 1, 1, 5, 89, 200, 325, 200, 125, 65, 75, 90, 65, 65]
    metodoQuickSort(lista, 0, len(lista) - 1)
    print(lista)