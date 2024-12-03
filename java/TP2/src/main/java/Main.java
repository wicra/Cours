import tp2.lib.Painter;
import java.awt.Color;

public class Main {
    public static void drawSquare(Turtle turtle, int size) {
        for (int i = 0; i < 4; i++) {
            turtle.moveForward(size);
            turtle.turnLeft(90);
        }
    }

    public static void main(String[] args) {
        Turtle turtle = new Turtle(800, 600);
        turtle.setColor(Color.black);
        turtle.setPenDown();
        int n = 20;
        for (int i = 0; i < n; i++) {
            turtle.turnRight(360.0 / n);
            drawSquare(turtle, 100);
        }
    }
}
