package student_management.src.fr.univ_amu.l2info;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final int NB_STUDENTS = 3;
        final String[] firstNames = {"Pierre", "Marie", "Paul"};
        final String[] lastNames = {"Martin", "Dubois", "Calcul"};
        
        for(int index = 0; index < NB_STUDENTS; index++) {
            System.out.println(new Student(index, firstNames[index], lastNames[index]));
        }


        //Pour essayer la classe Scanner, écrivez en Java le programme qui calcule
        // et affiche la somme d’une suite de nombres décimaux strictement positifs,
        // lus au clavier, dont la fin est indiquée par un nombre égal à 0.

        Scanner input = new Scanner(System.in);
        double sum = 0.0;

        System.out.println("Entrez des nombres décimaux strictement positifs (0 pour terminer) :");

        while (true) {
            double number = input.nextDouble();
            if (number == 0) break;
            if (number > 0) {
                sum += number;
            } else {
                System.out.println("Veuillez entrer un nombre positif.");
            }
        }
        
        System.out.println("Somme des nombres : " + sum);
    }
}


