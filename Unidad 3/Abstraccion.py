from abc import ABC, abstractmethod

# Clase abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Vehículo genérico: {self.marca} {self.modelo} ({self.año}) - Color: {self.color}"


# Subclases que heredan solo los atributos
class Auto(Vehiculo):
    pass


class Moto(Vehiculo):
    pass


class Camion(Vehiculo):
    pass

class Fabrica_automata_andante(Vehiculo):
    pass


# Crear objetos de las clases hijas
auto1 = Auto("Toyota", "Corolla", 2022, "Rojo")
moto1 = Moto("Yamaha", "FZ", 2021, "Negra")
camion1 = Camion("Volvo", "FH", 2020, "Blanco")
fabrica_automata_andante1 = Fabrica_automata_andante("PlayStation","PS5", 2024, "Gris")
auto2 = Auto("Chevrolet", "POP", "2a.c.", "Verde Descarapelado")
moto2 = Moto("Harley", "1", 2020, "Negro")
camion2 = Camion("Mercedes", "CAT", 2023 ,"Gris")

# Visualización
print(auto1)
print(moto1)
print(camion1)
print(fabrica_automata_andante1)
print(auto2)
print(moto2)
print(camion2)