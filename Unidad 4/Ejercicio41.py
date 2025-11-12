# -- coding: utf-8 --

class Alumno:
    #Agregar
    def _init_(self, nombre: str, numero_control: str, carrera=None):
        self.nombre = nombre                  # str: Nombre completo del alumno.
        self.numero_control = numero_control  # str: Identificador único del alumno (matrícula).
        self.carrera = carrera                # Objeto Carrera: La carrera a la que está inscrito.
        self.calificaciones = {}              # dict: Un diccionario para almacenar las calificaciones por materia. Ej: {"Cálculo I": 8.5}

    def asignar_carrera(self, carrera):
        self.carrera = carrera

    def consulta_calificacion(self, nombre_materia: str):
        if nombre_materia in self.calificaciones:
            return self.calificaciones[nombre_materia]
        else:
            return f'No hay calificación registrada para "{nombre_materia}".'

    def _repr_(self):
        return f'Alumno("{self.nombre}", "{self.numero_control}")'


class Universidad:
    def _init_(self, nombre: str):
        self.nombre = nombre      # str: El nombre de la institución universitaria.
        self.carreras = []        # list: Una lista para almacenar los objetos Carrera que ofrece la universidad.
        self.alumnos = []         # list: Una lista para almacenar todos los objetos Alumno inscritos.
        self.profesores = []      # list: Una lista para almacenar los objetos Profesor que trabajan en la universidad.

    # ------------------- Gestión de carreras -------------------
    def agregar_carrera(self, carrera):
        self.carreras.append(carrera)

    def obtener_carrera(self, nombre_carrera: str):
        for c in self.carreras:
            if c.nombre == nombre_carrera:
                return c
        return None

    # ------------------- Otros registros -------------------
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)


class Carrera:
    def _init_(self, nombre: str):
        self.nombre = nombre    # str: El nombre oficial de la carrera (ej. "Ingeniería").
        self.materias = []    # list: Una lista para almacenar los objetos Materia que componen esta carrera.

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def obtener_materia(self, nombre_materia: str):
        for m in self.materias:
            if m.nombre == nombre_materia:
                return m
        return None

    def _repr_(self):
        return f'Carrera("{self.nombre}")'


class Materia:
    def _init_(self, nombre: str, carrera: Carrera, calificacion_final: float = None):
        self.nombre = nombre                # str: El nombre de la asignatura (ej. "Cálculo I").
        self.carrera = carrera              # Objeto Carrera: La carrera a la que pertenece esta materia.
        self.calificacion_final = calificacion_final  # float: (Opcional) Podría usarse para una calificación general, aunque en tu lógica se guarda en Alumno.

    def _repr_(self):
        return f'Materia("{self.nombre}", carrera="{self.carrera.nombre}")'


class Profesor:
    def _init_(self, nombre: str, materia: Materia):
        self.nombre = nombre    # str: El nombre del profesor.
        self.materia = materia  # Objeto Materia: La materia específica que este profesor imparte.

    def registra_calificacion(self, alumno: Alumno, calificacion: float):
        # Este método usa el atributo 'materia' del profesor para saber qué materia está calificando
        # y actualiza el atributo 'calificaciones' del alumno.
        alumno.calificaciones[self.materia.nombre] = calificacion
        print(f'Calificación registrada: {alumno.nombre} -> '
              f'{self.materia.nombre}: {calificacion}')

    def _repr_(self):
        return f'Profesor("{self.nombre}", {self.materia})'

if _name_ == "_main_":

    uni = Universidad("Instituto")

    ing = Carrera("Ingeniería")
    lic = Carrera("Licenciatura en Ciencias Sociales")

    uni.agregar_carrera(ing)
    uni.agregar_carrera(lic)

    calc = Materia("Cálculo I", ing)
    fis = Materia("Física I", ing)
    sociologia = Materia("Introducción a la Sociología", lic)

    ing.agregar_materia(calc)
    ing.agregar_materia(fis)
    lic.agregar_materia(sociologia)

    juan = Alumno("Juan Pérez", "2023001")
    luisa = Alumno("Luisa Gómez", "2023002")

    juan.asignar_carrera(ing)
    luisa.asignar_carrera(ing)

    uni.agregar_alumno(juan)
    uni.agregar_alumno(luisa)

    prof_garcia = Profesor("Dr. García", calc)
    prof_rodriguez = Profesor("Mtra. Rodríguez", fis)

    uni.agregar_profesor(prof_garcia)
    uni.agregar_profesor(prof_rodriguez)

    prof_garcia.registra_calificacion(juan, 8.5)
    prof_garcia.registra_calificacion(luisa, 9.0)
    prof_rodriguez.registra_calificacion(juan, 7.5)

    print(juan.consulta_calificacion("Cálculo I"))   
    print(juan.consulta_calificacion("Física I"))   
    print(luisa.consulta_calificacion("Cálculo I")) 
    print(luisa.consulta_calificacion("Física I"))  

    print("Materias de Ingeniería:", [m.nombre for m in ing.materias])