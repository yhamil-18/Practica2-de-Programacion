import java.time.LocalDate;
import java.util.*;

class Persona {
    String ci, nombre, apellido;
    LocalDate fechaNac;
    
    Persona(String ci, String n, String a, LocalDate fn) {
        this.ci = ci; nombre = n; apellido = a; fechaNac = fn;
    }
    
    int edad() {
        return LocalDate.now().getYear() - fechaNac.getYear();
    }
}

class Estudiante extends Persona {
    String ru;
    Estudiante(String ci, String n, String a, LocalDate fn, String ru) {
        super(ci, n, a, fn); this.ru = ru;
    }
}

class Docente extends Persona {
    String profesion; char sexo;
    Docente(String ci, String n, String a, LocalDate fn, String p, char s) {
        super(ci, n, a, fn); profesion = p; sexo = s;
    }
}

public class Main {
    public static void main(String[] args) {
        List<Estudiante> ests = Arrays.asList(
            new Estudiante("123", "Juan", "Perez", LocalDate.of(1995,5,10), "E001"),
            new Estudiante("456", "Maria", "Gomez", LocalDate.of(2000,8,20), "E002"),
            new Estudiante("789", "Carlos", "Lopez", LocalDate.of(1998,12,5), "E003")
        );
        
        List<Docente> docs = Arrays.asList(
            new Docente("111", "Pedro", "Perez", LocalDate.of(1980,7,15), "Ingeniero", 'M'),
            new Docente("222", "Ana", "Gomez", LocalDate.of(1975,3,22), "Licenciada", 'F'),
            new Docente("333", "Luis", "Martinez", LocalDate.of(1970,11,30), "Ingeniero", 'M')
        );
        
        System.out.println("Estudiantes >25:");
        ests.stream().filter(e -> e.edad() > 25).forEach(e -> 
            System.out.println(e.nombre + " " + e.apellido));
        
        System.out.println("\nDocente Ingeniero M más viejo:");
        docs.stream()
            .filter(d -> d.profesion.equals("Ingeniero") && d.sexo == 'M')
            .max(Comparator.comparing(Persona::edad))
            .ifPresent(d -> System.out.println(d.nombre + " " + d.apellido));
        
        System.out.println("\nMismos apellidos:");
        Set<String> apeEst = new HashSet<>();
        ests.forEach(e -> apeEst.add(e.apellido));
        docs.stream()
            .filter(d -> apeEst.contains(d.apellido))
            .forEach(d -> System.out.println(d.apellido));
    }
}