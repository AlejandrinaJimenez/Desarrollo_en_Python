def sumin(x,y):
    sum = 0
    for i in range (x+1,y):
        #x+y
        sum += i
        print(i)
    print(sum)

x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: "))
s = sumin(x,y)