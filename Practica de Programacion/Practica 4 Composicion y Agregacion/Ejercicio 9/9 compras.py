class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio
    
    @property
    def nombre(self):
        return self._nombre
        
    def mostrar_info(self):
        print(f"{self._nombre} - ${self._precio}")

class CarritoCompras:
    def __init__(self):
        self._productos = []
    
    def agregar_producto(self, producto):
        if len(self._productos) < 10:
            self._productos.append(producto)
            print(f"Producto '{producto.nombre}' agregado")  
        else:
            print("¡Carrito lleno! (Máximo 10 productos)")
    
    def mostrar_carrito(self):
        print("\nCarrito de compras:")
        for p in self._productos:
            p.mostrar_info()
        print(f"Total: {len(self._productos)} productos")

p1 = Producto("Laptop", 1500)
p2 = Producto("Mouse", 25)
p3 = Producto("Teclado", 50)

carrito = CarritoCompras()

carrito.agregar_producto(p1)
carrito.agregar_producto(p2)
carrito.agregar_producto(p3)

carrito.mostrar_carrito()