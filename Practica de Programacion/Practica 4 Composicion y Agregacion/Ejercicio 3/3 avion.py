class Parte:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
        
    def mostrar_info(self):
        print(f"{self.nombre}: {self.peso}kg")
        
        
class Avion:
    def __init__(self, modelo, fabricante):
        self.modelo = modelo 
        self.fabricante = fabricante
        self.partes = [  
            Parte("Alas", 2), 
            Parte("Motores", 5), 
            Parte("Tren de aterrizaje", 3)  
        ]
        
    def agregar_parte(self, nombre, peso):  
        nueva_parte = Parte(nombre, peso)
        self.partes.append(nueva_parte)
        
    def mostrar_avion(self):
        print(f"\nAvión {self.modelo} de {self.fabricante}:")  
        for parte in self.partes: 
            parte.mostrar_info()
        total_peso = sum(p.peso for p in self.partes)
        print(f"Total: {len(self.partes)} partes, {total_peso}kg")

avion = Avion("Boeing 747", "Boeing")
avion.agregar_parte("Puerta", 10)  
avion.mostrar_avion()