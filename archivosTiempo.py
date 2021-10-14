import copy
from calculoTiempo import crearLista, calculoTiempoOrdenamiento as calculo

if __name__ == "__main__":
    numeroElementos = 2000
    x = 10
    lista = crearLista(numeroElementos)
    listaSeleccion = copy.deepcopy(lista)
    listaInsercion = copy.deepcopy(lista)
    listaQuickSort = copy.deepcopy(lista)
    
    calculo(lista, numeroElementos, x, 'Burbuja', 'Burbuja')
    calculo(listaSeleccion, numeroElementos, x, 'Seleccion', 'Seleccion')
    calculo(listaInsercion, numeroElementos, x, 'Insercion', 'Insercion')
    calculo(listaQuickSort, numeroElementos, x, 'QuickSort', 'QuickSort')