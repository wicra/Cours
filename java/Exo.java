import java.util.*;


// The main method must be in a class named "Main".
public class Main {
    public static void main(String[] args) {
        
        // EXO_01
        System.out.println("EXO_01");
        System.out.println("Hello world!");
    
        // EXO_02
        System.out.println("EXO_02");
        System.out.println(2+3);

        // EXO_03
        System.out.println("EXO_03");
        System.out.println(2/3);

        // EXO_04
        System.out.println("EXO_04");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Entrez un nombre : ");
        int valeur1 = scanner.nextInt();
        System.out.print("Entrez un autre nombre : ");
        int valeur2 = scanner.nextInt();
        scanner.close();
        System.out.println("Le résultat est : " + (valeur1 * valeur2));
        

        // EXO_05
        System.out.println("EXO_05");
        int nbTable =5;
        for(int i =0;i<=10;i++){
            System.out.println(nbTable + "X" + i + "=" + nbTable*i);
        }
        
        // EXO_06
        calculer_aire_per(4.2);

        // EXO_07
        System.out.println("EXO_07");
        //Scanner scanner = new Scanner(System.in);  !!!!DEJA IMLPORTER!!! 
        System.out.print("Entrez premier nombre : ");
        int nb1 = scanner.nextInt();
        System.out.print("Entrez deuxième nombre : ");
        int nb2 = scanner.nextInt();
        System.out.print("Entrez troisième nombre : ");
        int nb3 = scanner.nextInt();
        scanner.close();
        System.out.println("La moyenne est : " + ((nb1+nb2+nb3)/3));
        
        // EXO_08
        System.out.println("EXO_08");
        int e = 1;
        int b = 2;
        int temp1 =b;
        int b =temp1;
        System.out.println("Avant l'échange :" + "e = " + e + "," + "b = " + b);
        System.out.println("Avant l'échange :" + "e = " + e + "," + "b = " + b);

    }

    // EXO_06
    public static void calculer_aire_per(double rayon) {
        double aire = Math.PI * rayon * rayon;        
        double perimetre = 2 * Math.PI * rayon;  
        
        System.out.println("EXO_06");
        System.out.println("L'aire du cercle est : " + aire);
        System.out.println("Le périmètre du cercle est : " + perimetre);
    }

    
}

