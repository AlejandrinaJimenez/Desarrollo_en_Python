
def hexagono(n):
    for i in range(n):
        print (' '*(n-i-1)+'*' *(i+n))
    for j in range(n-1,0,-1):
        print(' '*(n-j)+'*' *(j+n-1))

x = int(input("Ingrese la longitud del lado del hexagono:"))
y = hexagono(x)