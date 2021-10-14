import random as rn
import copy
from time import time
import metodosOrdenamiento as metodos

def crearLista(longitud):
    lista = []
    for i in range(0, longitud):
        lista.append(rn.randint(0, 200))
    return lista

def calculoTiempoOrdenamiento(lista, numeroElementos , x, metodoOrdenamiento, nombreArchivo, menorQuick = 0, mayorQuick = 0):
    if(type(lista) == list and type(numeroElementos) == int and type(x) == int and type(metodoOrdenamiento) == str and type(nombreArchivo) == str):
        archivo = open(nombreArchivo+".csv", "w")
        archivo.write("N,Tiempo\n")
        salto = x
        
        for i in range(x, numeroElementos, x):
            listaNueva = copy.deepcopy(lista[:x])
            inicioTiempo = time()
            if(metodoOrdenamiento == 'Burbuja'):
                metodos.metodoBurbuja(listaNueva)
            elif(metodoOrdenamiento == 'Seleccion'):
                metodos.metodoSeleccion(listaNueva)
            elif(metodoOrdenamiento == 'Insercion'):
                metodos.metodoInsercion(listaNueva)
            elif(metodoOrdenamiento == 'QuickSort'):
                if(mayorQuick > 0 and menorQuick > 0):
                    metodos.metodoQuickSortTres(listaNueva, menorQuick, mayorQuick)
                else:
                    metodos.metodoQuickSortTres(listaNueva, 0, len(listaNueva) - 1)
            else:
                print('Error de metodo de ordenamiento, los unicos aceptados son:\nBurbuja\nSeleccion\nInsercion\nQuickSort')
            transcurrido = time() - inicioTiempo
            archivo.write(str(x) + "," + format(transcurrido, ".7f") + "\n")
            x = x + salto
        archivo.close()
    else:
        print('Revise su entrada de datos.')