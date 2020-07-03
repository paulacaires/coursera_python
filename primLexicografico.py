def primeiro_lex(lista):
    '''Dado uma lista de strings, devolve primeiro na ordem lexicográfica.'''
    cont = 0
    for elem in lista:
        if cont == 0 or elem < menorOrd:
            menorOrd = elem
            menor = elem
                  
        cont += 1

    return menor
        
