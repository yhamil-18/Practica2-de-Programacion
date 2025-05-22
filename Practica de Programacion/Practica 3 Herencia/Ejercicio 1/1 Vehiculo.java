public class Vehiculo {
    protected String marca;
    protected String modelo;
    protected int año;
    protected double precio;

    public Vehiculo(String marca, String modelo, int año, double precio) {
        this.marca = marca;
        this.modelo = modelo;
        this.año = año;
        this.precio = precio;
    }

    public String mostrarInfo() {
        return String.format("%s %s (%d) - $%.2f", marca, modelo, año, precio);
    }
}

public class Coche extends Vehiculo {
    private int puertas;
    private String combustible;

    public Coche(String marca, String modelo, int año, double precio, 
                int puertas, String combustible) {
        super(marca, modelo, año, precio);
        this.puertas = puertas;
        this.combustible = combustible;
    }

    @Override
    public String mostrarInfo() {
        return super.mostrarInfo() + ", " + puertas + " puertas, " + combustible;
    }
}


public class Moto extends Vehiculo {
    private int cilindrada;
    private String tipoMotor;

    public Moto(String marca, String modelo, int año, double precio,
            int cilindrada, String tipoMotor) {
        super(marca, modelo, año, precio);
        this.cilindrada = cilindrada;
        this.tipoMotor = tipoMotor;
    }

    @Override
    public String mostrarInfo() {
        return super.mostrarInfo() + ", " + cilindrada + "cc, " + tipoMotor;
    }
}


public class Main {
    public static void main(String[] args) {

        Vehiculo[] vehiculos = {
            new Coche("Toyota", "Corolla", 2020, 25000, 4, "Gasolina"),
            new Coche("Ford", "Mustang", 2023, 45000, 2, "Gasolina"),
            new Coche("Volkswagen", "Golf", 2022, 28000, 5, "Diésel"),
            new Moto("Honda", "CBR600RR", 2021, 12000, 599, "4 tiempos"),
            new Moto("Yamaha", "MT-07", 2023, 8500, 689, "2 cilindros")
        };

        System.out.println("=== Todos los vehículos ===");
        for (Vehiculo v : vehiculos) {
            System.out.println(v.mostrarInfo());
        }


        System.out.println("\n=== Coches con más de 4 puertas ===");
        for (Vehiculo v : vehiculos) {
            if (v instanceof Coche && ((Coche)v).puertas > 4) {
                System.out.println(v.mostrarInfo());
            }
        }


        System.out.println("\n=== Vehículos del 2025 ===");
        boolean hay2025 = false;
        for (Vehiculo v : vehiculos) {
            if (v.año == 2025) {
                System.out.println(v.mostrarInfo());
                hay2025 = true;
            }
        }
        if (!hay2025) {
            System.out.println("No hay vehículos del 2025");
        }
    }
}