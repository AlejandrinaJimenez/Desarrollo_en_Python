from models import DEV
from models import QA
from models import DBA
import operator
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
