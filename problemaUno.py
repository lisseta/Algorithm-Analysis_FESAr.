# Solución para el problema N° 1 de Diseño y Análisis de Algoritmos
# Autor: SouYui

# ! Requiere una lista de elementos tipo str
# R Devuelve el indice del primer elemento que su predecesor es menor a él
def primerElementoMenor(lista):
    if(type(lista) == list and len(lista) > 1):
        for i in range(1, len(lista)):
            if(len(lista[i]) > len(lista[i - 1])):
                return [i]
    else:
        print("No es una lista, verifique su entrada.")


listaPrueba = ["Samuel", "Emilia", "Erick","Samuel", "Emmanuel"]
result = primerElementoMenor(listaPrueba)
print(f"El índice de la lista donde se encuentra el elemento es: {result}")
