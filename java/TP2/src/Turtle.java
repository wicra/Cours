import java.awt.Color;
import tp2.lib.Tools;
import tp2.lib.Painter;

public class Turtle { 
    private Color penColor;
    private double angleDirection;
    private Point position;
    private boolean penIsDown;
    private Painter painter;

    public Turtle(int width, int height) {
        this.penColor = null;
        this.angleDirection = 270; // Pointe vers le Nord (90 degrés dans le sens inverse des aiguilles d'une montre)
        this.painter = new Painter(width, height);
        this.penIsDown = false;
        this.position = new Point(width/2, height/2); // Centre de la fenêtre
    }

    public void moveForward(double distance) {
        Tools.sleep(500);
        double radians = Math.toRadians(angleDirection);
        double newX = position.getX() + distance * Math.cos(radians);
        double newY = position.getY() + distance * Math.sin(radians);
        
        if (penIsDown && penColor != null) {
            Point newPosition = new Point(newX, newY);
            newPosition.drawLine(position, painter, penColor);
        }
        
        position = new Point(newX, newY);
    }

    public void setColor(Color color) {
        this.penColor = color;
    }

    public void turnLeft(double angle) {
        this.angleDirection = (this.angleDirection - angle) % 360;
    }

    public void turnRight(double angle) {
        this.angleDirection = (this.angleDirection + angle) % 360;
    }

    public void setPenDown() {
        this.penIsDown = true;
    }

    public void setPenUp() {
        this.penIsDown = false;
    }

    public void drawString(String sequence, double length, double angle) {
        for (char c : sequence.toCharArray()) {
            switch (c) {
                case 'A':
                    moveForward(length);
                    break;
                case '+':
                    turnRight(angle);
                    break;
                case '-':
                    turnLeft(angle);
                    break;
            }
        }
    }

    public static void main(String[] args) { 
        Turtle turtle = new Turtle(400, 400); 
        turtle.setColor(Color.red); 
        turtle.setPenDown(); 
        turtle.moveForward(40); 
        turtle.turnLeft(90); 
        turtle.moveForward(40); 
        turtle.turnLeft(90); 
        turtle.moveForward(40); 
        turtle.turnLeft(90); 
        turtle.moveForward(40); 
    } 
}