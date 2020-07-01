def sao_multiplicaveis(m1, m2):
    if dimensao(m1)[1] == dimensao(m2)[0]:
        return True
    else:
        return False


def dimensao(matriz):
    '''Dada uma matriz, calcula sua dimensão.'''
    nLinha = 0
    for i in matriz:
        nLinha += 1

        nCol = 0
        for j in i:
            nCol += 1

    return nLinha, nCol 
