class Jugador:
    def __init__(self, nombre, numero, posicion):
        self.nombre = nombre
        self.numero = numero  
        self.posicion = posicion

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Número: {self.numero}, Posición: {self.posicion}")
        
class Habilidad(Jugador):
    def __init__(self, nombre, numero, posicion, habilidad_especial):
        super().__init__(nombre, numero, posicion)
        self.habilidad_especial = habilidad_especial
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Habilidad Especial: {self.habilidad_especial}")
        
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []
        
    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        
    def mostrar_informacion(self):
        print(f"\nEquipo: {self.nombre}")
        for jugador in self.jugadores:
            jugador.mostrar_informacion()


equipo = Equipo("Los Campeones")
jugador1 = Jugador("Juan", 10, "Delantero" )
jugador2 = Habilidad("Pedro", 9, "Defensa", "Saltos altos")
jugador3 = Habilidad("Luis", 8, "Portero", "Velocidad")

equipo.agregar_jugador(jugador1)
equipo.agregar_jugador(jugador2)
equipo.agregar_jugador(jugador3)

equipo.mostrar_informacion()