def maiusculas(frase):
    '''Dado uma frase, retorna string com letras maísculas.'''
    letrasMai = ''
    for palavra in frase:
        for letra in palavra:
            if ord(letra) >= 65 and ord(letra) <= 90:
                letrasMai += letra

    return letrasMai
                    
