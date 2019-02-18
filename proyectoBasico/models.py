##models
## Crear una clase llamada Trabajador// Parent class
class Trabajador:
    ## Inizializar los atributos
    def __init__(self, identificador, nombre,years, proyecto):
        self.identificador = identificador
        self.nombre = nombre
        self.years = years
        self.proyecto = proyecto
        self.bono = 0
        self.salario = 0
    def get_datos(self):
        return (("Identificador: "+ self.identificador) + "\t" + ("Nombre: "+ self.nombre) + "\t" + ("Años de Servicio: " + self.years))
    def get_bonos(self):
        self.years = int(self.years)
        SMN = 6180
        if 2<=self.years<=4:
            self.bono = 0.05 * SMN
        elif 5<=self.years<=7:
            self.bono = 0.11 * SMN
        elif 8<=self.years<=10:
            self.bono = 0.18 *SMN
        elif 11<=self.years<=14:
            self.bono = 0.26 *SMN
        elif 15<=self.years <= 19:
            self.bono = 0.34 *SMN
        elif 20<=self.years<=24:
            self.bono = 0.42 * SMN
        elif 25 <= self.years:
            self.bono = 0.5 *SMN
        return ("El bono de antigüedad del empleado es: " + str(self.bono))
    def get_salario_total(self):
        salario_total = self.salario + self.bono
        return salario_total
    def get_proyecto(self):
        return ("El Proyecto en el cual trabaja es: "+ self.proyecto)
    def get_names(self):
        return (self.nombre)
    def get_years(self):
        return (int(self.years))

## Crear clases en funcion al cargo // Child classes 
class DEV(Trabajador):
    def __init__(self, identificador, nombre, proyecto, years):
        Trabajador.__init__(self,identificador, nombre, years, proyecto)
        self.salario = 5600
        self.cargo = "DEV"
    def get_datos(self):
        return Trabajador.get_datos(self)+ "\t" + ("Cargo: " + self.cargo)


class QA(Trabajador):
    def __init__(self, identificador, nombre, proyecto, years):
        Trabajador.__init__(self,identificador, nombre, years, proyecto)
        self.salario = 3800
        self.cargo = "QA"
        
    def get_datos(self):
        return Trabajador.get_datos(self) + "\t" + ("Cargo: " + self.cargo)

class DBA(Trabajador):
    def __init__(self, identificador, nombre, proyecto, years):
        Trabajador.__init__(self,identificador, nombre, years, proyecto)
        self.salario = 6000
        self.cargo = "DBA"
    def get_datos(self):
        return Trabajador.get_datos(self) + "\t" + ("Cargo: " + self.cargo)


