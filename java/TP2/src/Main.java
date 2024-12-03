import tp2.lib.Painter;

public class Main {

    public static void main(String[] args) {
        Painter painter = new Painter(400, 400);

        // Appeler la méthode pour dessiner la roue
        Roue.dessinerRoue(painter);
    }
}
