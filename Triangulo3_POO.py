class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c    
            
    def retangulo(self):
        lados = sorted([self.a, self.b, self.c])

        if (lados[0] ** 2 + lados[1] ** 2 == lados[2] ** 2):
            return True
        else:
            return False     
        
        


