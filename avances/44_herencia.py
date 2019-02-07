class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def get_datos(self):
        return self.nombre + "\t" +self.apellido

class Trabajador(Persona):
    def __init__(self, nombre, apellido, cargo):
        Persona.__init__(self, nombre, apellido)
        self.cargo = cargo

    def get_datos(self):
        return Persona.get_datos(self) + "\t" + self.cargo

p = Persona("Marge", "Simpson")
print(p.get_datos())
t = Trabajador("Homero", "Simpson", "frontend Developer")
print(t.get_datos())