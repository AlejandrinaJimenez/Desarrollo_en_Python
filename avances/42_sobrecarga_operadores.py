class Punto:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x) + "," + str(self.y)
    def __add__(self, punto2):
        x = self.x + punto2.x
        y = self.y + punto2.y
        return Punto(x,y)

punto1 = Punto(1,2)
punto2  = Punto(3,4)
res = punto1 + punto2
print(res)