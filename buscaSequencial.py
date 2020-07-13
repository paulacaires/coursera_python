def busca(lista,elemento):
    '''Busca determinado elemento em uma lista, retornando o indice.'''
    indice = 0
    for elem in lista:
        if elem == elemento:
            return indice
        indice += 1
    return False
