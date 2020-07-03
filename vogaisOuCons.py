def conta_letras(frase, contar="vogais"):
    '''Dado uma string, retorna o número de vogais ou consoantes.'''
    contVogais = 0
    contCons = 0

    for letra in frase:
        if letra in 'aeiou':
            contVogais += 1
        else:
            if letra != ' ':
                contCons += 1

    if contar == 'vogais':
        return contVogais
    elif contar == 'consoantes':
        return contCons
