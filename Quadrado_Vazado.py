largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
for a in range(0, altura):
    for l in range(0, largura):
        if a == 0 or a == altura - 1 or l == 0 or l == largura - 1:
            print('#', end='')
        elif l != 0:
            print(' ', end='')
    print('')

