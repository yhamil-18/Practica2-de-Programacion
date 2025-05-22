class Estudiante:
    def __init__(self, nombre, carrera, semestre):
        self.nombre = nombre
        self.carrera = carrera
        self.semestre = semestre
    
    def mostrar_info(self):
        print(f"{self.nombre} | {self.carrera} | Semestre {self.semestre}")

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def mostrar_universidad(self):
        print(f"\nUniversidad: {self.nombre}")
        for estudiante in self.estudiantes:
            estudiante.mostrar_info()

est1 = Estudiante("Ana", "Ingeniería", 3)
est2 = Estudiante("Luis", "Medicina", 5)

uni = Universidad("UNAL")
uni.agregar_estudiante(est1)
uni.agregar_estudiante(est2)

uni.mostrar_universidad()