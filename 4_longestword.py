def longest(x, y):
    lx = len(x)
    ly = len(y)
    if lx > ly:
        dif = lx -ly
        print ("La primera palabra es la mas larga por ", str(dif))
    else:
        dif = ly-lx
        print ("La segunda palabra es la mas larga por ", str(dif))

x = str(input("Ingrese la primera palabra: "))
y = str(input("Ingrese la segunda palabra: "))
l = longest(x,y)