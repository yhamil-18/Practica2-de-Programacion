class Empleado:
    def __init__(self, nombre, apellido, salario_base, años):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base = salario_base
        self.años = años
    
    def calcular_salario(self):
        return self.salario_base + (self.salario_base * 0.05 * self.años)


class Gerente(Empleado):
    def __init__(self, nombre, apellido, salario_base, años, departamento, bono):
        super().__init__(nombre, apellido, salario_base, años)
        self.departamento = departamento
        self.bono = bono
    
    def calcular_salario(self):
        return super().calcular_salario() + self.bono


class Desarrollador(Empleado):
    def __init__(self, nombre, apellido, salario_base, años, lenguaje, horas_extras):
        super().__init__(nombre, apellido, salario_base, años)
        self.lenguaje = lenguaje
        self.horas_extras = horas_extras
    
    def calcular_salario(self):
        return super().calcular_salario() + (self.horas_extras * 20)

gerentes = [
    Gerente("Juan", "Pérez", 5000, 5, "TI", 1500),
    Gerente("María", "Gómez", 6000, 8, "Ventas", 800)
]

desarrolladores = [
    Desarrollador("Carlos", "López", 4000, 3, "Python", 15),
    Desarrollador("Ana", "Martínez", 4500, 4, "Java", 8)
]

print("Salarios:")
for g in gerentes:
    print(f"{g.nombre}: ${g.calcular_salario():.2f}")

for d in desarrolladores:
    print(f"{d.nombre}: ${d.calcular_salario():.2f}")

print("\nGerentes con bono > $1000:")
print(*[f"{g.nombre} (${g.bono})" for g in gerentes if g.bono > 1000], sep="\n")

print("\nDesarrolladores con +10 horas extras:")
print(*[f"{d.nombre} ({d.horas_extras} hrs)" for d in desarrolladores if d.horas_extras > 10], sep="\n")