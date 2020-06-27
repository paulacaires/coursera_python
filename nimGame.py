def computador_escolhe_jogada(n, m):
    pecasTiradas = 0
    while n % (m + 1) != 0:
        pecasTiradas += 1
        n -= 1

    if pecasTiradas == 0 or pecasTiradas > m:
        pecasTiradas = m
        
    return pecasTiradas

    
def usuario_escolhe_jogada(n, m):
    valido = False
    while True:
        pecasTiradas = int(input('Quantas peças você vai tirar? '))
        if (pecasTiradas <= 0) or (pecasTiradas > m):
            print('Oops! Jogada inválida! Tente de novo.')
        else:
            break
            
    return pecasTiradas


def partida():
    compJoga = False
    
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    if n % (m + 1) == 0:
        print('Você começa!')
        compJoga = False
    else:
        print('Computador começa!')
        compJoga = True

    while not (n == 0):
        if not compJoga:
            pecasRem = usuario_escolhe_jogada(n, m)
            n -= pecasRem
            print('Você tirou', pecasRem, 'pecas.')
            print('Agora restam', n, 'peças no tabuleiro.')
            compJoga = True
        else:
            pecasRem = computador_escolhe_jogada(n, m)
            n -= pecasRem
            print('O computador tirou', pecasRem, 'pecas.')
            print('Agora restam', n, 'peças no tabuleiro.')
            compJoga = False

    print('Fim do jogo! O computador ganhou!')


def campeonato():
    for cont in range(1, 4):
        print('**** Rodada {} ****'.format(cont))
        partida()
        
    print('**** Final do campeonato! ****')
    print('Placar: Você 0 X 3 Computador')


escolha = int(input('''Bem-vindo ao jogo do NIM! Escolha:

1 - para jogar uma partida isolada
2 - para jogar um campeonato '''))

if escolha == 1:
    partida()
else:
    campeonato()
