def ordena(lista):
    for indice in range(len(lista)):
        menorIndice = indice
        for j in range(indice + 1, len(lista)):
            if lista[menorIndice] > lista[j]:
                lista[menorIndice], lista[j] = lista[j], lista[menorIndice]

    return lista


def selectionSort(array):
    for index in range(len(array)): #Para cada índice da lista.
        min_index = index #O mínimo índice recebe o índice.

        for right in range(index + 1, len(array)): #Pra cada elemento à direita.
            if array[right] < array[min_index]:
                min_index = right

        array[index], array[min_index] = array[min_index], array[index]
