def soma_matrizes(m1, m2):
    '''Soma de duas matrizes.'''
    if dimensao(m1) == dimensao(m2):
        matrizSoma = list()
        for i in range(dimensao(m1)[0]): #dimensao(m1)[0] = Nº de Linhas;
            linha = list()
            for j in range(dimensao(m1)[1]): #dimensao(m1)[1] = Nº de Colunas;
                linha.append(m1[i][j] + m2[i][j])
            matrizSoma.append(linha)            
                
        return matrizSoma
    else:
        return False



def dimensao(matriz):
    '''Retorna dimensão de uma matriz.'''
    nLinha = 0
    for linha in matriz:
        nLinha += 1

        nColuna = 0
        for elem in linha:
            nColuna += 1
    return nLinha, nColuna
