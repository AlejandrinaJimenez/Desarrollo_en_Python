class Perro:

    def __init__(self, nombre):
        self.nombre = nombre
        self.trucos = []

    def agregar_Truco(self, truco):
        self.trucos.append(truco)

f = Perro("FIDO")
f.agregar_Truco('Darse la vuelta')

n = Perro("Negro")
n.agregar_Truco('Hacerse al muerto')


m = Perro("N")
m.agregar_Truco("Mover la cola")
print(f.trucos)