class Habitacion:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano
    
    def mostrar_info(self):
        print(f"{self.nombre}: {self.tamano}m²")


class Casa: 
    def __init__(self, direccion):
        self.direccion = direccion
        self.habitaciones = []
    
    def agregar_habitacion(self, nombre, tamano):
        self.habitaciones.append(Habitacion(nombre, tamano))
    
    def mostrar_info(self):
        print(f"\nCasa en {self.direccion}:")
        [h.mostrar_info() for h in self.habitaciones]
        print(f"Total: {len(self.habitaciones)} habitaciones, {sum(h.tamano for h in self.habitaciones)}m²")


casa = Casa("Calle Principal 123")
casa.agregar_habitacion("Dormitorio", 15)
casa.agregar_habitacion("Cocina", 10)
casa.agregar_habitacion("Baño", 5)

casa.mostrar_info()