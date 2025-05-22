class Habitacion {
    String nombre;
    double tamano;
    
    public Habitacion(String nombre, double tamano) {
        this.nombre = nombre;
        this.tamano = tamano;
    }
    
    void mostrarInfo() {
        System.out.println(nombre + ": " + tamano + "m²");
    }
}

class Casa {
    String direccion;
    java.util.ArrayList<Habitacion> habitaciones;
    
    public Casa(String direccion) {
        this.direccion = direccion;
        this.habitaciones = new java.util.ArrayList<>();
    }
    
    void agregarHabitacion(String nombre, double tamano) {
        habitaciones.add(new Habitacion(nombre, tamano));
    }
    
    void mostrarInfo() {
        System.out.println("\nCasa en " + direccion + ":");
        for (Habitacion h : habitaciones) {
            h.mostrarInfo();
        }
        
        double totalM2 = 0;
        for (Habitacion h : habitaciones) {
            totalM2 += h.tamano;
        }
        
        System.out.println("Total: " + habitaciones.size() + " habitaciones, " + totalM2 + "m²");
    }
}

public class Main {
    public static void main(String[] args) {
        Casa casa = new Casa("Calle Principal 123");
        casa.agregarHabitacion("Dormitorio", 15);
        casa.agregarHabitacion("Cocina", 10);
        casa.agregarHabitacion("Baño", 5);
        
        casa.mostrarInfo();
    }
}