from datetime import date

class Persona:
    def __init__(self, ci, nombre, apellido, fecha_nac):
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac
    
    def edad(self):
        hoy = date.today()
        return hoy.year - self.fecha_nac.year - ((hoy.month, hoy.day) < (self.fecha_nac.month, self.fecha_nac.day))
    
    def mostrar(self):
        print(f"{self.nombre} {self.apellido} - CI: {self.ci} - Edad: {self.edad()}")

class Estudiante(Persona):
    def __init__(self, ci, nombre, apellido, fecha_nac, ru, semestre):
        super().__init__(ci, nombre, apellido, fecha_nac)
        self.ru = ru
        self.semestre = semestre
    
    def mostrar(self):
        super().mostrar()
        print(f"RU: {self.ru} - Semestre: {self.semestre}")

class Docente(Persona):
    def __init__(self, ci, nombre, apellido, fecha_nac, nit, profesion, sexo):
        super().__init__(ci, nombre, apellido, fecha_nac)
        self.nit = nit
        self.profesion = profesion
        self.sexo = sexo
    
    def mostrar(self):
        super().mostrar()
        print(f"NIT: {self.nit} - Profesión: {self.profesion} - Sexo: {self.sexo}")

estudiantes = [
    Estudiante("123", "Juan", "Perez", date(1995, 5, 10), "E001", 8),
    Estudiante("456", "Maria", "Gomez", date(2000, 8, 20), "E002", 5),
    
]

docentes = [
    Docente("111", "Pedro", "Perez", date(1980, 7, 15), "N001", "Ingeniero", "M"),
    Docente("222", "Ana", "Gomez", date(1975, 3, 22), "N002", "Licenciada", "F"),
]


print("Estudiantes >25 años:")
for e in estudiantes:
    if e.edad() > 25:
        e.mostrar()

ingenieros = [d for d in docentes if d.profesion == "Ingeniero" and d.sexo == "M"]
if ingenieros:
    mayor = max(ingenieros, key=lambda x: x.edad())
    print("\nDocente Ingeniero masculino más mayor:")
    mayor.mostrar()

print("\nPersonas con mismos apellidos:")
apellidos = set(e.apellido for e in estudiantes) & set(d.apellido for d in docentes)
for a in apellidos:
    print(f"\nApellido: {a}")
    print("Estudiantes:")
    for e in [x for x in estudiantes if x.apellido == a]:
        e.mostrar()
    print("Docentes:")
    for d in [x for x in docentes if x.apellido == a]:
        d.mostrar()