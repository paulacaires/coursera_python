class Triangulo():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, triangulo):
        tri1 = sorted([self.a, self.b, self.c])
        tri2 = sorted([triangulo.a, triangulo.b, triangulo.c])

        cont = 0 #Contador de lados semelhantes.
        
        for lado1, lado2 in zip(tri1, tri2):
           
            if lado1 % lado2 == 0 or lado2 % lado1 == 0:
                cont += 1

        if cont == 3:
            return True
        else:
            return False
