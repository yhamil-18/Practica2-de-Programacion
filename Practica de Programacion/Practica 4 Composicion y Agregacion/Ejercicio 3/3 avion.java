import java.util.ArrayList;

class Parte {
    private String nombre;
    private int peso;
    
    public Parte(String nombre, int peso) {
        this.nombre = nombre;
        this.peso = peso;
    }
    
    public void mostrarInfo() {
        System.out.println(nombre + ": " + peso + "kg");
    }
}

class Avion {
    private String modelo;
    private String fabricante;
    private ArrayList<Parte> partes;
    
    public Avion(String modelo, String fabricante) {
        this.modelo = modelo;
        this.fabricante = fabricante;
        this.partes = new ArrayList<>();
        
        partes.add(new Parte("Alas", 2));
        partes.add(new Parte("Motores", 5));
        partes.add(new Parte("Tren de aterrizaje", 3));
    }
    
    public void agregarParte(String nombre, int peso) {
        partes.add(new Parte(nombre, peso));
    }
    
    public void mostrarAvion() {
        System.out.println("\nAvión " + modelo + " de " + fabricante + ":");
        
        int totalPeso = 0;
        for (Parte parte : partes) {
            parte.mostrarInfo();
            totalPeso += parte.peso;
        }
        
        System.out.println("Total: " + partes.size() + " partes, " + totalPeso + "kg");
    }
}

public class Main {
    public static void main(String[] args) {
        Avion avion = new Avion("Boeing 747", "Boeing");
        avion.agregarParte("Puerta", 10);
        avion.mostrarAvion();
    }
}