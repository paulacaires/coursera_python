from random import randint

def lista_grande(n):
    lista = list()
    for _ in range(n):
        lista.append(randint(0, 100))
    return lista
