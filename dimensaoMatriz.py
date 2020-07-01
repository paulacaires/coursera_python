def dimensoes(matriz):
    '''Dado uma matriz, imprime a dimensão dela.'''
    for i in matriz:
        nCol = len(i)

    print('{}X{}'.format(len(matriz), nCol))
