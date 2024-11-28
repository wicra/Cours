import java.io.File;
import java.util.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

// The main method must be in a class named "Main".
public class Main {
    public static void main(String[] args) {
        
        // EXO_01
        System.out.println("EXO_01");
        System.out.println("Hello world!");
        System.out.println("\n");
        // EXO_02
        System.out.println("EXO_02");
        System.out.println(2+3);
        System.out.println("\n");
        
        // EXO_03
        System.out.println("EXO_03");
        System.out.println(2/3);
        System.out.println("\n");

        // EXO_04
        System.out.println("EXO_04");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Entrez un nombre : ");
        int valeur1 = scanner.nextInt();
        System.out.print("Entrez un autre nombre : ");
        int valeur2 = scanner.nextInt();
        System.out.println("Le résultat est : " + (valeur1 * valeur2));
        System.out.println("\n");
        

        // EXO_05
        System.out.println("EXO_05");
        int nbTable =5;
        for(int i =0;i<=10;i++){
            System.out.println(nbTable + "X" + i + "=" + nbTable*i);
        }
        System.out.println("\n");
        
        // EXO_06
        calculer_aire_per(4.2);

        // EXO_07
        System.out.println("EXO_07");
        Scanner nombre = new Scanner(System.in); 
        System.out.print("Entrez premier nombre : ");
        int nb1 = nombre.nextInt();
        System.out.print("Entrez deuxième nombre : ");
        int nb2 = nombre.nextInt();
        System.out.print("Entrez troisième nombre : ");
        int nb3 = nombre.nextInt();
        System.out.println("La moyenne est : " + ((nb1+nb2+nb3)/3));
        System.out.println("\n");
        
        // EXO_08
        System.out.println("EXO_08");
        int e = 1;
        int b = 2;
        System.out.println("Avant l'échange : e = " + e + ", b = " + b);
        int temp1 = e; 
        e = b;
        b = temp1; 
        System.out.println("Après l'échange : e = " + e + ", b = " + b);
        System.out.println("\n");
         
        // EXO_09
        System.out.println("EXO_09");
        factoriel(5);
        System.out.println("\n");

        // EXO_10
        System.out.println("EXO_10");
        reverse("WayToLearnX");

        // EXO_11
        System.out.println("EXO_11");
        //maxtab({1, 15, 3, 8, 25, 4, 5});

        // EXO_12
        System.out.println("EXO_12");
        ascii('A'); 

        // EXO_13
        System.out.println("EXO_13");
        tailleFichier("/Users/wicramachine/Cours/java/Exo/Main.java");

        // EXO_14 & EXO_15
        System.out.println("EXO_14 & EXO_15");
        afficherHeure();

        // EXO_16
        System.out.println("EXO_16");
        exercice16();
                
        // EXO_17
        System.out.println("\nEXO_17");
        exercice17();

        // EXO_18
        System.out.println("\nEXO_18");
        exercice18();
    }

    // EXO_06
    public static void calculer_aire_per(double rayon) {
        double aire = Math.PI * rayon * rayon;        
        double perimetre = 2 * Math.PI * rayon;  
        
        System.out.println("EXO_06");
        System.out.println("L'aire du cercle est : " + aire);
        System.out.println("Le périmètre du cercle est : " + perimetre);
        System.out.println("\n");
    }

    // EXO_09
    public static void factoriel(int n) {
        for(int j = n-1;j> 0;j--){
            n *=j; 
        }
        System.out.println(n);
    }

    // EXO_10
    public static void reverse(String str) {
        String motInverse = ""; 
        
        for (int i = str.length() - 1; i >= 0; i--) {
            motInverse += str.charAt(i); 
        } 
        System.out.println(motInverse); 
    }

    // EXO_11
    public static int maxtab(int[] tab) {
        int maxtemp = tab[0]; 
        
        for (int i = 1; i < tab.length; i++) {
            if (tab[i] > maxtemp) {
                maxtemp = tab[i]; 
            }
        }
        
        return maxtemp;
    }

    // EXO_12
    public static void ascii(char caractere) {
        byte valeurAscii = (byte) caractere;
        System.out.println("Le caractère '" + caractere + "' a pour valeur ASCII : " + (valeurAscii & 0xFF));
    }

    // EXO_13
    public static void tailleFichier(String chemin) {
        File fichier = new File(chemin);
        if (fichier.exists() && fichier.isFile()) {
            long taille = fichier.length();
            System.out.println("La taille du fichier '" + fichier.getName() 
            + "' est : " + taille + " octets");
        } else {
            System.out.println("Le fichier n'existe pas ou n'est pas un fichier valide");
        }
    }

    // EXO_14 & EXO_15
    public static void afficherHeure() {
        LocalDateTime maintenant = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm:ss");
        String heure = maintenant.format(formatter);
        System.out.println("L'heure actuelle est : " + heure);
    }

    // EXO_16
    public static void exercice16() {
        Scanner vitesse = new Scanner(System.in);
        System.out.print("Entrez la distance parcourue en miles : ");
        double distance = vitesse.nextDouble();
        System.out.print("Entrez le temps mis en heures : ");
        double temps = vitesse.nextDouble();
        vitesse.close();
        double vitesseMoyenne = distance / temps;
        System.out.println("La vitesse moyenne est de " + vitesseMoyenne + " miles par heure");
    }

    // EXO_17
    public static void exercice17() {
        double distanceKm = 15.0;
        int minutes = 50;
        int secondes = 10;
        double tempsHeures = (minutes + (secondes / 60.0)) / 60.0;
        double vitesseMoyenne = distanceKm / tempsHeures;
        
        System.out.printf("Pour une distance de %.2f km parcourue en %d minutes et %d secondes,%n", 
            distanceKm, minutes, secondes);
        System.out.printf("La vitesse moyenne est de %.2f kilomètres par heure%n", vitesseMoyenne);
    }
    
    // EXO_18
    public static void exercice18() {
        // Coefficients du système d'équations
        // ax + by = e
        // cx + dy = f
        double a = 2;  // coefficient de x dans la première équation
        double b = 3;  // coefficient de y dans la première équation
        double c = 1;  // coefficient de x dans la deuxième équation
        double d = -1; // coefficient de y dans la deuxième équation
        double e = 8;  // terme constant de la première équation
        double f = 2;  // terme constant de la deuxième équation
        
        // Calcul du déterminant principal
        double determinant = a * d - b * c;
        
        if (determinant == 0) {
            System.out.println("Le système n'a pas de solution unique (déterminant = 0)");
            return;
        }
        
        // Calcul de x et y selon la règle de Cramer
        double x = (e * d - b * f) / determinant;
        double y = (a * f - e * c) / determinant;
        
        // Affichage du système d'équations
        System.out.println("Système d'équations :");
        System.out.printf("%.1fx + %.1fy = %.1f%n", a, b, e);
        System.out.printf("%.1fx + %.1fy = %.1f%n", c, d, f);
        
        // Affichage des solutions
        System.out.println("\nSolutions :");
        System.out.printf("x = %.2f%n", x);
        System.out.printf("y = %.2f%n", y);
        
        // Vérification des solutions
        double eq1 = a * x + b * y;
        double eq2 = c * x + d * y;
        System.out.println("\nVérification :");
        System.out.printf("Équation 1 : %.2f = %.2f%n", eq1, e);
        System.out.printf("Équation 2 : %.2f = %.2f%n", eq2, f);
    }

}
