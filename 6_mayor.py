def mayor(x):
    lst=[]
    for i in range (x):
        numeros = int(input("Ingrese el numero: "))
        lst.append(numeros)
    print("El numero mayor en la lista es: ", max(lst))

x = int(input('Cuantos numeros tiene su lista?: '))
y = mayor(x)
