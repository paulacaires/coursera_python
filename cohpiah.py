import re

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def palavras(texto):
    '''Coloca todas as palavras em uma lista.'''
    listaFrases = list()
    listaPalavras = list()
    listaFinal = list()
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        listaFrases.append(frases)
    for frase in listaFrases:
        for elem in frase:
            palavra = separa_palavras(elem)
            listaPalavras.append(palavra)
    for lista in listaPalavras:
        for elem in lista:
            listaFinal.append((elem))
    return listaFinal


def tamMedioPalavra(texto):
    '''Calcula tamanho médio das palavras.'''
    soma = 0
    for palavra in palavras(texto):
        soma += len(palavra)
    tamPalavra = soma / (len(palavras(texto)))
    return tamPalavra


def typeToken(texto):
    '''Calcula Relação TypeToken.'''
    palDif =  n_palavras_diferentes(palavras(texto))
    typeToken = palDif / (len(palavras(texto)))
    return typeToken


def hapaxLegomana(texto):
    '''Calcula Razão Hapax Legomana.'''
    palUnicas = n_palavras_unicas(palavras(texto))
    hapaxLegomana = palUnicas / (len(palavras(texto)))
    return hapaxLegomana


def tamMedioSentenca(texto):
    '''Calcula o tamanho médio da sentença.'''
    soma = 0 #Soma dos números de caracteres em todas as sentenças. 
    qtdSentencas = 0 #Quantidade de sentenças.
    for sentenca in separa_sentencas(texto):
        soma += len(sentenca)
        qtdSentencas += 1
        
    tamSentenca = soma / qtdSentencas
    return tamSentenca       


def complexidade(texto):
    '''Total de frases dividido pelo número de sentenças.'''
    #Numero total de frases no texto.
    soma = 0
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            soma += 1

    complexidade = soma / len(separa_sentencas(texto))
    return complexidade


def tamMedioFrase(texto):
    '''Calcula o tamanho médio da frase.'''
    soma = 0 #Soma dos números de caracteres em todas as frases.
    qtdFrases = 0 #Quantidade de frases.
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            soma += len(frase)
            qtdFrases += 1

    tamFrase = soma / qtdFrases
    return tamFrase
  

def calcula_assinatura(texto):
    '''Dado um texto, calcula sua assinatura.'''
    assinatura = [tamMedioPalavra(texto), typeToken(texto), hapaxLegomana(texto), tamMedioSentenca(texto), complexidade(texto), tamMedioFrase(texto)]
    return assinatura


def compara_assinatura(as_a, as_b):
    grauSim = 0
    for traco in range(6): #Para cada traço na assinatura A.
        grauSim += abs(as_a[traco] - as_b[traco])

    return (grauSim / 6)
     

def avalia_textos(textos, ass_cp):
    grauSim = list() #Lista com todos os graus de similaridade.
    for texto in textos:
        as_a = calcula_assinatura(texto)
        grauSim.append(compara_assinatura(as_a, ass_cp))

    return (grauSim.index(min(grauSim)) + 1)
    

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")


print('Bem-vindo ao detector automático de COH-PIAH.')
print('Informe a assinatura típica de um aluno infectado:')
print()
tamPalavra = float(input('Entre o tamanho médio de palavra: '))
typeToken = float(input('Entre a relação Type-Token: '))
hapaxLegomana = float(input('Entre a Razão Hapax Legomana: '))
tamSentenca = float(input('Entre o tamanho médio de sentença: '))
complexidade = float(input('Entre a complexidade média da sentença: '))
tamFrase = float(input('Entre o tamanho médio de frase: '))
ass_cp = [tamPalavra, typeToken, hapaxLegomana, tamSentenca, complexidade, tamFrase]
print()

textos = list()
textos.append(le_textos())
textoCont = avalia_textos(textos, ass_cp)

print('O autor do texto', textoCont, 'está infectado com COH-PIAH')
