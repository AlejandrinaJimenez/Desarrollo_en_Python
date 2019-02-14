import operator
def ordenar(d):
    ascendente = str(input("Ascendente (True/False):"))
    t = ascendente.startswith('T')
    if t == True:
        sorted_d = sorted(d.items(), key=lambda x: x[1])
        print(sorted_d)
    else:
        sorted_d = sorted(d.items(), key=lambda x: x[1])
        sorted_d.reverse()
        print(sorted_d)


d = {}
a = {str(input("Ingrese el nombre:")):int(input("Ingrese la edad:"))}
d.update(a)
b = {str(input("Ingrese el nombre:")):int(input("Ingrese la edad:"))}
d.update(b)
c = {str(input("Ingrese el nombre:")):int(input("Ingrese la edad:"))}
d.update(c)

print(d)
ordernado = ordenar(d)

