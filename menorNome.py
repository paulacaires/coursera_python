def menor_nome(nomes):
    '''Dado uma lista de strings, retorna o nome mais curto.'''
    cont = 1
    for nome in nomes:
        
        if cont == 1 or (len(nome.strip()) < menorLen): #Se for o primeiro nome.
            menorLen = len(nome.strip())
            menorNome = nome.strip()

        cont += 1
    return menorNome.capitalize()
