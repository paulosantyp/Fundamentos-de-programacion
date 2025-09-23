#van a crear una lista vacia con su nombre y van a agregar 5 elementos con input:
#(nombre, preparatoria, lugar de recidencia,edad, carrera)
lista_de_datos = []
dato = input("Agrega tu nombre:")
lista_de_datos.append(dato)
dato1 = input("Agrega tu Preparatoria de procedencia:")
lista_de_datos.append(dato1)
dato2 = input("Agrega tu lugar de recidencia:")
lista_de_datos.append(dato2)
dato3 = input("Agrega tu edad:")
lista_de_datos.append(dato3)
dato4 = input("Agrega tu Carrera:")
lista_de_datos.append(dato4)
print("Tu lista es:")
for dato in lista_de_datos:
    print(f"- {dato}")
print("\n✅ ¡Lista creada con éxito!")