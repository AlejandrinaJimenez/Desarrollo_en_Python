def filtro(x):
    lst=[]
    for i in range (x):
        palabras = str(input("Ingrese la palabra: "))
        lst.append(palabras)
    y = str(input("Que palabra desea buscar: "))
    filtrado = [k for k in lst if y in k] 
    print (filtrado)   


x = int(input('Cuantas palabras hay en su lista?: '))
y = filtro(x)
