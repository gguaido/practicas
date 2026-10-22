#Variables a utilizar
Dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
Tareas = ['Barrer', 'Cocinar', 'Lavar', 'Plancar']
Nombre = input('¿Cuál es tu nombre?') #Permitir que la persona añada su nombre y luego sea almacenado en la variable
#Mensaje que tiene que reflejar la consola
print(f'{Nombre.strip().lower()}, tienes pendiente por realizar las siguientes tareas: {Tareas} en los siguientes días: {Dias}') 
#En el fragmento anterior se estandariza el nombre tanto por posibles espacios como irregularidades en las mayúsuculas o minúsculas que tenga, además de mostrar las tareas pendientes en el resto de los días