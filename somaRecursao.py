def soma_lista(lista):
    '''Soma dos elementos de uma lista com recursão.'''
    for pos in range(len(lista)):
        if pos == len(lista) - 1:
            return lista[pos]
        else:
            return lista[pos] + soma_lista(lista[pos + 1:])    
