def imprime_matriz(matriz):
    '''Imprime uma matriz.'''
    for i in matriz:
        cont = 1
        for j in i:
            if cont == nColunas(matriz):
                print(j, end='')
            else:
                print(j, end=' ')

            cont += 1
        print()


def nColunas(matriz):
    '''Dado uma matriz, retorna número de colunas.'''
    for i in matriz:
        nCol = 0
        for j in i:
            nCol += 1

    return nCol
