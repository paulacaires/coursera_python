def bubble_sort(lista):
    houveTroca = True
    while houveTroca:
        houveTroca = False
        for pos in range(1, len(lista)):
            if lista[pos] < lista[pos - 1]:
                lista[pos], lista[pos - 1] = lista[pos - 1], lista[pos]
                print(lista)
                houveTroca = True
    return lista
