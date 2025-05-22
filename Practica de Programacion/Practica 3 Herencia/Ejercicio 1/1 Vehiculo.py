class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
    
    def mostrar_info(self):
        return f"{self.marca} {self.modelo} ({self.año}) - ${self.precio}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, precio, puertas, combustible):
        super().__init__(marca, modelo, año, precio)
        self.puertas = puertas
        self.combustible = combustible
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}, {self.puertas} puertas, {self.combustible}"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, precio, cilindrada, motor):
        super().__init__(marca, modelo, año, precio)
        self.cilindrada = cilindrada
        self.motor = motor
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}, {self.cilindrada}cc, {self.motor}"

vehiculos = [
    Coche("Toyota", "Corolla", 2020, 25000, 4, "Gasolina"),
    Coche("Ford", "Mustang", 2023, 45000, 2, "Gasolina"),
    Coche("Volkswagen", "Golf", 2022, 28000, 5, "Diésel"),
    Moto("Honda", "CBR600RR", 2021, 12000, 599, "4T"),
    Moto("Yamaha", "MT-07", 2023, 8500, 689, "2Cil")
]

print("Todos los vehículos:")
for v in vehiculos:
    print(v.mostrar_info())

print("\nCoches con +4 puertas:")
print(*[v.mostrar_info() for v in vehiculos if isinstance(v, Coche) and v.puertas > 4], sep="\n")

print("\nVehículos 2025:")
print(*[v.mostrar_info() for v in vehiculos if v.año == 2025] or ["No hay"], sep="\n")