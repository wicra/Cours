package student_management.src.fr.univ_amu.l2info;

public class Student {
    private final int id;          // Immutable et privé
    private final String firstName; // Immutable et privé
    private final String lastName;  // Immutable et privé

    // Constructeur de la classe Student
    public Student(int id, String firstName, String lastName) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // Méthode toString
    @Override
    public String toString() {
        return firstName + " " + lastName + " id: " + id;
    }
}
