def isPrime(num):
    cont = 0
    for div in range(1, num + 1):
        if num % div == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False

        
def n_primos(n):
    c = 0
    while n >= 2:
        if isPrime(n):
            c += 1
        n -= 1
    return c
    
    
