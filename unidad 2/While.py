#Esta funcion muestra el menu
def Mostrar_Menu() -> None:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1) Saludar")
    print("2) Calcular la suma de dos números")
    print("3) Mostrar la tabla de multiplicar del 5")
    print("0) Salir")
    
#Esta Funcion ejecuta la opcion 1 introduces tu nombre y te saluda
def Opcion_Saludar() -> None:
    Nombre = input("¿Cómo te llamas? ").strip()
    print(f"¡Hola, {Nombre}! Bienvenido/a.")

#Esta Funcion ejecuta la opcion 2 introduces dos numeros y los suma
def Opcion_Suma() -> None:
    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print(f"La suma es: {a + b}")
    except ValueError:
        print(" Debes introducir valores numéricos.")

#Esta funcion ejecuta la opcion 3 te muestra la tabla del 5
def Opcion_Tabla() -> None:
    numero = 5
    print(f"\nTabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} × {i} = {numero * i}")


# ---------- Bucle principal ----------
#La variable continuar funciona con while,
#hace que se este repitiendo el menu mientras se introdusca la opcion 1,2,3 si es la opcion 0 continuar se convierte en una variable falsa y el ciclo termina
continuar = True              
while continuar:
    Mostrar_Menu()             
    eleccion = input("Elige una opción: ").strip()

    if eleccion == "1":
        Opcion_Saludar()
    elif eleccion == "2":
        Opcion_Suma()
    elif eleccion == "3":
        Opcion_Tabla()
    elif eleccion == "0":
        print("\n ¡Hasta luego!")
        continuar = False
    else:
        print(" Opción no válida, intenta de nuevo.")

print("Programa terminado.")