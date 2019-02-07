class X:
    pass
class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h =h
        self.m=m
        self.s=s
    def imprimirHora(hora):
        print(hora.h)
        print(hora.m)
        print(hora.s)

clock = Time ()
clock.imprimirHora()

x=X()
clock.imprimirHora(x)
