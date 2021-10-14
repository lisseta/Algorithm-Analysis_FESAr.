import random as rn
import copy
from time import time
import metodosOrdenamiento as metodos

# ! Requiere un dato de tipo int 
# R Devuelve una lista con la cantidad n de elementos aleatorios de tipo int
def crearLista(longitud):
    lista = []
    for i in range(0, longitud):
        lista.append(rn.randint(0, 200))
    return lista

# ! Requiere 5 elementos para su funcionamiento o un maximo de 7: 
#   1. Una lista de elementos tipo int desordenados
#   2. La cantidad de elementos que posee la lista
#   3. El número que definirá los saltos para ir evaluando el ordenamiento
#   4. El método de ordenamiento deseado de una lista de 4 {Burbuja, Seleccion, Insercion, QuickSort} : No deben utilizarse acentos ni espacios
#   5. El nombre del archivo .xls en el que se creará el registro del tiempo en ordenar por saltos
#   6. OPCIONAL. El límite menor para tomar en el método de QuickSort (Por defecto es 0)
#   7. OPCIONAL. El límite mayor para tomar en el método de QuickSort (Por defecto es 0 y se ocupa la longitud de la lista insertada - 1)
# R Ordena la lista insertada y crea un archivo .xls con el nombre insertado en el parámetro 5 en la carpeta madre.
def calculoTiempoOrdenamiento(lista, numeroElementos , x, metodoOrdenamiento, nombreArchivo, menorQuick = 0, mayorQuick = 0):
    if(type(lista) == list and type(numeroElementos) == int and type(x) == int and type(metodoOrdenamiento) == str and type(nombreArchivo) == str):
        archivo = open(nombreArchivo+".csv", "w")
        archivo.write("N,Tiempo\n")
        salto = x
        metodoOrdenamiento = metodoOrdenamiento.upper()
        
        for i in range(x, numeroElementos, x):
            listaNueva = copy.deepcopy(lista[:x])
            inicioTiempo = time()
            if(metodoOrdenamiento == 'BURBUJA'):
                metodos.metodoBurbuja(listaNueva)
            elif(metodoOrdenamiento == 'SELECCION'):
                metodos.metodoSeleccion(listaNueva)
            elif(metodoOrdenamiento == 'INSERCION'):
                metodos.metodoInsercion(listaNueva)
            elif(metodoOrdenamiento == 'QUICKSORT'):
                if(mayorQuick > 0 and menorQuick > 0):
                    metodos.metodoQuickSort(listaNueva, menorQuick, mayorQuick)
                else:
                    metodos.metodoQuickSort(listaNueva, 0, len(listaNueva) - 1)
            else:
                print('Error de metodo de ordenamiento, los unicos aceptados son:\nBurbuja\nSeleccion\nInsercion\nQuickSort')
            transcurrido = time() - inicioTiempo
            archivo.write(str(x) + "," + format(transcurrido, ".7f") + "\n")
            x = x + salto
        archivo.close()
    else:
        print('Revise su entrada de datos.')