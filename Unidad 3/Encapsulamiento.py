class Auto:
    def __init__(self, marca, velocidad_maxima):
        self.__marca = marca           # atributo privado
        self.__velocidad_maxima = velocidad_maxima
        self.__velocidad_actual = 0

    # obtiene velocidad
    def get_velocidad_actual(self):
        return self.__velocidad_actual

    # método para acelerar
    # aumenta la velocidad dependiendo el valor actual y el valor introduciodo
    def acelerar(self, aumento):
        if self.__velocidad_actual + aumento > self.__velocidad_maxima:
            self.__velocidad_actual = self.__velocidad_maxima
        else:
            self.__velocidad_actual += aumento

    # método para frenar
     # disminuye la velocidad dependiendo el valor actual y el valor introduciodo
    def frenar(self, reduccion):
        if self.__velocidad_actual - reduccion < 0:
            self.__velocidad_actual = 0
        else:
            self.__velocidad_actual -= reduccion


auto1 = Auto("Toyota", 180)
auto2 = Auto("Fiat", 60)

auto1.acelerar(50)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto1.acelerar(200)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto1.frenar(100)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto2.acelerar(50)
print("Velocidad actual:", auto2.get_velocidad_actual(), "km/h")

auto2.acelerar(200)
print("Velocidad actual:", auto2.get_velocidad_actual(), "km/h")

auto2.frenar(20)
print("Velocidad actual:", auto2.get_velocidad_actual(), "km/h")

#Encapsulamiento

# __marca = variables privadas
# _marca = variables que se pueden mandar a llamar primero a la clase o funcion
# marca = variables publicas