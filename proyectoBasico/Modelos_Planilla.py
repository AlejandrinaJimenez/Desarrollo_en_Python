
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



#####################################################################
##Crear los objetos: 8 trabajadores

dev1 = DEV("1","Maria", "Microsoft vsxode","6")
print (dev1.get_datos())
print (dev1.get_bonos())
a = (dev1.get_salario_total())
print("El salario total del empleado es: " + str(a) ) 
print (dev1.get_proyecto())
print ("##" * 40)

dev2 = DEV("2","Alfonso", "MarlinFirmware","17")
print (dev2.get_datos())
print (dev2.get_bonos())
b = (dev2.get_salario_total())
print("El salario total del empleado es: " + str(b) ) 
print (dev2.get_proyecto())
print ("##" * 40)

qa1= QA("3","Lucia", "MarlinFirmware","4")
print (qa1.get_datos())
print (qa1.get_bonos())
c = (qa1.get_salario_total())
print("El salario total del empleado es: " + str(c)) 
print (qa1.get_proyecto())
print ("##" * 40)

dba1 =DBA("4","Margarita","Google Dopamine","3")
print (dba1.get_datos())
print (dba1.get_bonos())
d = (dba1.get_salario_total())
print("El salario total del empleado es: " + str(d)) 
print (dba1.get_proyecto())
print ("##" * 40)

qa2=QA("5","Pedro", "Conda","1")
print (qa2.get_datos())
print (qa2.get_bonos())
e = (qa2.get_salario_total())
print("El salario total del empleado es: " + str(e)) 
print (qa2.get_proyecto())
print ("##" * 40)

qa3=QA("6","Rene", "MarlinFirmware","8")
print (qa3.get_datos())
print (qa3.get_bonos())
f = (qa3.get_salario_total())
print("El salario total del empleado es: " + str(f) ) 
print (qa3.get_proyecto())
print ("##" * 40)

dba2 = DBA("7","Jose", "Finances ER", "9")
print (dba2.get_datos())
print (dba2.get_bonos())
g = (dba2.get_salario_total())
print("El salario total del empleado es: " + str(g)) 
print (dba2.get_proyecto())
print ("##" * 40)

qa4=QA("8","Heriberto", "Google Dopamine","1")
print (qa4.get_datos())
print (qa4.get_bonos())
h = (qa4.get_salario_total())
print("El salario total del empleado es: " + str(h) ) 
print (qa4.get_proyecto())
print ("**" * 40)

#######################################################################
## Promedio de salario de los cargos DEV
promedio_dev = (int(dev1.get_salario_total())+int(dev2.get_salario_total()))/2
print("Promedio de salario de todos los trabajadores con el cargo DEV: " + str(promedio_dev))
print ("**" * 40)

##########################################################################
#obtener el trabajador mas antiguo
import operator
lista_antiguedad = {dev1.get_names(): dev1.get_years(),
                    dev2.get_names(): dev2.get_years(),
                    qa1.get_names(): dev2.get_years(),
                    qa2.get_names(): dev2.get_years(),
                    qa3.get_names(): dev2.get_years(),
                    qa4.get_names(): dev2.get_years(),
                    dba1.get_names(): dev2.get_years(),
                    dba2.get_names(): dev2.get_years()
                    
                    }

mas_antiguo = max(lista_antiguedad.items(), key=operator.itemgetter(1))[0]
print ("El trabajador con mayor años de servicio es: "+ mas_antiguo)
print ("$$" * 40)
#############################################################################
#Monto total que se paga a los trabajadores

monto_total = a + b + c + d + e + f + g + h
print("El monto total que se paga a los empleados es: "+ str(monto_total))
