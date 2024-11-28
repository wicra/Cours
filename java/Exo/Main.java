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
}
